#!/usr/bin/env python
#coding=utf-8
#
# Merchant's Guide to the Galaxy
#  unittest for merchant_robot.MerchantRobot class
#  run: python **_test.py -v
#    
#

import unittest

from merchant_robot import MerchantRobot


class TestMerchantRobot(unittest.TestCase):
    ref_words = [   "glob is I",
                    "prok is V",
                    "pish is X",
                    "tegj is L"]
    prices_words = [    "glob glob Silver is 34 Credits",
                        "glob prok Gold is 57800 Credits",
                        "pish pish Iron is 3910 Credits"]
    questions = [   "how much is pish tegj glob glob ?",
                    "how many Credits is glob prok Silver ?",
                    "how many Credits is glob prok Gold ?",
                    "how many Credits is glob prok Iron ?",
                    "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?"]
    answers = [ "pish tegj glob glob is 42",
                "glob prok Silver is 68 Credits",
                "glob prok Gold is 57800 Credits",
                "glob prok Iron is 782 Credits",
                "I have no idea what you are talking about"]
    
    DEFAULT_ANSWER = "I have no idea what you are talking about"

    def test__init_(self):
        with self.assertRaises(TypeError):
            test_robot = MerchantRobot()

        try:
            test_robot = MerchantRobot(self.DEFAULT_ANSWER)
        except:
            self.fail()

    def test_build_words_book(self):
        test_robot = MerchantRobot(self.DEFAULT_ANSWER)
        self.assertEqual(test_robot.build_words_book(self.ref_words), [])

    def test_build_prices_book(self):
        test_robot = MerchantRobot(self.DEFAULT_ANSWER)
        self.assertEqual(test_robot.build_prices_book(self.prices_words), [])

    def test_translate_ref_to_arabic(self):
        test_robot = MerchantRobot(self.DEFAULT_ANSWER)
        self.assertEqual(test_robot.build_words_book(self.ref_words), [])
        self.assertEqual(test_robot.translate_ref_to_arabic("glob prok".split()), 4)
        self.assertEqual(test_robot.translate_ref_to_arabic("pish tegj glob glob".split()), 42)

    def test_answer_questions(self):
        test_robot = MerchantRobot(self.DEFAULT_ANSWER)
        self.assertEqual(test_robot.build_words_book(self.ref_words), [])
        self.assertEqual(test_robot.build_prices_book(self.prices_words), [])
        self.assertEqual(test_robot.answer_questions(self.questions), self.answers)


if __name__ == '__main__':
    unittest.main()