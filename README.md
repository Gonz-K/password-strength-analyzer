w# Password Strength Analyzer

A Python-based tool that analyzes password strength according to NIST SP 800-63B and OWASP guidelines. Developed as part of the Security Automation class final project, this tool showcases the application of modern security practices, automated analysis techniques, and DevSecOps principles.

## Project Overview

The Password Strength Analyzer is designed to evaluate the robustness of passwords against common attack vectors and best practice standards. It incorporates a variety of checks, including:

- Minimum length requirements per NIST guidelines (8 characters)
- Character complexity analysis (uppercase, lowercase, numbers, special characters)
- Detection of common patterns (keyboard sequences, repeated characters)
- Verification against databases of known weak passwords
- Compliance validation against NIST SP 800-63B requirements
- Implementation of OWASP password security recommendations

The tool provides real-time feedback and specific suggestions for improving password strength, empowering users to make informed decisions about their password choices.

## Development Journey

The development of this project was an immersive learning experience that demanded the application of concepts from across the Security Automation curriculum. 

One of the key challenges faced was scoping the feature set appropriately given the time constraints. The vast landscape of password security techniques presented a constant temptation to expand the project's ambitions, leading to several restarts as new features were considered. Ultimately, the looming deadline necessitated a focused approach, prioritizing core functionality that would best demonstrate an understanding of the critical course concepts.

Throughout the process, a variety of AI-powered tools were leveraged to enhance the learning journey and project outcomes:

- **ChatGPT** was used for initial project ideation and decomposition, helping to break down the overarching goal into manageable tasks and milestones.
- **GitHub Copilot** served as a constant companion during the coding phase, offering intelligent suggestions, assisting with code review and formatting, and providing explanations for encountered errors. 
- **Claude** played a critical role in project planning and task prioritization. Its ability to analyze proposed features and architectures was invaluable in steering the project towards a viable MVP within the given constraints. Claude's aptitude for breaking down complex problems into step-by-step solutions was a guiding light in moments of conceptual impasse.
- **Notion** acted as a centralized knowledge base, housing research notes, failed repository attempts, and evolving project documentation.

However, not all challenges were purely technical. The project demanded a level of time management and self-regulation that proved formative. The allure of perfection and the drive to incorporate just one more feature led to periods of overwork and frustration. Learning to pace oneself, to take strategic breaks, and to accept the constraints of a deadline were lessons hard-won. 

## Security Implementation

In line with DevSecOps principles, security was treated as a first-class citizen throughout the development lifecycle:

- The codebase was regularly scanned using **Bandit**, a static code analysis tool, to identify potential security vulnerabilities. The scan results were integrated into the CI/CD pipeline to ensure continuous security validation.
- A robust suite of unit tests was developed using the **pytest** framework, covering all critical paths and edge cases. These tests were automatically run on each code change via a **GitHub Actions** workflow.
- All external inputs were carefully sanitized and validated to prevent potential injection attacks. 
- Error handling was implemented thoughtfully to avoid leaking sensitive information.

## Lessons Learned

This project served as a capstone to the Security Automation course, solidifying the understanding of key concepts and highlighting areas for continued growth. Key takeaways include:

- The importance of thorough planning and documentation cannot be overstated. Well-defined requirements and architectural decisions early on can prevent significant headaches later.
- Time management is a skill unto itself. Ambitious projects need to be tempered with realistic expectations and a willingness to compromise when necessary.
- Security is a mindset, not a checklist. It needs to be woven into every stage of development, from initial design through to deployment and maintenance.
- Collaboration, whether with human peers or AI tools, is a powerful multiplier. Knowing when and how to seek guidance and leverage external expertise is a critical skill.

In the end, while the final product may not have achieved every envisioned bell and whistle, it stands as a testament to the growth and learning that occurred throughout the Security Automation course. The challenges faced, mistakes made, and lessons learned will serve as invaluable guideposts in future endeavors.

## Future Enhancements

While the current iteration of the Password Strength Analyzer fulfills its core mission, there are numerous avenues for potential enhancement, including:

- Integration of AI-based password cracking defense techniques
- Generation of language-agnostic secure password suggestions
- Development of a user-friendly web interface for easier interaction
- Expansion of the password database to include more known weak passwords

One planned feature that didn't make it into the final version was the calculation of password entropy using Shannon's entropy formula. This measure of password unpredictability could have added another dimension to the strength evaluation. However, due to time constraints, it was decided to prioritize other critical functionalities. Implementing Shannon's entropy calculation remains an exciting opportunity for future development.

These features, while out of scope for the current academic project, present exciting opportunities for continued development and learning in the realm of password security.

## Setup and Installation

1. Clone the repository:

   ```
   git clone https://github.com/Gonz-K/password-strength-analyzer.git
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   source venv/bin/activate  # On Unix/MacOS
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

```python
# Import the PasswordAnalyzer class from the password_analyzer module 
from password_analyzer import PasswordAnalyzer

# Create an instance of the PasswordAnalyzer
analyzer = PasswordAnalyzer()

# Analyze a password
result = analyzer.analyze_password("YourPasswordHere")

# Get detailed feedback on the password's strength
print(result.get_detailed_feedback())
```

## Running Tests

Execute the test suite:

```
pytest tests/
```

Run the security scan:

```
bandit -r . -f json -o security_scan_results.json
```

## Acknowledgements

This project would not have been possible without the generous support and guidance provided by:

- Professor Simpson and the Security Automation course team
- The open-source community, particularly the maintainers and contributors of the various tools and libraries used
- The AI research community, whose work on language models and code assistants like ChatGPT, Claude, and GitHub Copilot is truly transformative

A special thanks to the developers of Python, pytest, Bandit, and the countless other shoulders upon which this project stands.

## Conclusion

The Password Strength Analyzer project has been a testament to the power of security automation and the potential of AI in enhancing cybersecurity practices. By leveraging cutting-edge tools and techniques, this project has demonstrated how we can create more robust, user-friendly systems that promote safer online behaviors.

Moreover, the project has underscored the importance of continuous learning and adaptation in the rapidly evolving field of cybersecurity. As new threats emerge and technologies advance, it's critical that we, as security professionals, remain committed to expanding our knowledge and refining our skills.

In the end, the greatest lesson of this project may be that security is a journey, not a destination. There will always be new challenges to confront and new heights to reach. But with a mindset of curiosity, collaboration, and resilience, we can continue to push the boundaries of what's possible and create a safer digital world for all.

## License

This project is developed solely for academic purposes as part of the Security Automation course at National University. It is not licensed for reuse or distribution. All rights are reserved by the author.
