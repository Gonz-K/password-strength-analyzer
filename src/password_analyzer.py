# src/password_analyzer.py

import re
import string
from typing import Dict

class PasswordAnalyzer:
    """Password strength analyzer implementing NIST guidelines"""
    
    def __init__(self):
        self.MIN_LENGTH = 8
        self.MAX_LENGTH = 64
        self._setup_patterns()
    
    def _setup_patterns(self):
        """Initialize regex patterns for password analysis"""
        self.patterns = {
            'sequential': re.compile(r'(abc|123|qwerty)', re.IGNORECASE),
            'repeated': re.compile(r'(.)\1{2,}'),
            'common': re.compile(r'(password|admin)', re.IGNORECASE)
        }
    
    def analyze_password(self, password: str) -> Dict:
        """
        Analyze password strength and provide feedback
        
        Args:
            password: Password string to analyze
            
        Raises:
            ValueError: If password is empty or invalid
            
        Returns:
            Dictionary containing analysis results
        """
        # Input validation
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        if not password:
            raise ValueError("Password cannot be empty")
            
        results = {
            'length': len(password),
            'meets_length': len(password) >= self.MIN_LENGTH,
            'complexity': self._check_complexity(password),
            'patterns': self._check_patterns(password)
        }
        
        results['score'] = self._calculate_score(results)
        results['feedback'] = self._generate_feedback(results)
        
        return results
    
    def _check_complexity(self, password: str) -> Dict:
        """Check password character composition"""
        return {
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_numbers': bool(re.search(r'\d', password)),
            'has_special': bool(re.search(f'[{re.escape(string.punctuation)}]', password))
        }
    
    def _check_patterns(self, password: str) -> Dict:
        """Check for weak patterns in password"""
        found_patterns = []
        
        for name, pattern in self.patterns.items():
            if pattern.search(password):
                found_patterns.append(name)
        
        return {
            'has_patterns': bool(found_patterns),
            'patterns_found': found_patterns
        }
    
    def _calculate_score(self, results: Dict) -> float:
        """Calculate overall password strength score"""
        score = 0.0
        
        # Length score (40%)
        if results['meets_length']:
            score += 0.4
            
        # Complexity score (40%)
        complexity = results['complexity']
        if complexity['has_lowercase']: score += 0.1
        if complexity['has_uppercase']: score += 0.1
        if complexity['has_numbers']: score += 0.1
        if complexity['has_special']: score += 0.1
            
        # Pattern penalty (20%)
        if not results['patterns']['has_patterns']:
            score += 0.2
            
        return min(1.0, score)
    
    def _generate_feedback(self, results: Dict) -> list:
        """Generate improvement suggestions"""
        feedback = []
        
        if not results['meets_length']:
            feedback.append(f"Password must be at least {self.MIN_LENGTH} characters")
            
        complexity = results['complexity']
        if not complexity['has_lowercase']:
            feedback.append("Add lowercase letters")
        if not complexity['has_uppercase']:
            feedback.append("Add uppercase letters")
        if not complexity['has_numbers']:
            feedback.append("Add numbers")
        if not complexity['has_special']:
            feedback.append("Add special characters")
            
        if results['patterns']['has_patterns']:
            feedback.append("Avoid common patterns and sequences")
            
        return feedback