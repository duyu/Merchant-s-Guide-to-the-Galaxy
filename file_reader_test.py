#!/usr/bin/env python
#coding=utf-8
#
# Merchant's Guide to the Galaxy
#  unittest for file_reader.read_file class
#  run: python ***_test.py -v
#    
#

import unittest

from file_reader import read_file

class TestReadFile(unittest.TestCase):
    ref_words = [   "glob is I",
                    "prok is V",
                    "pish is X",
                    "tegj is L"]
    price_msgs = [    "glob glob Silver is 34 Credits",
                        "glob prok Gold is 57800 Credits",
                        "pish pish Iron is 3910 Credits"]
    questions = [   "how much is pish tegj glob glob ?",
                    "how many Credits is glob prok Silver ?",
                    "how many Credits is glob prok Gold ?",
                    "how many Credits is glob prok Iron ?",
                    "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?"]

    info={'ref_words':ref_words,'price_msgs':price_msgs,'questions':questions, 'error_msgs':[]}

    def test_read_file(self):
        for key, value in read_file('input.txt').items():
            self.assertEqual(value, self.info[key])


if __name__ == '__main__':
    unittest.main()
