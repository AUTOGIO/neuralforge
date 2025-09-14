#!/usr/bin/env python3
"""
AI Memory Buffer System with PostgreSQL Backend
Advanced memory management for AI interactions
"""
import json
import sqlite3
import psycopg2
from datetime import datetime
from typing import Dict, List, Any, Optional, Union
from pathlib import Path
import os

class MemoryEntry:
    """Data model for memory entries"""
    
    def __init__(self, agent_name: str, task: str, response: str, 
                 success_rating: int, model_used: str = "unknown", 
                 tokens_used: int = 0, metadata: Dict = None):
        self.agent_name = agent_name
        self.task = task
        self.response = response
        self.success_rating = success_rating
        self.model_used = model_used
        self.tokens_used = tokens_used
        self.metadata = metadata or {}
        self.timestamp = datetime.now().isoformat()

class SimpleMemoryBuffer:
    """Simple file-based memory storage"""
    
    def __init__(self, storage_path: str = "memory_storage.json"):
        self.storage_path = Path(storage_path)
        self.memories = self._load_memories()
    
    def _load_memories(self) -> List[Dict]:
        """Load memories from file"""
        if self.storage_path.exists():
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _save_memories(self):
        """Save memories to file"""
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.memories, f, indent=2, ensure_ascii=False)
    
    def add_memory_entry(self, entry: MemoryEntry) -> bool:
        """Add a memory entry"""
        try:
            memory_dict = {
                'id': len(self.memories) + 1,
                'agent_name': entry.agent_name,
                'task': entry.task,
                'response': entry.response,
                'success_rating': entry.success_rating,
                'model_used': entry.model_used,
                'tokens_used': entry.tokens_used,
                'metadata': entry.metadata,
                'timestamp': entry.timestamp
            }
            self.memories.append(memory_dict)
            self._save_memories()
            return True
        except Exception as e:
            print(f"Error adding memory entry: {e}")
            return False
    
    def query_memory(self, query: str, limit: int = 10) -> List[Dict]:
        """Query memories by text search"""
        results = []
        query_lower = query.lower()
        
        for memory in self.memories:
            score = 0
            if query_lower in memory['task'].lower():
                score += 2
            if query_lower in memory['response'].lower():
                score += 1
            if query_lower in memory['agent_name'].lower():
                score += 1
            
            if score > 0:
                memory['relevance_score'] = score / 4.0
                results.append(memory)
        
        # Sort by relevance score
        results.sort(key=lambda x: x['relevance_score'], reverse=True)
        return results[:limit]
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get memory system statistics"""
        if not self.memories:
            return {
                'total_entries': 0,
                'avg_success_rating': 0,
                'total_tokens_used': 0,
                'top_model': 'none',
                'models_used': [],
                'date_range': {'oldest': None, 'newest': None}
            }
        
        total_entries = len(self.memories)
        avg_rating = sum(m['success_rating'] for m in self.memories) / total_entries
        total_tokens = sum(m['tokens_used'] for m in self.memories)
        
        models = [m['model_used'] for m in self.memories if m['model_used'] != 'unknown']
        top_model = max(set(models), key=models.count) if models else 'none'
        
        timestamps = [m['timestamp'] for m in self.memories]
        date_range = {
            'oldest': min(timestamps) if timestamps else None,
            'newest': max(timestamps) if timestamps else None
        }
        
        return {
            'total_entries': total_entries,
            'avg_success_rating': round(avg_rating, 2),
            'total_tokens_used': total_tokens,
            'top_model': top_model,
            'models_used': list(set(models)),
            'date_range': date_range
        }

class PostgreSQLMemoryBuffer:
    """PostgreSQL-based memory storage"""
    
    def __init__(self, connection_params: Dict[str, str]):
        self.connection_params = connection_params
        self.connection = None
    
    def connect(self):
        """Connect to PostgreSQL database"""
        try:
            self.connection = psycopg2.connect(**self.connection_params)
            return True
        except Exception as e:
            print(f"PostgreSQL connection failed: {e}")
            return False
    
    def setup_database(self) -> bool:
        """Setup database schema"""
        if not self.connect():
            return False
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ai_memories (
                        id SERIAL PRIMARY KEY,
                        agent_name VARCHAR(100) NOT NULL,
                        task TEXT NOT NULL,
                        response TEXT NOT NULL,
                        success_rating INTEGER CHECK (success_rating >= 1 AND success_rating <= 5),
                        model_used VARCHAR(100),
                        tokens_used INTEGER DEFAULT 0,
                        metadata JSONB,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_ai_memories_task 
                    ON ai_memories USING gin(to_tsvector('english', task))
                """)
                
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_ai_memories_response 
                    ON ai_memories USING gin(to_tsvector('english', response))
                """)
                
                self.connection.commit()
                return True
        except Exception as e:
            print(f"Database setup failed: {e}")
            return False
        finally:
            if self.connection:
                self.connection.close()

class ConfigurableMemoryBuffer:
    """Main memory buffer with configurable backend"""
    
    def __init__(self, config_path: str = "config/memory_config.json", 
                 config_override: Dict = None):
        self.config = self._load_config(config_path, config_override)
        self.buffer = self._initialize_buffer()
    
    def _load_config(self, config_path: str, config_override: Dict = None) -> Dict:
        """Load configuration from file"""
        config_file = Path(config_path)
        if config_file.exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            except:
                config = {}
        else:
            config = {}
        
        if config_override:
            config.update(config_override)
        
        return config
    
    def _initialize_buffer(self):
        """Initialize the appropriate memory buffer"""
        provider = self.config.get('provider', 'simple')
        
        if provider == 'postgresql':
            pg_config = self.config.get('postgresql', {})
            if pg_config.get('enabled', False):
                buffer = PostgreSQLMemoryBuffer({
                    'host': pg_config.get('host', 'localhost'),
                    'port': pg_config.get('port', 5432),
                    'database': pg_config.get('database', 'ai_memory'),
                    'user': pg_config.get('user', 'postgres'),
                    'password': pg_config.get('password', '')
                })
                if buffer.setup_database():
                    return buffer
        
        # Fallback to simple storage
        fallback_config = self.config.get('fallback', {})
        storage_path = fallback_config.get('storage_path', 'memory_storage.json')
        return SimpleMemoryBuffer(storage_path)
    
    def add_memory_entry(self, agent_name: str, task: str, response: str,
                        success_rating: int, model_used: str = "unknown",
                        tokens_used: int = 0, metadata: Dict = None) -> bool:
        """Add a memory entry"""
        entry = MemoryEntry(agent_name, task, response, success_rating,
                          model_used, tokens_used, metadata)
        return self.buffer.add_memory_entry(entry)
    
    def query_memory(self, query: str, limit: int = 10, 
                    min_relevance: float = 0.1) -> List[Dict]:
        """Query memories"""
        return self.buffer.query_memory(query, limit)
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get memory statistics"""
        return self.buffer.get_memory_stats()
    
    def get_model_performance(self, model_name: str = None) -> Dict:
        """Get model performance analytics"""
        stats = self.get_memory_stats()
        return {
            'total_models': len(stats['models_used']),
            'top_model': stats['top_model'],
            'avg_rating': stats['avg_success_rating'],
            'total_usage': stats['total_entries']
        }

def main():
    """Main entry point for testing"""
    print("🧠 AI Memory Buffer System")
    print("=" * 40)
    
    # Initialize memory system
    memory = ConfigurableMemoryBuffer()
    
    # Add sample memory
    success = memory.add_memory_entry(
        agent_name="GPT-4",
        task="System analysis for M3 iMac",
        response="System is running optimally with 85% efficiency",
        success_rating=5,
        model_used="gpt-4-turbo",
        tokens_used=150
    )
    
    if success:
        print("✅ Memory entry added successfully")
    else:
        print("❌ Failed to add memory entry")
    
    # Query memories
    results = memory.query_memory("system analysis")
    print(f"🔍 Found {len(results)} related memories")
    
    # Get statistics
    stats = memory.get_memory_stats()
    print(f"📊 Total memories: {stats['total_entries']}")
    print(f"⭐ Average rating: {stats['avg_success_rating']}")

if __name__ == "__main__":
    main()
