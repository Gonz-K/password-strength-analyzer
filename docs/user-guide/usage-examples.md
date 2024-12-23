# Usage Examples

This document provides practical examples of using the Password Strength Analyzer in various scenarios.

## Basic Usage

Analyze a single password:
```python
from password_analyzer import PasswordAnalyzer

analyzer = PasswordAnalyzer()
result = analyzer.analyze_password("MyP@ssw0rd123!")

print(f"Password Score: {result['score']:.1%}")
print("Feedback:", result['feedback'])
```

## Integration Examples

### Form Validation
```python
def validate_signup_form(username: str, password: str) -> dict:
    analyzer = PasswordAnalyzer()
    analysis = analyzer.analyze_password(password)
    
    return {
        'is_valid': analysis['score'] >= 0.7,
        'feedback': analysis['feedback'],
        'strength': analysis['score']
    }
```

### Batch Processing
```python
def analyze_password_list(passwords: list) -> dict:
    analyzer = PasswordAnalyzer()
    results = {}
    
    for password in passwords:
        results[password] = analyzer.analyze_password(password)
    
    return results
```

## Advanced Usage

### Custom Strength Requirements
```python
def meets_enterprise_requirements(password: str) -> bool:
    analyzer = PasswordAnalyzer()
    result = analyzer.analyze_password(password)
    
    return (
        result['score'] >= 0.8 and
        result['complexity']['has_special'] and
        result['length'] >= 12 and
        not result['patterns']['has_patterns']
    )
```

### Security Integration
```python
from password_analyzer import PasswordAnalyzer
from typing import Tuple

def secure_password_validation(password: str) -> Tuple[bool, list]:
    analyzer = PasswordAnalyzer()
    result = analyzer.analyze_password(password)
    
    security_checks = [
        result['score'] >= 0.7,
        not result['patterns']['has_patterns'],
        result['length'] >= 10,
        all(result['complexity'].values())
    ]
    
    return all(security_checks), result['feedback']
```

## Example Output

```python
# Example password analysis result
{
    'score': 0.85,
    'length': 14,
    'meets_length': True,
    'complexity': {
        'has_uppercase': True,
        'has_lowercase': True,
        'has_numbers': True,
        'has_special': True
    },
    'patterns': {
        'has_patterns': False,
        'patterns_found': []
    },
    'feedback': []
}