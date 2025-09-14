"""
Tests for AI Memory Buffer functionality
"""
import pytest
import sys
import tempfile
import os
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ai.memory_buffer import ConfigurableMemoryBuffer, MemoryEntry, SimpleMemoryBuffer


class TestMemoryEntry:
    """Test cases for MemoryEntry"""
    
    def test_memory_entry_creation(self):
        """Test creating a memory entry"""
        entry = MemoryEntry(
            agent_name="GPT-4",
            task="Test task",
            response="Test response",
            success_rating=5,
            model_used="gpt-4-turbo",
            tokens_used=100
        )
        
        assert entry.agent_name == "GPT-4"
        assert entry.task == "Test task"
        assert entry.response == "Test response"
        assert entry.success_rating == 5
        assert entry.model_used == "gpt-4-turbo"
        assert entry.tokens_used == 100
        assert entry.timestamp is not None


class TestSimpleMemoryBuffer:
    """Test cases for SimpleMemoryBuffer"""
    
    def test_initialization(self):
        """Test buffer initialization"""
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            temp_path = f.name
        
        try:
            buffer = SimpleMemoryBuffer(temp_path)
            assert buffer is not None
            assert buffer.storage_path == Path(temp_path)
        finally:
            os.unlink(temp_path)
    
    def test_add_memory_entry(self):
        """Test adding memory entries"""
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            temp_path = f.name
        
        try:
            buffer = SimpleMemoryBuffer(temp_path)
            
            entry = MemoryEntry(
                agent_name="Test Agent",
                task="Test task",
                response="Test response",
                success_rating=4
            )
            
            result = buffer.add_memory_entry(entry)
            assert result is True
            
            # Check that entry was stored
            assert len(buffer.memories) == 1
            assert buffer.memories[0]['agent_name'] == "Test Agent"
        finally:
            os.unlink(temp_path)
    
    def test_query_memory(self):
        """Test memory querying"""
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            temp_path = f.name
        
        try:
            buffer = SimpleMemoryBuffer(temp_path)
            
            # Add test entries
            entry1 = MemoryEntry("Agent1", "python programming", "Python is great", 5)
            entry2 = MemoryEntry("Agent2", "javascript coding", "JS is flexible", 4)
            entry3 = MemoryEntry("Agent3", "data analysis", "Data insights", 5)
            
            buffer.add_memory_entry(entry1)
            buffer.add_memory_entry(entry2)
            buffer.add_memory_entry(entry3)
            
            # Query for python-related entries
            results = buffer.query_memory("python")
            assert len(results) == 1
            assert results[0]['task'] == "python programming"
            
            # Query for coding-related entries
            results = buffer.query_memory("coding")
            assert len(results) == 2
            
        finally:
            os.unlink(temp_path)
    
    def test_get_memory_stats(self):
        """Test memory statistics"""
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            temp_path = f.name
        
        try:
            buffer = SimpleMemoryBuffer(temp_path)
            
            # Add test entries
            entry1 = MemoryEntry("Agent1", "Task1", "Response1", 5, tokens_used=100)
            entry2 = MemoryEntry("Agent2", "Task2", "Response2", 4, tokens_used=200)
            
            buffer.add_memory_entry(entry1)
            buffer.add_memory_entry(entry2)
            
            stats = buffer.get_memory_stats()
            
            assert stats['total_entries'] == 2
            assert stats['avg_success_rating'] == 4.5
            assert stats['total_tokens_used'] == 300
            assert stats['top_model'] == 'unknown'  # Default value
            
        finally:
            os.unlink(temp_path)


class TestConfigurableMemoryBuffer:
    """Test cases for ConfigurableMemoryBuffer"""
    
    def test_initialization_with_fallback(self):
        """Test initialization with fallback to simple storage"""
        buffer = ConfigurableMemoryBuffer()
        assert buffer is not None
        assert hasattr(buffer, 'add_memory_entry')
        assert hasattr(buffer, 'query_memory')
        assert hasattr(buffer, 'get_memory_stats')
    
    def test_add_memory_entry_fallback(self):
        """Test adding memory entries with fallback storage"""
        buffer = ConfigurableMemoryBuffer()
        
        result = buffer.add_memory_entry(
            agent_name="Test Agent",
            task="Test task",
            response="Test response",
            success_rating=5
        )
        
        assert result is True
    
    def test_query_memory_fallback(self):
        """Test querying memory with fallback storage"""
        buffer = ConfigurableMemoryBuffer()
        
        # Add test entry
        buffer.add_memory_entry(
            agent_name="Test Agent",
            task="python programming",
            response="Python is great for AI",
            success_rating=5
        )
        
        # Query for python-related entries
        results = buffer.query_memory("python")
        assert len(results) >= 1
    
    def test_get_memory_stats_fallback(self):
        """Test getting memory statistics with fallback storage"""
        buffer = ConfigurableMemoryBuffer()
        
        # Add test entry
        buffer.add_memory_entry(
            agent_name="Test Agent",
            task="Test task",
            response="Test response",
            success_rating=5
        )
        
        stats = buffer.get_memory_stats()
        assert isinstance(stats, dict)
        assert 'total_entries' in stats
        assert 'avg_success_rating' in stats


if __name__ == "__main__":
    pytest.main([__file__])
