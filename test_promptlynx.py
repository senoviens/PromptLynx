# test_promptlynx.py
"""
Tests for PromptLynx module.
"""

import unittest
from promptlynx import PromptLynx

class TestPromptLynx(unittest.TestCase):
    """Test cases for PromptLynx class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PromptLynx()
        self.assertIsInstance(instance, PromptLynx)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PromptLynx()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
