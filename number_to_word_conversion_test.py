
import unittest
import number_to_word_conversion

class test_number_to_word(unittest.TestCase):

    def test_decimal(self):
        self.assertEqual(number_to_word_conversion.number_to_word(1191212.234),'Rs. eleven Lakh ninety one thousand two hundred and twelve 234/100 only')

    def test_range(self):
        self.assertEqual(number_to_word_conversion.number_to_word(11912121.234),
                         'number out of range')

    def test_integer(self):
        self.assertEqual(number_to_word_conversion.number_to_word(1191212), 'Rs. eleven Lakh ninety one thousand two hundred and twelve only')

    def test_format(self):
        self.assertEqual(number_to_word_conversion.number_to_word("sfddsfsdf"), 'string must be number')

    def test_two_digit_number(self):
        self.assertEqual(number_to_word_conversion.number_to_word(99),'Rs. ninety nine only')

    def test_one_digit_number(self):
        self.assertEqual(number_to_word_conversion.number_to_word(9),'Rs. nine only')

    def test_three_digit_number(self):
        self.assertEqual(number_to_word_conversion.number_to_word(999),'Rs. nine hundred and ninety nine only')

    def test_three_digit__hundred_only_number(self):
        self.assertEqual(number_to_word_conversion.number_to_word(900),'Rs. nine hundred only')

if __name__ == '__main__':
    unittest.main()
