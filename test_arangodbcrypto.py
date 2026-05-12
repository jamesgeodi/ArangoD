# test_arangodbcrypto.py
"""
Tests for ArangoDBCrypto module.
"""

import unittest
from arangodbcrypto import ArangoDBCrypto

class TestArangoDBCrypto(unittest.TestCase):
    """Test cases for ArangoDBCrypto class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArangoDBCrypto()
        self.assertIsInstance(instance, ArangoDBCrypto)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArangoDBCrypto()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
