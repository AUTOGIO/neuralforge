# 🧠 NeuralForge Documentation

Welcome to the NeuralForge documentation! This is the main documentation site for the NeuralForge project.

## 🚀 Quick Start

```bash
# Install NeuralForge
pip install neuralforge

# Launch the toolkit
neuralforge
```

## 📚 Documentation Sections

### Core Features
- [Neural Engine Monitor](neural-engine-monitor.md) - Real-time Apple Neural Engine monitoring
- [AI Memory System](ai-memory-system.md) - PostgreSQL-powered conversation storage
- [Core ML Integration](core-ml-integration.md) - Model conversion and optimization
- [File Organizer](file-organizer.md) - Intelligent file management
- [Web Scraper](web-scraper.md) - Advanced web scraping tools
- [Document Tagger](document-tagger.md) - Document processing and tagging

### Development
- [API Reference](api/) - Complete API documentation
- [Contributing Guide](../CONTRIBUTING.md) - How to contribute
- [Security Policy](../SECURITY.md) - Security guidelines
- [Changelog](../CHANGELOG.md) - Version history

### Examples
- [Basic Usage](examples/basic-usage.md) - Getting started examples
- [Advanced Features](examples/advanced-features.md) - Advanced use cases
- [Integration Examples](examples/integrations.md) - System integration examples

## 🔧 Configuration

### Environment Variables
```bash
export NEURALFORGE_ENV=production
export POSTGRES_PASSWORD=your_secure_password
export OPENAI_API_KEY=your_openai_key  # Optional
export OLLAMA_HOST=http://localhost:11434  # Optional
```

### Configuration Files
- [Memory Configuration](config/memory-config.md) - AI memory system settings
- [Neural Engine Settings](config/neural-engine-config.md) - Monitoring configuration
- [Automation Workflows](config/automation-workflows.md) - n8n/Node-RED setup

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test module
pytest tests/test_neural_check.py -v
```

## 📊 Performance

NeuralForge is optimized for Apple Silicon and includes comprehensive performance tracking:

- **Neural Engine Utilization** - Real-time ANE performance metrics
- **Model Performance Analytics** - Success rates, token usage, response times
- **Memory System Statistics** - Query performance, storage efficiency
- **System Resource Monitoring** - CPU, GPU, memory usage

## 🤝 Support

- **Issues**: [GitHub Issues](https://github.com/AUTOGIO/neuralforge/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AUTOGIO/neuralforge/discussions)
- **Wiki**: [Project Wiki](https://github.com/AUTOGIO/neuralforge/wiki)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

**Built with ❤️ for Apple Silicon and AI automation**
