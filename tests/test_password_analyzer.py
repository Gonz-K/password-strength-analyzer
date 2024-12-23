# tests/test_password_analyzer.py

import pytest
from src.password_analyzer import PasswordAnalyzer

class TestPasswordAnalyzer:
    """Test suite for PasswordAnalyzer class"""
    
    @pytest.fixture
    def analyzer(self):
        """Provide analyzer instance for each test"""
        return PasswordAnalyzer()

    def test_input_validation(self, analyzer):
        """Test input validation security controls"""
        # Test empty password
        with pytest.raises(ValueError):
            analyzer.analyze_password("")
            
        # Test non-string input
        with pytest.raises(ValueError):
            analyzer.analyze_password(None)

    def test_pattern_detection(self, analyzer):
        """Test weak pattern detection"""
        # Test sequential pattern
        result = analyzer.analyze_password("abc123")
        assert result['patterns']['has_patterns']
        assert 'sequential' in result['patterns']['patterns_found']
        
        # Test repeated characters
        result = analyzer.analyze_password("aaa123")
        assert result['patterns']['has_patterns']
        assert 'repeated' in result['patterns']['patterns_found']
        
        # Test strong password
        result = analyzer.analyze_password("Str0ng!P@ss")
        assert not result['patterns']['has_patterns']
        assert len(result['patterns']['patterns_found']) == 0

    def test_complexity_check(self, analyzer):
        """Test character composition checks"""
        result = analyzer.analyze_password("Abcd123!@#")
        assert result['complexity']['has_uppercase']
        assert result['complexity']['has_lowercase']
        assert result['complexity']['has_numbers']
        assert result['complexity']['has_special']

    def test_score_calculation(self, analyzer):
        """Test password scoring"""
        # Test weak password
        weak = analyzer.analyze_password("weak")
        assert weak['score'] < 0.5
        
        # Test strong password
        strong = analyzer.analyze_password("Str0ng!P@ssw0rd")
        assert strong['score'] > 0.8

    def test_feedback_generation(self, analyzer):
        """Test feedback messages"""
        result = analyzer.analyze_password("weak")
        assert isinstance(result['feedback'], list)
        assert any("characters" in msg for msg in result['feedback'])