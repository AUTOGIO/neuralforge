# 📚 NEURAL_CORE_VAULT API Documentation

Welcome to the NEURAL_CORE_VAULT API documentation. This section provides comprehensive documentation for all public APIs, classes, and functions.

## 📋 Table of Contents

- [Core Modules](#core-modules)
- [AI Modules](#ai-modules) 
- [Web Modules](#web-modules)
- [Configuration](#configuration)
- [Examples](#examples)

## 🧠 Core Modules

### [`core.neural_check`](neural_check.md)
Real-time Apple Neural Engine monitoring and performance analytics.

**Key Classes:**
- `NeuralEngineMonitor` - Main monitoring class
- `SystemMetrics` - System performance data

**Usage:**
```python
from core.neural_check import NeuralEngineMonitor

monitor = NeuralEngineMonitor()
monitor.start_monitoring()
```

### [`core.coreml`](coreml.md)
PyTorch to Core ML model conversion and optimization for Apple Silicon.

**Key Classes:**
- `CoreMLConverter` - Model conversion and optimization
- `ModelBenchmark` - Performance benchmarking

**Usage:**
```python
from core.coreml import CoreMLConverter

converter = CoreMLConverter()
model = converter.convert_pytorch_model(pytorch_model)
```

### [`core.folder_organizer`](folder_organizer.md)
Intelligent file organization with wxPython GUI interface.

**Key Classes:**
- `FolderOrganizerApp` - Main GUI application
- `FileOrganizer` - Core organization logic

## 🤖 AI Modules

### [`ai.memory_buffer`](memory_buffer.md)
Advanced AI memory system with PostgreSQL backend and multi-provider support.

**Key Classes:**
- `ConfigurableMemoryBuffer` - Main memory interface
- `PostgreSQLMemoryBuffer` - PostgreSQL-specific implementation
- `MemoryEntry` - Data model for memory entries

**Usage:**
```python
from ai.memory_buffer import ConfigurableMemoryBuffer

memory = ConfigurableMemoryBuffer()
memory.add_memory_entry(
    agent_name="GPT-4",
    task="Market analysis",
    response="Analysis complete...",
    success_rating=5
)
```

### [`ai.document_tagger`](document_tagger.md)
Document processing and intelligent tagging using NLTK.

**Key Functions:**
- `extract_keywords()` - Extract key terms from documents
- `generate_tags()` - Generate relevant tags
- `process_document()` - Complete document processing pipeline

### [`ai.document_processor_ui`](document_processor_ui.md)
UI interface for querying and processing embedded documents.

**Key Classes:**
- `DocumentProcessor` - Main processing interface
- `QueryEngine` - Document query functionality

## 🌐 Web Modules

### [`web.gui_scraper`](gui_scraper.md)
PyQt5-based web scraping with intelligent data extraction.

**Key Classes:**
- `WebScraperGUI` - Main GUI interface
- `ScrapingEngine` - Core scraping logic
- `DataExtractor` - Content extraction utilities

**Usage:**
```python
from web.gui_scraper import WebScraperGUI

scraper = WebScraperGUI()
scraper.show()
```

## ⚙️ Configuration

### [`config.memory_config`](config.md)
Configuration management for AI memory and database connections.

**Configuration Structure:**
```json
{
  "provider": "postgresql",
  "postgresql": {
    "host": "localhost",
    "port": 5432,
    "database": "ai_memory",
    "user": "username"
  }
}
```

## 🎯 Quick Examples

### Basic AI Memory Usage
```python
from ai.memory_buffer import ConfigurableMemoryBuffer

# Initialize memory system
memory = ConfigurableMemoryBuffer()

# Store an AI interaction
memory.add_memory_entry(
    agent_name="Claude-3",
    task="Code review for Python module",
    response="Found 3 optimization opportunities...",
    success_rating=4,
    model_used="claude-3-sonnet",
    tokens_used=500
)

# Query past interactions
results = memory.query_memory("code review")
print(f"Found {len(results)} related memories")

# Get performance statistics
stats = memory.get_memory_stats()
print(f"Total memories: {stats['total_entries']}")
```

### Neural Engine Monitoring
```python
from core.neural_check import NeuralEngineMonitor
import time

# Start monitoring
monitor = NeuralEngineMonitor()

# Get current metrics
metrics = monitor.get_system_metrics()
print(f"Neural Engine utilization: {metrics.get('ane_power', 'N/A')}")

# Start real-time monitoring (runs until interrupted)
monitor.start_monitoring()
```

### Core ML Model Conversion
```python
from core.coreml import CoreMLConverter
import torch

# Initialize converter
converter = CoreMLConverter()

# Convert a PyTorch model
pytorch_model = torch.nn.Linear(10, 1)
coreml_model = converter.convert_pytorch_model(
    pytorch_model,
    input_shape=(1, 10),
    output_name="prediction"
)

# Benchmark performance
benchmark = converter.benchmark_model(coreml_model)
print(f"Inference time: {benchmark['avg_time']:.3f}ms")
```

## 🔧 Advanced Usage

### Custom Memory Providers
```python
from ai.memory_buffer import ConfigurableMemoryBuffer

# Configure for Ollama local models
config = {
    "provider": "ollama",
    "ollama": {
        "host": "http://localhost:11434",
        "model": "llama2"
    }
}

memory = ConfigurableMemoryBuffer(config_override=config)
```

### Performance Optimization
```python
# Enable performance monitoring
import os
os.environ['NEURAL_VAULT_DEBUG'] = 'true'

# Use connection pooling for PostgreSQL
memory = ConfigurableMemoryBuffer()
memory.setup_connection_pool(min_connections=2, max_connections=10)
```

## 🐛 Error Handling

All modules implement comprehensive error handling:

```python
from ai.memory_buffer import ConfigurableMemoryBuffer, MemoryError

try:
    memory = ConfigurableMemoryBuffer()
    memory.add_memory_entry(...)
except MemoryError as e:
    print(f"Memory operation failed: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 📊 Performance Considerations

### Memory System Performance
- **PostgreSQL**: Best for production, supports full-text search
- **Local Models**: Good for privacy-sensitive applications
- **Simple Storage**: Fastest for development and testing

### Neural Engine Monitoring
- **Polling Rate**: Default 1 second, configurable
- **Resource Usage**: <5% CPU overhead
- **Privileges**: No sudo required, some metrics may be limited

### Core ML Optimization
- **Model Size**: Smaller models perform better on Neural Engine
- **Data Types**: Float16 recommended for best performance
- **Batch Size**: Single predictions optimized for mobile devices

## 🔗 Related Documentation

- [Installation Guide](../installation.md)
- [Configuration Guide](../configuration.md)
- [Troubleshooting](../troubleshooting.md)
- [Contributing Guidelines](../../CONTRIBUTING.md)

---

For specific API details, see the individual module documentation files in this directory.
