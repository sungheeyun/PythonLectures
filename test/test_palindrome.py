import unittest

from list.palindrome import is_palindrome_1, is_palindrome_2


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_1(self):
        self.assertTrue(is_palindrome_1('abcdcba'))
        self.assertTrue(is_palindrome_1('abcddcba'))
        self.assertFalse(is_palindrome_1('acddcba'))

    def test_is_palindrome_2(self):
        self.assertTrue(is_palindrome_2('abcdcba'))
        self.assertTrue(is_palindrome_2('abcddcba'))
        self.assertFalse(is_palindrome_2('acddcba'))


if __name__ == '__main__':
    unittest.main()
