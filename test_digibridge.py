# test_digibridge.py
"""
Tests for DigiBridge module.
"""

import unittest
from digibridge import DigiBridge

class TestDigiBridge(unittest.TestCase):
    """Test cases for DigiBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigiBridge()
        self.assertIsInstance(instance, DigiBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigiBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
