from unittest import TestCase
import MorseConverter


class Test(TestCase):
    def test_verify_contents_are_valid_true(self):
        self.assertTrue(MorseConverter.verify_contents_are_valid("2"))

    def test_verify_contents_are_valid_false(self):
        self.assertFalse(MorseConverter.verify_contents_are_valid("?"))


