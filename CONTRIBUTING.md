# Contributing to NeuralForge

Thank you for your interest in contributing to NeuralForge! This document provides guidelines and information for contributors.

## 🎯 **How to Contribute**

### **Reporting Issues**
- Use the [GitHub Issues](https://github.com/yourusername/neuralforge/issues) page
- Search existing issues before creating new ones
- Use the provided issue templates
- Include system information (macOS version, Python version, etc.)

### **Suggesting Features**
- Use the "Feature Request" issue template
- Provide clear use cases and examples
- Consider Apple Silicon optimization opportunities

### **Code Contributions**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 🛠️ **Development Setup**

### **Prerequisites**
- macOS with Apple Silicon (M1/M2/M3)
- Python 3.9+
- Xcode Command Line Tools
- Git

### **Local Development**
```bash
# Clone your fork
git clone https://github.com/yourusername/neuralforge.git
cd neuralforge

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run tests
pytest
```

## 📝 **Code Style Guidelines**

### **Python Code Style**
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [mypy](https://mypy.readthedocs.io/) for type checking
- Maximum line length: 88 characters

### **Documentation**
- Use Google-style docstrings
- Include type hints for all functions
- Update README.md for user-facing changes
- Add examples for new features

### **Testing**
- Write tests for all new functionality
- Aim for >80% code coverage
- Use descriptive test names
- Include both unit and integration tests

## 🧪 **Testing Guidelines**

### **Running Tests**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_neural_check.py

# Run with verbose output
pytest -v
```

### **Test Categories**
- **Unit Tests**: Test individual functions/methods
- **Integration Tests**: Test component interactions
- **System Tests**: Test end-to-end workflows

## 🔧 **Apple Silicon Optimization**

### **Performance Considerations**
- Optimize for Neural Engine usage
- Use Core ML when appropriate
- Consider memory constraints (16GB unified memory)
- Test on different Apple Silicon chips

### **MLX Integration**
- Prefer MLX models for Apple Silicon
- Use quantized models for memory efficiency
- Benchmark performance improvements

## 📦 **Package Structure**

### **Adding New Modules**
```
src/neuralforge/
├── __init__.py
├── launcher.py          # Main entry point
└── new_module/
    ├── __init__.py
    ├── core.py          # Main functionality
    └── utils.py         # Helper functions
```

### **Module Guidelines**
- Keep modules focused and cohesive
- Use clear, descriptive names
- Include comprehensive error handling
- Add logging for debugging

## 🚀 **Release Process**

### **Version Numbering**
- Follow [Semantic Versioning](https://semver.org/)
- Update version in `pyproject.toml`
- Update `CHANGELOG.md`

### **Release Checklist**
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version bumped
- [ ] Changelog updated
- [ ] Tagged release

## 🐛 **Bug Reports**

### **Information to Include**
- macOS version and hardware
- Python version
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs
- Screenshots if applicable

### **Bug Report Template**
```markdown
**Bug Description**
Brief description of the bug

**Steps to Reproduce**
1. Step one
2. Step two
3. Step three

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**System Information**
- macOS: [version]
- Hardware: [M1/M2/M3]
- Python: [version]
- NeuralForge: [version]

**Additional Context**
Any other relevant information
```

## 💡 **Feature Requests**

### **Information to Include**
- Clear description of the feature
- Use cases and examples
- Potential implementation approach
- Apple Silicon optimization opportunities

### **Feature Request Template**
```markdown
**Feature Description**
Brief description of the feature

**Use Cases**
- Use case 1
- Use case 2
- Use case 3

**Proposed Implementation**
High-level approach

**Apple Silicon Optimization**
How this could be optimized for Apple Silicon

**Additional Context**
Any other relevant information
```

## 📚 **Documentation**

### **Documentation Types**
- **API Documentation**: Auto-generated from docstrings
- **User Guides**: Step-by-step tutorials
- **Examples**: Code examples and use cases
- **Architecture**: System design and components

### **Writing Guidelines**
- Use clear, concise language
- Include code examples
- Add screenshots for GUI components
- Keep documentation up-to-date

## 🔒 **Security**

### **Security Guidelines**
- Never commit secrets or API keys
- Use environment variables for sensitive data
- Follow secure coding practices
- Report security issues privately

### **Reporting Security Issues**
- Email: security@giovannini.us
- Use "SECURITY" in subject line
- Include detailed description
- Wait for response before public disclosure

## 🤝 **Community Guidelines**

### **Code of Conduct**
- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the [Contributor Covenant](https://www.contributor-covenant.org/)

### **Communication**
- Use GitHub Discussions for questions
- Be patient with responses
- Provide clear, detailed information
- Help others when possible

## 📞 **Getting Help**

### **Resources**
- [GitHub Discussions](https://github.com/yourusername/neuralforge/discussions)
- [Documentation](https://github.com/yourusername/neuralforge/wiki)
- [Issues](https://github.com/yourusername/neuralforge/issues)

### **Contact**
- Email: eduardo@giovannini.us
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 **Recognition**

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to NeuralForge! 🧠✨