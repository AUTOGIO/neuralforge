# 🧠 NeuralForge

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20Apple%20Silicon-lightgrey.svg)](https://support.apple.com/en-us/HT211814)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://img.shields.io/badge/tests-pytest-blue.svg)](https://pytest.org/)

> **Professional AI & Automation Toolkit** optimized for Apple Silicon (M3) Macs with enterprise-grade PostgreSQL 17 integration.

NeuralForge is a comprehensive platform that combines **Neural Engine monitoring**, **AI memory management**, **Core ML integration**, and **intelligent automation tools** in a unified, production-ready system.

## ✨ **Key Features**

### 🧠 **Neural Engine Monitoring**
- Real-time Apple Neural Engine performance tracking
- CPU/GPU/ANE power consumption analysis
- MLX model discovery and optimization
- Professional terminal dashboard with Rich UI

### 💾 **AI Memory System** 
- **PostgreSQL 17** powered conversation storage
- Multi-provider support (OpenAI, Ollama, Local models)
- Advanced analytics and performance tracking
- Full-text search across AI interactions
- Model performance comparison and optimization

### 🔧 **Core ML Integration**
- PyTorch to Core ML model conversion
- Apple Silicon optimization (M1/M2/M3)
- Performance benchmarking
- MLX model ecosystem integration

### 📁 **Smart Automation**
- Intelligent file organization with wxPython GUI
- Web scraping with PyQt5 interface
- Document processing and tagging
- Automated workflow integration

## 🚀 **Quick Start**

### **Prerequisites**
- **macOS** with Apple Silicon (M3 recommended)
- **Python 3.9+**
- **PostgreSQL 17** (optional but recommended)
- **Xcode Command Line Tools**

### **Installation**

```bash
# Clone the repository
git clone https://github.com/yourusername/neuralforge.git
cd neuralforge

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Optional: Setup PostgreSQL for AI memory
python3 scripts/setup_postgresql.py

# Launch the toolkit
python3 src/neuralforge/launcher.py
```

### **One-Line Setup**
```bash
curl -sSL https://raw.githubusercontent.com/yourusername/neuralforge/main/scripts/quick_start.sh | bash
```

## 📖 **Usage**

### **Interactive Launcher**
```bash
python3 src/neuralforge/launcher.py
```

The launcher provides access to all tools:

```
🧠 NeuralForge - AI & Automation Toolkit
🎯 Optimized for Apple Silicon (M3) Macs
🔧 PostgreSQL 17 + Neural Engine + Core ML

🛠️  Available Tools:
1. 🧠 Neural Engine Monitor    # Real-time ANE performance
2. 📁 File Organizer          # Smart file management  
3. 🔧 Core ML Integration     # Model conversion & optimization
4. 💾 AI Memory System        # PostgreSQL-powered memory
5. 🌐 Web Scraper            # Intelligent data extraction
6. 🧪 Run All Tests          # Comprehensive testing
7. 📊 Project Status         # System health check
```

### **AI Memory System Usage**

```python
from src.ai.memory_buffer import ConfigurableMemoryBuffer

# Initialize AI memory system
memory = ConfigurableMemoryBuffer()

# Store AI interactions
memory.add_memory_entry(
    agent_name="GPT-4",
    task="Market analysis for Q4 2024",
    response="Identified 3 key growth sectors...",
    success_rating=5,
    model_used="gpt-4-turbo",
    tokens_used=450
)

# Query past interactions  
results = memory.query_memory("market analysis")
stats = memory.get_memory_stats()

# Performance analytics
performance = memory.get_model_performance("gpt-4")
```

### **Neural Engine Monitoring**

```python
from src.core.neural_check import NeuralEngineMonitor

# Start real-time monitoring
monitor = NeuralEngineMonitor()
monitor.start_monitoring()  # Displays live dashboard
```

## 📁 **Project Structure**

```
NeuralForge/
├── 📦 src/                        # Source code
│   ├── neuralforge/              # Main package
│   │   └── launcher.py           # Main application launcher
│   ├── core/                     # Core system tools
│   │   ├── neural_check.py       # Neural Engine monitoring
│   │   ├── coreml.py            # Core ML integration
│   │   └── folder_organizer.py  # File management GUI
│   ├── ai/                       # AI & ML components  
│   │   ├── memory_buffer.py      # PostgreSQL memory system
│   │   └── document_tagger.py    # Document processing
│   ├── web/                      # Web automation tools
│   │   └── gui_scraper.py       # PyQt5 web scraper
│   └── integration/              # System integration
│       └── system_integration.py # Cross-project integration
├── 🧪 tests/                     # Comprehensive test suite
│   ├── test_neural_check.py     # Neural Engine tests
│   └── test_memory_buffer.py    # Memory system tests
├── 📚 docs/                      # Documentation
│   ├── api/                     # API documentation
│   ├── guides/                  # User guides
│   └── examples/                # Usage examples
├── 🔧 scripts/                   # Setup & utility scripts
│   ├── setup_postgresql.py     # Database initialization
│   ├── n8n_workflows.json      # n8n automation workflows
│   ├── node_red_flows.json     # Node-RED flows
│   └── raycast_commands.json   # Raycast integration
├── ⚙️  config/                   # Configuration files
│   └── memory_config.json      # AI memory settings
├── 🚀 .github/                   # GitHub workflows and templates
│   ├── workflows/              # CI/CD workflows
│   └── ISSUE_TEMPLATE/         # Issue templates
├── 📦 assets/                    # Static assets
│   ├── images/                 # Screenshots and diagrams
│   └── icons/                  # Application icons
├── 📋 requirements.txt          # Python dependencies
├── ⚙️  pyproject.toml           # Modern Python configuration
├── 🔧 setup.py                  # Package setup
├── 📄 LICENSE                   # MIT License
├── 🛡️  SECURITY.md              # Security policy
├── 🤝 CONTRIBUTING.md           # Contribution guidelines
└── 📄 README.md                # This file
```

## 🛠️ **Configuration**

### **AI Memory Configuration** (`config/memory_config.json`)

```json
{
  "provider": "postgresql",
  "postgresql": {
    "enabled": true,
    "host": "localhost", 
    "port": 5432,
    "database": "ai_memory",
    "user": "your_username",
    "auto_create_db": true
  },
  "local": {
    "enabled": true,
    "models_path": "/Volumes/MICRO/models"
  }
}
```

### **Environment Variables**

```bash
export NEURALFORGE_ENV=production
export POSTGRES_PASSWORD=your_secure_password
export OPENAI_API_KEY=your_openai_key  # Optional
export OLLAMA_HOST=http://localhost:11434  # Optional
```

## 📊 **Performance & Analytics**

NeuralForge includes comprehensive performance tracking:

- **Neural Engine Utilization** - Real-time ANE performance metrics
- **Model Performance Analytics** - Success rates, token usage, response times
- **Memory System Statistics** - Query performance, storage efficiency
- **System Resource Monitoring** - CPU, GPU, memory usage

## 🧪 **Testing**

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run specific test module
python3 -m pytest tests/test_neural_check.py -v

# Run with coverage
python3 -m pytest tests/ --cov=src --cov-report=html
```

## 🔧 **Development**

### **Setting Up Development Environment**

```bash
# Clone and setup
git clone https://github.com/yourusername/neuralforge.git
cd neuralforge

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run linting
black . && flake8 . && mypy .
```

### **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following our [style guide](CONTRIBUTING.md)
4. Add tests for new functionality
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 🔒 **Security**

- Secure PostgreSQL connections with proper authentication
- Environment-based configuration management
- No hardcoded credentials in source code
- Regular dependency updates and security scanning

See [SECURITY.md](SECURITY.md) for our security policy.

## 📈 **Roadmap**

### **v1.1.0 - Enhanced Integration**
- [ ] n8n/Node-RED workflow integration
- [ ] Advanced MLX model optimization
- [ ] Multi-agent coordination system

### **v1.2.0 - Enterprise Features**
- [ ] User management and access control
- [ ] Advanced analytics dashboard
- [ ] API endpoint for external integrations

### **v2.0.0 - Cloud Integration**
- [ ] Cloud deployment options
- [ ] Distributed AI memory system
- [ ] Real-time collaboration features

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 **Support**

- **Issues**: [GitHub Issues](https://github.com/yourusername/neuralforge/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/neuralforge/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/neuralforge/wiki)

## 🌟 **Acknowledgments**

- Apple Silicon optimization techniques
- PostgreSQL community for database excellence
- Rich library for beautiful terminal interfaces
- MLX ecosystem for Apple Silicon ML

---

<div align="center">

**Built with ❤️ for Apple Silicon and AI automation**

[Documentation](https://github.com/yourusername/neuralforge/wiki) • [Examples](docs/examples/) • [API Reference](docs/api/)

</div>