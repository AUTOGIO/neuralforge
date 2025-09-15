# NeuralForge Code Templates

## Python Class Template
```python
"""
Module description for NeuralForge component.
"""
import logging
from typing import Optional, Dict, Any
from rich.console import Console

console = Console()
logger = logging.getLogger(__name__)

class ComponentName:
    """
    Component description for NeuralForge.
    
    Args:
        param1: Description of parameter
        param2: Description of parameter
    """
    
    def __init__(self, param1: str, param2: Optional[int] = None):
        self.param1 = param1
        self.param2 = param2
        self._setup()
    
    def _setup(self) -> None:
        """Initialize component setup."""
        try:
            # Setup logic here
            console.print(f"[green]✅ {self.__class__.__name__} initialized[/green]")
        except Exception as e:
            logger.error(f"Failed to initialize {self.__class__.__name__}: {e}")
            raise
    
    def method_name(self, param: str) -> Dict[str, Any]:
        """
        Method description.
        
        Args:
            param: Parameter description
            
        Returns:
            Dictionary with results
            
        Raises:
            ValueError: If parameter is invalid
        """
        try:
            # Method logic here
            return {"result": "success"}
        except Exception as e:
            logger.error(f"Method failed: {e}")
            raise
```

## Test Template
```python
"""
Tests for ComponentName.
"""
import pytest
from unittest.mock import Mock, patch
from src.module.component import ComponentName

class TestComponentName:
    """Test cases for ComponentName."""
    
    def test_initialization(self):
        """Test component initialization."""
        component = ComponentName("test_param")
        assert component.param1 == "test_param"
        assert component.param2 is None
    
    def test_method_success(self):
        """Test successful method execution."""
        component = ComponentName("test_param")
        result = component.method_name("test_input")
        assert result["result"] == "success"
    
    def test_method_error(self):
        """Test method error handling."""
        component = ComponentName("test_param")
        with pytest.raises(ValueError):
            component.method_name("")
```

## Configuration Template
```json
{
  "component_name": {
    "enabled": true,
    "param1": "default_value",
    "param2": 42,
    "advanced": {
      "option1": true,
      "option2": "value"
    }
  }
}
```
