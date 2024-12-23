# Contributing Guide

Thank you for considering contributing to the Password Strength Analyzer project. This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the Repository
2. Clone your fork locally
3. Set up development environment
4. Create a feature branch

## Development Process

### Setting Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install development dependencies
pip install -r requirements-dev.txt
```

### Making Changes

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following our code style guidelines

3. Run tests:
```bash
pytest tests/
```

4. Run security checks:
```bash
bandit -r src/
```

### Pull Request Process

1. Update documentation
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Submit pull request

## Code Review Process

Pull requests are reviewed for:
- Code quality
- Test coverage
- Security considerations
- Documentation completeness

## Security Guidelines

- Follow secure coding practices
- Report security issues privately
- Review SECURITY.md
- Run security scans

## Testing Guidelines

1. Write tests for new features
2. Maintain test coverage
3. Include edge cases
4. Document test purposes

## Documentation

Update documentation for:
- New features
- Changed functionality
- API modifications
- Security considerations