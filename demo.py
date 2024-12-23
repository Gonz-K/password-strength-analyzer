"""
Password Strength Analyzer Demonstration Script
Shows real-world examples of password analysis with detailed feedback.
"""

from password_analyzer import PasswordAnalyzer
import time


def run_demonstration():
    # Initialize our analyzer
    analyzer = PasswordAnalyzer()
    
    print("\n===== Password Strength Analyzer Demonstration =====\n")
    
    # We'll test a variety of passwords to demonstrate different scenarios
    test_cases = [
        {
            "password": "password123",
            "description": "Common weak password"
        },
        {
            "password": "SecureP@ssw0rd123!",
            "description": "Strong password with mixed characters"
        },
        {
            "password": "abcdef123456",
            "description": "Sequential pattern password"
        },
        {
            "password": "Admin2024!",
            "description": "Moderate strength with common word"
        }
    ]
    
    for case in test_cases:
        print(f"\nTesting: {case['description']}")
        print(f"Password: {case['password']}")
        print("-" * 50)
        
        # Analyze the password
        result = analyzer.analyze_password(case['password'])
        
        # Display comprehensive results
        print(f"\nStrength Score: {result['score']:.1%}")
        print(f"Length: {result['length']} characters")
        
        print("\nComplexity Analysis:")
        for check, passed in result['complexity'].items():
            status = "✓" if passed else "✗"
            print(f"  {status} {check.replace('has_', '').capitalize()}")
        
        if result['patterns']['patterns_found']:
            print("\nDetected Patterns:")
            for pattern in result['patterns']['patterns_found']:
                print(f"  ! {pattern.capitalize()} pattern found")
        
        if result['feedback']:
            print("\nImprovement Suggestions:")
            for suggestion in result['feedback']:
                print(f"  → {suggestion}")
        
        print("\n" + "="*50)
        time.sleep(1)  # Pause between analyses for readability

    print("\n\n===== Demonstration Complete =====\n")

    if __name__ == "__main__":
        run_demonstration()
        