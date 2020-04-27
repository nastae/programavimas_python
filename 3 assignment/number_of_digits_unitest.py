import unittest

def number_of_digits(s):
    return sum(c.isdigit() for c in s)

# Parašykite funkcijai X unittest'us
class Test(unittest.TestCase):

    def test_only_digits(self):
        s = "123456789"
        self.assertEqual(number_of_digits(s), 9)

    def test_only_letters(self):
        s = "abcdef"
        self.assertEqual(number_of_digits(s), 0)

    def test_digits_between_letters(self):
        s = "asd123asd123asd"
        self.assertEqual(number_of_digits(s), 6)

    def test_letters_between_digits(self):
        s = "123asd123asd123"
        self.assertEqual(number_of_digits(s), 9)

    def test_neither_letter_or_digit(self):
        s = ",./;';'[]`"
        self.assertEqual(number_of_digits(s), 0)

if __name__ == '__main__':
    unittest.main()
