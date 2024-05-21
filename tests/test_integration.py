import unittest
from src.my_module import my_function, another_function

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        result = my_function(2, 3)
        self.assertEqual(another_function(result), 10)

if __name__ == '__main__':
    unittest.main()
