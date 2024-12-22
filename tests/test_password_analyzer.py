"""
Test suite for Password Strength Analyzer
---------------------------------------
Comprehensive tests for password analysis functionality following testing best practices:
- Unit tests for each component
- Edge cases
- Known weak passwords
- Strong password validation
"""

import pytest
from src.password_analyzer import PasswordAnalyzer

class TestPasswordAnalyzer:
    """Test suite for PasswordAnalyzer class"""
    
    @pytest.fixture
    def analyzer(self):
        """
        Pytest fixture to provide a fresh PasswordAnalyzer instance for each test.
        """
        return PasswordAnalyzer()

    def test_password_length(self, analyzer):
        """
        Test password length validation against NIST requirements.
        Tests both minimum and recommended lengths.
        """
        # Test short password
        short_result = analyzer._check_length("short")
        assert not short_result['meets_minimum']
        assert not short_result['meets_recommended']
        
        # Test minimum length password
        min_result = analyzer._check_length("minimum8!")
        assert min_result['meets_minimum']
        assert not min_result['meets_recommended']
        
        # Test recommended length password
        recommended_result = analyzer._check_length("recommendedLength12!")
        assert recommended_result['meets_minimum']
        assert recommended_result['meets_recommended']

    def test_complexity_requirements(self, analyzer):
        """
        Test password complexity analysis.
        Checks for presence of different character types.
        """
        # Test simple password
        simple_result = analyzer._check_complexity("simple123")
        assert simple_result['has_lowercase']
        assert not simple_result['has_uppercase']
        assert simple_result['has_numbers']
        assert not simple_result['has_special']
        
        # Test complex password
        complex_result = analyzer._check_complexity("Complex123!")
        assert all([
            complex_result['has_lowercase'],
            complex_result['has_uppercase'],
            complex_result['has_numbers'],
            complex_result['has_special']
        ])

    def test_pattern_detection(self, analyzer):
        """
        Test detection of common patterns and weak password characteristics.
        """
        # Test sequential patterns
        seq_result = analyzer._check_patterns("abc123")
        assert seq_result['has_patterns']
        
        # Test repeated characters
        repeat_result = analyzer._check_patterns("aaa123")
        assert repeat_result['has_patterns']
        
        # Test common words
        common_result = analyzer._check_patterns("password123")
        assert common_result['has_patterns']
        
        # Test strong password
        strong_result = analyzer._check_patterns("StrongP@ssw0rd!")
        assert not strong_result['has_patterns']

    def test_entropy_calculation(self, analyzer):
        """
        Test entropy calculation for different password types.
        """
        # Test low entropy
        low_entropy = analyzer._calculate_entropy("aaaaa")
        
        # Test medium entropy
        medium_entropy = analyzer._calculate_entropy("Password123")
        
        # Test high entropy
        high_entropy = analyzer._calculate_entropy("K7#mP9$xL2&nQ4")
        
        assert low_entropy < medium_entropy < high_entropy

    def test_overall_strength_score(self, analyzer):
        """
        Test overall password strength scoring.
        """
        # Test weak password
        weak_result = analyzer.analyze_password("weak")
        assert weak_result['strength_score'] < 0.4
        
        # Test medium password
        medium_result = analyzer.analyze_password("Medium123")
        assert 0.4 <= medium_result['strength_score'] < 0.7
        
        # Test strong password
        strong_result = analyzer.analyze_password("Str0ng#P@ssw0rd!")
        assert strong_result['strength_score'] >= 0.7

    def test_feedback_generation(self, analyzer):
        """
        Test feedback generation for different password strengths.
        """
        # Test feedback for short password
        short_result = analyzer.analyze_password("short")
        assert any("length" in feedback.lower() for feedback in short_result['feedback'])
        
        # Test feedback for simple password
        simple_result = analyzer.analyze_password("simplepassword")
        assert any("uppercase" in feedback.lower() for feedback in simple_result['feedback'])
        
        # Test feedback for strong password
        strong_result = analyzer.analyze_password("Str0ng#P@ssw0rd!")
        assert len(strong_result['feedback']) == 0