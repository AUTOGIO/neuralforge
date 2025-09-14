# 🧠 AI Memory Buffer API Documentation

## Overview

The `ai.memory_buffer` module provides a sophisticated AI memory system with PostgreSQL backend support, multi-provider configuration, and advanced analytics capabilities.

## Classes

### `ConfigurableMemoryBuffer`

Main interface for AI memory management with configurable backend providers.

#### Constructor

```python
def __init__(self, config_path: str = "config/memory_config.json", config_override: Dict = None)
```

**Parameters:**
- `config_path` (str): Path to configuration file
- `config_override` (Dict, optional): Override configuration parameters

**Example:**
```python
# Default configuration
memory = ConfigurableMemoryBuffer()

# Custom configuration
memory = ConfigurableMemoryBuffer(
    config_override={"provider": "postgresql"}
)
```

#### Methods

##### `add_memory_entry()`

Store a new AI interaction in memory.

```python
def add_memory_entry(
    self,
    agent_name: str,
    task: str,
    response: str,
    success_rating: int,
    model_used: str = "unknown",
    tokens_used: int = 0,
    metadata: Dict = None
) -> bool
```

**Parameters:**
- `agent_name` (str): Name of the AI agent
- `task` (str): Description of the task performed
- `response` (str): AI's response/output
- `success_rating` (int): Rating from 1-5 for success
- `model_used` (str, optional): Model identifier
- `tokens_used` (int, optional): Number of tokens consumed
- `metadata` (Dict, optional): Additional metadata

**Returns:**
- `bool`: True if successfully stored

**Example:**
```python
success = memory.add_memory_entry(
    agent_name="GPT-4",
    task="Analyze quarterly sales data",
    response="Q3 sales increased 15% YoY driven by...",
    success_rating=5,
    model_used="gpt-4-turbo",
    tokens_used=450,
    metadata={"department": "sales", "quarter": "Q3"}
)
```

##### `query_memory()`

Search and retrieve relevant memories.

```python
def query_memory(
    self,
    query: str,
    limit: int = 10,
    min_relevance: float = 0.1
) -> List[Dict]
```

**Parameters:**
- `query` (str): Search query
- `limit` (int): Maximum results to return
- `min_relevance` (float): Minimum relevance score

**Returns:**
- `List[Dict]`: List of matching memory entries

**Example:**
```python
results = memory.query_memory(
    query="sales analysis quarterly",
    limit=5,
    min_relevance=0.3
)

for result in results:
    print(f"Task: {result['task']}")
    print(f"Agent: {result['agent_name']}")
    print(f"Relevance: {result['relevance_score']:.2f}")
```

##### `get_memory_stats()`

Retrieve comprehensive memory system statistics.

```python
def get_memory_stats(self) -> Dict[str, Union[int, float, str]]
```

**Returns:**
- `Dict`: Statistics including total entries, average ratings, etc.

**Example:**
```python
stats = memory.get_memory_stats()
print(f"Total memories: {stats['total_entries']}")
print(f"Average success rate: {stats['avg_success_rating']:.2f}")
print(f"Most used model: {stats['top_model']}")
```

##### `get_model_performance()`

Get performance analytics for specific models.

```python
def get_model_performance(self, model_name: str = None) -> Dict
```

**Parameters:**
- `model_name` (str, optional): Specific model to analyze

**Returns:**
- `Dict`: Performance metrics and analytics

**Example:**
```python
# All models performance
all_performance = memory.get_model_performance()

# Specific model performance  
gpt4_performance = memory.get_model_performance("gpt-4-turbo")
print(f"Average rating: {gpt4_performance['avg_rating']}")
print(f"Total usage: {gpt4_performance['usage_count']}")
```

##### `cleanup_old_memories()`

Remove old or low-rated memories to optimize storage.

```python
def cleanup_old_memories(
    self,
    days_old: int = 90,
    min_rating: int = 2
) -> int
```

**Parameters:**
- `days_old` (int): Remove memories older than this many days
- `min_rating` (int): Minimum rating to keep

**Returns:**
- `int`: Number of memories removed

---

### `PostgreSQLMemoryBuffer`

PostgreSQL-specific implementation with advanced database features.

#### Constructor

```python
def __init__(self, connection_params: Dict[str, str])
```

**Parameters:**
- `connection_params` (Dict): Database connection parameters

**Example:**
```python
postgres_memory = PostgreSQLMemoryBuffer({
    "host": "localhost",
    "port": 5432,
    "database": "ai_memory",
    "user": "username",
    "password": "password"
})
```

#### Methods

##### `setup_database()`

Initialize database schema and tables.

```python
def setup_database(self) -> bool
```

**Returns:**
- `bool`: True if setup successful

##### `full_text_search()`

Perform advanced full-text search using PostgreSQL capabilities.

```python
def full_text_search(
    self,
    query: str,
    language: str = "english"
) -> List[Dict]
```

**Parameters:**
- `query` (str): Search query with PostgreSQL text search syntax
- `language` (str): Text search language configuration

**Returns:**
- `List[Dict]`: Ranked search results

**Example:**
```python
# Advanced text search
results = postgres_memory.full_text_search(
    query="sales & (quarterly | monthly)",
    language="english"
)
```

##### `get_conversation_thread()`

Retrieve related memories forming a conversation thread.

```python
def get_conversation_thread(
    self,
    memory_id: int,
    max_depth: int = 5
) -> List[Dict]
```

**Parameters:**
- `memory_id` (int): Starting memory ID
- `max_depth` (int): Maximum thread depth

**Returns:**
- `List[Dict]`: Connected memories in thread

---

## Data Models

### Memory Entry Structure

```python
{
    "id": 123,
    "agent_name": "GPT-4",
    "task": "Analyze customer feedback",
    "response": "Customer satisfaction improved by...",
    "success_rating": 4,
    "model_used": "gpt-4-turbo",
    "tokens_used": 320,
    "timestamp": "2024-08-28T10:30:00Z",
    "metadata": {
        "department": "customer_service",
        "priority": "high"
    },
    "relevance_score": 0.87  # Only in search results
}
```

### Statistics Structure

```python
{
    "total_entries": 1247,
    "avg_success_rating": 4.2,
    "total_tokens_used": 125430,
    "top_model": "gpt-4-turbo",
    "models_used": ["gpt-4-turbo", "claude-3-sonnet", "local-llama"],
    "date_range": {
        "oldest": "2024-07-01T00:00:00Z",
        "newest": "2024-08-28T12:00:00Z"
    },
    "provider_info": {
        "type": "postgresql",
        "status": "connected",
        "version": "17.1"
    }
}
```

## Configuration

### Configuration File Structure

```json
{
  "provider": "postgresql",
  "postgresql": {
    "enabled": true,
    "host": "localhost",
    "port": 5432,
    "database": "ai_memory",
    "user": "username",
    "password": "",
    "auto_create_db": true,
    "ssl_mode": "prefer",
    "pool_size": 5
  },
  "openai": {
    "enabled": false,
    "api_key": "",
    "model": "gpt-4-turbo"
  },
  "ollama": {
    "enabled": false,
    "host": "http://localhost:11434",
    "model": "llama2"
  },
  "local": {
    "enabled": true,
    "models_path": "/Volumes/MICRO/models"
  },
  "fallback": {
    "provider": "simple",
    "storage_path": "memory_storage.json"
  }
}
```

### Environment Variables

```bash
# Database configuration
export POSTGRES_PASSWORD="your_secure_password"
export POSTGRES_SSL_MODE="require"

# API keys
export OPENAI_API_KEY="sk-..."
export OLLAMA_HOST="http://localhost:11434"

# Performance tuning
export MEMORY_BUFFER_CACHE_SIZE="1000"
export MEMORY_BUFFER_BATCH_SIZE="50"
```

## Error Handling

### Exception Classes

```python
class MemoryError(Exception):
    """Base exception for memory operations"""
    pass

class ConnectionError(MemoryError):
    """Database connection issues"""
    pass

class ConfigurationError(MemoryError):
    """Configuration problems"""
    pass

class ProviderError(MemoryError):
    """AI provider issues"""
    pass
```

### Error Handling Example

```python
from ai.memory_buffer import ConfigurableMemoryBuffer, MemoryError

try:
    memory = ConfigurableMemoryBuffer()
    
    success = memory.add_memory_entry(
        agent_name="Claude-3",
        task="Data analysis",
        response="Analysis complete",
        success_rating=5
    )
    
    if not success:
        print("Failed to store memory entry")
        
except ConnectionError as e:
    print(f"Database connection failed: {e}")
    # Fallback to simple storage
    
except ConfigurationError as e:
    print(f"Configuration error: {e}")
    # Use default configuration
    
except MemoryError as e:
    print(f"Memory system error: {e}")
    # Log error and continue
```

## Performance Optimization

### Connection Pooling

```python
# Configure connection pooling
memory = ConfigurableMemoryBuffer()
memory.setup_connection_pool(
    min_connections=2,
    max_connections=10,
    pool_timeout=30
)
```

### Batch Operations

```python
# Batch memory entries for better performance
entries = [
    {
        "agent_name": "GPT-4",
        "task": f"Task {i}",
        "response": f"Response {i}",
        "success_rating": 4
    }
    for i in range(100)
]

memory.add_memory_entries_batch(entries)
```

### Caching

```python
# Enable query result caching
memory.enable_cache(
    max_size=1000,
    ttl_seconds=300
)

# Cached queries will be faster
results = memory.query_memory("analysis")  # First call: database query
results = memory.query_memory("analysis")  # Second call: cached result
```

## Best Practices

### 1. Memory Entry Quality

```python
# Good: Descriptive and structured
memory.add_memory_entry(
    agent_name="GPT-4-Financial",
    task="Q3 2024 financial analysis with risk assessment",
    response="Revenue growth 12% YoY, identified 3 risk factors...",
    success_rating=5,
    model_used="gpt-4-turbo",
    tokens_used=750,
    metadata={
        "quarter": "Q3-2024",
        "analysis_type": "financial",
        "risk_level": "medium"
    }
)

# Bad: Vague and minimal
memory.add_memory_entry(
    agent_name="AI",
    task="analysis",
    response="done",
    success_rating=3
)
```

### 2. Query Optimization

```python
# Good: Specific queries with context
results = memory.query_memory(
    "financial analysis Q3 revenue growth",
    limit=5,
    min_relevance=0.4
)

# Bad: Overly broad queries
results = memory.query_memory("analysis")
```

### 3. Regular Maintenance

```python
# Regular cleanup of old/poor memories
cleaned = memory.cleanup_old_memories(
    days_old=90,
    min_rating=2
)
print(f"Cleaned up {cleaned} old memories")

# Vacuum database for PostgreSQL
if hasattr(memory, 'vacuum_database'):
    memory.vacuum_database()
```

## Integration Examples

### With n8n Workflows

```python
# n8n webhook integration
from flask import Flask, request, jsonify
from ai.memory_buffer import ConfigurableMemoryBuffer

app = Flask(__name__)
memory = ConfigurableMemoryBuffer()

@app.route('/n8n/memory', methods=['POST'])
def n8n_memory_webhook():
    data = request.get_json()
    
    success = memory.add_memory_entry(
        agent_name=data.get('agent_name', 'n8n-workflow'),
        task=data['task'],
        response=data['response'],
        success_rating=data.get('rating', 3),
        metadata=data.get('metadata', {})
    )
    
    return jsonify({"success": success})
```

### With Core ML Models

```python
# Store Core ML model performance
from core.coreml import CoreMLConverter

converter = CoreMLConverter()
model = converter.convert_pytorch_model(pytorch_model)

# Benchmark and store results
benchmark = converter.benchmark_model(model)

memory.add_memory_entry(
    agent_name="CoreML-Converter",
    task=f"Convert and benchmark {model.name}",
    response=f"Conversion successful, avg inference: {benchmark['avg_time']:.2f}ms",
    success_rating=5 if benchmark['avg_time'] < 50 else 4,
    metadata={
        "model_size": benchmark['model_size'],
        "inference_time": benchmark['avg_time'],
        "platform": "Apple Silicon"
    }
)
```
