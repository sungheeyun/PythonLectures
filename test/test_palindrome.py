import unittest

from list.palindrome import is_palindrome_1, is_palindrome_2


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_1(self):
        self.assertTrue(is_palindrome_1('aba'))
        self.assertFalse(is_palindrome_1('abaa'))

    def test_is_palindrome_2(self):
        self.assertTrue(is_palindrome_2('aba'))
        self.assertFalse(is_palindrome_2('abaa'))


if __name__ == '__main__':
    unittest.main()
