# NeuralForge Development Guidelines

## Code Standards
- Follow PEP 8 style guidelines
- Use type hints for all functions
- Include Google-style docstrings
- Maximum line length: 88 characters
- Use Black for code formatting

## Apple Silicon Optimization
- ALWAYS prioritize Apple Silicon M3 optimizations first
- Use MLX for mathematical operations when available
- Leverage 16-core Neural Engine (18 TOPS) for AI tasks
- Optimize for 16GB unified memory and 10-core GPU
- Test MLX integration before falling back to numpy

## Testing Requirements
- Write tests for all new functionality
- Aim for >80% code coverage
- Use descriptive test names
- Include both unit and integration tests
- Test Apple Silicon specific features

## Error Handling
- Include comprehensive error handling
- Use Rich for beautiful error messages
- Log all operations with appropriate levels
- Provide clear error messages and recovery suggestions
- Never over-complicate: maintain stability first

## Documentation Standards
- Update README.md for user-facing changes
- Add examples for new features
- Include API documentation
- Use Markdown for all documentation
- Keep documentation up-to-date

## Git Workflow
- Use feature branches for new features
- Write descriptive commit messages
- Create pull requests for code review
- Ensure all tests pass before merging
- Update documentation with changes
