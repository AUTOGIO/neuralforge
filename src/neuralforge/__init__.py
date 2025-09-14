"""
NeuralForge - Professional AI & Automation Toolkit for Apple Silicon

A comprehensive platform that combines Neural Engine monitoring, AI memory management,
Core ML integration, and intelligent automation tools in a unified, production-ready system.
"""

__version__ = "1.0.0"
__author__ = "Eduardo Giovannini"
__email__ = "eduardo@giovannini.us"
__description__ = "Professional AI & Automation Toolkit for Apple Silicon"

# Core modules
from .launcher import NeuralVaultLauncher

# AI modules
from ..ai.memory_buffer import ConfigurableMemoryBuffer

# Core modules
from ..core.neural_check import NeuralEngineMonitor
from ..core.coreml import CoreMLConverter
from ..core.folder_organizer import FileOrganizer

# Integration modules
from ..integration.system_integration import SystemIntegration

__all__ = [
    "NeuralVaultLauncher",
    "ConfigurableMemoryBuffer", 
    "NeuralEngineMonitor",
    "CoreMLConverter",
    "FileOrganizer",
    "SystemIntegration",
    "__version__",
    "__author__",
    "__email__",
    "__description__",
]
