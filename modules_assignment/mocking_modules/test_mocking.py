import unittest
from unittest import mock
import math  # Importing the module that we will mock in the test

# Function that uses math.sqrt
def calculate_square_root(value):
    return math.sqrt(value)

class TestMathSqrtMocking(unittest.TestCase):
    @mock.patch('math.sqrt', return_value=100)  # Mocking math.sqrt
    def test_calculate_square_root(self, mock_sqrt):
        result = calculate_square_root(25)  # Normally, sqrt(25) is 5, but we mock it to return 100
        self.assertEqual(result, 100)  # Check if the mock return value is used
        mock_sqrt.assert_called_once_with(25)  # Ensure math.sqrt was called with the correct argument

if __name__ == '__main__':
    unittest.main()

#Explanation of the Code
#Function Definition:

#calculate_square_root(value) uses math.sqrt(value).
#Unit Test Class:

#We use unittest.TestCase to define a test case.
#Mocking math.sqrt:

#@mock.patch('math.sqrt', return_value=100) replaces math.sqrt with a mock that always returns 100.
#This ensures the function doesn't call the real math.sqrt() during testing.
#Assertions in the Test:

#self.assertEqual(result, 100): Verifies that the function returns 100 (mocked value).
#mock_sqrt.assert_called_once_with(25): Ensures math.sqrt(25) was actually called.