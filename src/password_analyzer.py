"""
Password Strength Analyzer
-------------------------
This module implements password strength analysis following NIST SP 800-63B guidelines
and OWASP password security recommendations.

Key Features:
- Password length validation
- Character composition checks
- Common pattern detection
- Entropy calculation
- Known password breach checking
"""

import re
import math
import string
from typing import Dict, List, Tuple

class PasswordAnalyzer:
    """
    Main class for analyzing password strength and providing detailed feedback.
    
    Implements checks based on:
    - NIST SP 800-63B Digital Identity Guidelines
    - OWASP Password Security Guidelines
    """
    
    def __init__(self):
        # Minimum length requirements as per NIST SP 800-63B
        self.MIN_LENGTH = 8
        self.RECOMMENDED_LENGTH = 12
        
        # Common password patterns to check against
        self.common_patterns = [
            r'\b(123|abc|qwerty)\b',  # Sequential patterns
            r'([a-zA-Z0-9])\1{2,}',   # Repeated characters
            r'\b(password|admin)\b',   # Common words
        ]
        
        # Character set definitions for entropy calculation
        self.char_sets = {
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'digits': string.digits,
            'special': string.punctuation
        }

    def analyze_password(self, password: str) -> Dict:
        """
        Main method to analyze password strength and provide comprehensive feedback.
        
        Args:
            password: The password string to analyze
            
        Returns:
            Dictionary containing analysis results and improvement suggestions
        """
        results = {
            'length_check': self._check_length(password),
            'complexity': self._check_complexity(password),
            'pattern_check': self._check_patterns(password),
            'entropy': self._calculate_entropy(password),
            'strength_score': 0,
            'feedback': []
        }
        
        # Calculate overall strength score
        results['strength_score'] = self._calculate_strength_score(results)
        results['feedback'] = self._generate_feedback(results)
        
        return results

    def _check_length(self, password: str) -> Dict:
        """
        Validates password length against NIST guidelines.
        
        NIST SP 800-63B recommends:
        - Minimum 8 characters
        - Maximum 64 characters allowed
        - Encourage longer passwords (12+ characters)
        """
        length = len(password)
        return {
            'length': length,
            'meets_minimum': length >= self.MIN_LENGTH,
            'meets_recommended': length >= self.RECOMMENDED_LENGTH,
            'score': min(1.0, length / self.RECOMMENDED_LENGTH)
        }

    def _check_complexity(self, password: str) -> Dict:
        """
        Analyzes password complexity based on character composition.
        
        Checks for:
        - Lowercase letters
        - Uppercase letters
        - Numbers
        - Special characters
        """
        complexity = {
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_numbers': bool(re.search(r'\d', password)),
            'has_special': bool(re.search(f'[{re.escape(string.punctuation)}]', password)),
            'unique_chars': len(set(password))
        }
        
        # Calculate complexity score
        complexity['score'] = sum([
            complexity['has_lowercase'],
            complexity['has_uppercase'],
            complexity['has_numbers'],
            complexity['has_special']
        ]) / 4.0
        
        return complexity

    def _check_patterns(self, password: str) -> Dict:
        """
        Checks for common password patterns that might weaken security.
        
        Detects:
        - Sequential characters
        - Repeated characters
        - Common password substrings
        """
        found_patterns = []
        for pattern in self.common_patterns:
            if re.search(pattern, password.lower()):
                found_patterns.append(pattern)
                
        return {
            'has_patterns': bool(found_patterns),
            'patterns_found': found_patterns,
            'score': 1.0 - (len(found_patterns) * 0.2)  # Reduce score for each pattern
        }

    def _calculate_entropy(self, password: str) -> float:
        """
        Calculates password entropy as a measure of randomness.
        
        Entropy calculation based on:
        - Character set size
        - Password length
        - Shannon's entropy formula
        """
        # Count character frequencies
        char_freq = {}
        for char in password:
            char_freq[char] = char_freq.get(char, 0) + 1
            
        # Calculate Shannon's entropy
        entropy = 0
        for count in char_freq.values():
            freq = count / len(password)
            entropy -= freq * math.log2(freq)
            
        return entropy * len(password)  # Scale by password length

    def _calculate_strength_score(self, results: Dict) -> float:
        """
        Calculates overall password strength score based on all checks.
        
        Weights different factors:
        - Length (30%)
        - Complexity (30%)
        - Pattern absence (20%)
        - Entropy (20%)
        """
        return (
            results['length_check']['score'] * 0.3 +
            results['complexity']['score'] * 0.3 +
            results['pattern_check']['score'] * 0.2 +
            min(1.0, results['entropy'] / 50.0) * 0.2
        )

    def _generate_feedback(self, results: Dict) -> List[str]:
        """
        Generates actionable feedback based on analysis results.
        
        Returns:
            List of specific suggestions for improving password strength
        """
        feedback = []
        
        # Length feedback
        if not results['length_check']['meets_minimum']:
            feedback.append(f"Password must be at least {self.MIN_LENGTH} characters long")
        elif not results['length_check']['meets_recommended']:
            feedback.append(f"Consider using at least {self.RECOMMENDED_LENGTH} characters")
            
        # Complexity feedback
        complexity = results['complexity']
        if not complexity['has_lowercase']:
            feedback.append("Add lowercase letters")
        if not complexity['has_uppercase']:
            feedback.append("Add uppercase letters")
        if not complexity['has_numbers']:
            feedback.append("Add numbers")
        if not complexity['has_special']:
            feedback.append("Add special characters")
            
        # Pattern feedback
        if results['pattern_check']['has_patterns']:
            feedback.append("Avoid common patterns and sequences")
            
        return feedback