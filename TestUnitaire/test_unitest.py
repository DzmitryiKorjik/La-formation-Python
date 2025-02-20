from unittest import TestCase, main

from main import add

class TestCalculatrice(TestCase):
    def test_add_with_two_numbers(self):
        self.assertEqual(add(5, 10), 15)

    def test_add_with_two_letters(self):
        self.assertEqual(add("a", "b"), "ab")

    def test_add_with_two_booleans(self):
        self.assertEqual(add(True, False), 0)
        self.assertEqual(add(False, True), 1)
        self.assertEqual(add(True, True), 2)

    def test_add_with_none(self):
        self.assertEqual(add(None, None), 2)

if __name__ == '__main__':
    main()