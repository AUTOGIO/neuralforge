"""
Tests for Neural Engine monitoring functionality
"""
import pytest
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from core.neural_check import NeuralEngineMonitor


class TestNeuralEngineMonitor:
    """Test cases for NeuralEngineMonitor"""
    
    def test_initialization(self):
        """Test monitor initialization"""
        monitor = NeuralEngineMonitor()
        assert monitor is not None
        assert hasattr(monitor, 'get_system_metrics')
        assert hasattr(monitor, 'start_monitoring')
    
    def test_get_system_metrics(self):
        """Test system metrics retrieval"""
        monitor = NeuralEngineMonitor()
        metrics = monitor.get_system_metrics()
        
        assert isinstance(metrics, dict)
        assert 'timestamp' in metrics
        assert 'platform' in metrics
        
        # Check that platform is Apple Silicon
        assert metrics['platform'] == 'Apple Silicon M3'
    
    def test_metrics_structure(self):
        """Test metrics data structure"""
        monitor = NeuralEngineMonitor()
        metrics = monitor.get_system_metrics()
        
        expected_keys = [
            'timestamp', 'cpu_percent', 'memory_percent', 
            'memory_used_gb', 'memory_total_gb', 'platform'
        ]
        
        for key in expected_keys:
            assert key in metrics, f"Missing key: {key}"
    
    def test_error_handling(self):
        """Test error handling in metrics collection"""
        monitor = NeuralEngineMonitor()
        
        # Should not raise exceptions even if some metrics fail
        metrics = monitor.get_system_metrics()
        assert isinstance(metrics, dict)
    
    @pytest.mark.slow
    def test_monitoring_duration(self):
        """Test monitoring for a short duration"""
        monitor = NeuralEngineMonitor()
        
        # This test would run monitoring for a short time
        # In a real test, we'd mock the monitoring loop
        assert monitor.running is False
        monitor.running = True
        assert monitor.running is True
        monitor.stop_monitoring()
        assert monitor.running is False


if __name__ == "__main__":
    pytest.main([__file__])
