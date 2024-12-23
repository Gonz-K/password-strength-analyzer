# Installation Guide

This guide walks you through the process of setting up the Password Strength Analyzer in your development environment.

## Prerequisites

Before installation, ensure you have:
- Python 3.8 or higher
- pip package manager
- Git (for version control)
- Virtual environment tool (recommended)

## Step-by-Step Installation

1. Clone the Repository
```bash
git clone https://github.com/Gonz-K/password-strength-analyzer.git
cd password-strength-analyzer
```

2. Create and Activate Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Verify Installation
```bash
# Run tests to ensure everything is working
pytest tests/

# Run the demonstration script
python demo.py
```

## Development Setup

For development work, install additional tools:
```bash
pip install -r requirements-dev.txt
```

This includes:
- pylint for code quality
- black for formatting
- bandit for security scanning

## Troubleshooting Installation

If you encounter issues during installation:

1. Check Python Version
```bash
python --version
```

2. Verify pip Installation
```bash
pip --version
```

3. Confirm Virtual Environment
```bash
# Should show virtual environment path
which python
```

## Next Steps

After installation:
1. Review the API documentation
2. Run the demonstration script
3. Explore the test suite
4. Check security guidelines