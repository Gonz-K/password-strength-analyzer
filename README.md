# Password Strength Analyzer

A Python-based tool that analyzes password strength according to NIST SP 800-63B and OWASP guidelines. Developed as part of my Security Automation class final project, this tool implements modern security practices through automated analysis and DevSecOps principles.

## Features

Password strength evaluation incorporating:
- Length requirements (NIST minimum 8 characters)
- Character complexity analysis (uppercase, lowercase, numbers, special characters)
- Pattern detection (keyboard patterns, repeated sequences)
- Common password database verification
- Password entropy calculation using Shannon entropy
- Real-time feedback with specific improvement suggestions
- NIST SP 800-63B compliance validation
- OWASP password security best practices implementation

## Security Implementation

- Automated security scanning with Bandit
- Continuous Integration/Continuous Deployment (CI/CD) pipeline
- Regular automated testing through GitHub Actions
- Input sanitization and validation
- Secure error handling

## Setup and Installation

Clone the repository:
```sh
git clone https://github.com/Gonz-K/password-strength-analyzer.git
```

Create and activate virtual environment:
```sh
python -m venv venv
source venv/Scripts/activate # Windows
source venv/bin/activate # Unix/MacOS
```

Install Dependencies:
```sh
pip install -r requirements.txt
```

## Usage

```python
from password_analyzer import PasswordAnalyzer

# Initialize analyzer
analyzer = PasswordAnalyzer()

# Analyze a password
result = analyzer.analyze_password("YourPasswordHere")

# Get detailed feedback
print(result.get_detailed_feedback())
```

## Testing and Security Validation

Run the test suite:
```sh
pytest tests/
```

Execute security scan:
```sh
bandit -r . -f json -o security_scan_results.json
```
## Testing

This project maintains comprehensive test coverage:
- 98% overall code coverage
- Automated testing via pytest
- Full coverage report available in docs/testing-guide
  
## Development Guidelines

- Follow PEP 8 style guidelines
- Run tests before committing changes
- Verify security scan results
- Update documentation as needed

## Project Status and Usage Rights

This is an academic project developed as part of the Security Automation course curriculum. The project utilizes various AI-assisted development tools and resources, all of which were:
- Approved for use within course guidelines
- Properly documented in the acknowledgments section
- Used as learning and development aids
- Implemented with full transparency and academic integrity

All rights are reserved, and this project is not licensed for reuse or distribution. The code and documentation serve as a demonstration of academic learning and implementation of security concepts, particularly in the areas of password strength analysis, NIST compliance, and DevSecOps practices.

The project's primary purpose is educational, demonstrating understanding of:
- Security automation principles
- Password strength evaluation techniques
- Modern development practices including AI-assisted coding
- DevSecOps implementation
- Documentation and attribution standards

For questions about this project or its academic context, please contact Professor Simpson CYB333 Security Automation class.

## Acknowledgments

This project was developed with various resources and assistance that were all approved for use in this academic project:

Guidelines and Technical Standards:
- NIST Special Publication 800-63B Digital Identity Guidelines - Used as primary reference for password security requirements and validation criteria
- OWASP Password Security Guidelines and Best Practices - Referenced for implementing secure password evaluation methods
- Python PEP 8 Style Guidelines - Followed for code formatting and style consistency

Development Assistance and Tools:
- GitHub Copilot - An AI programming assistant used for code completion and suggestions during development, as permitted by course guidelines
- Claude (Anthropic) - Utilized for:
  - Project planning and organization
  - Code review and revision assistance
  - Documentation structure guidance
  - General development feedback
- Notion - Employed as a database management system for:
  - Storing and organizing project requirements
  - Tracking development progress
  - Managing project documentation
  - Maintaining reference materials

GitHub Resources:
- GitHub Documentation - Referenced for:
  - Project structure best practices
  - Repository setup guidance
  - Implementation of CI/CD workflows
  - Troubleshooting common issues
- DevSecOps Documentation and Best Practices - Consulted for:
  - Security pipeline implementation
  - Automated testing integration
  - Continuous security scanning setup
  - Secure development workflow design

Academic Support:
- Professor Simpson - for course guidance and project requirements
- Security Automation Course Materials - Provided foundation for implementing security concepts

Note: All AI tools and external resources were used in accordance with course guidelines and academic integrity policies. Their use was focused on learning enhancement and development assistance rather than direct solution provision.