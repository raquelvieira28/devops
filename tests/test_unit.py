import unittest
from src.my_module import my_function

class TestMyFunction(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(my_function(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
