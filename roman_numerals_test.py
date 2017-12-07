#!/usr/bin/env python
#coding=utf-8
#
# Merchant's Guide to the Galaxy
#  unittest for roman_numerals.RomanNumerals class
#  run: python ***_test.py -v
#    
#

import unittest

from roman_numerals import RomanNumerals

class TestRomanNumerals(unittest.TestCase):
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'))

    illegal_romans = ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII', 'CMCM', 
                    'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV', 'IIMXCC', 'VX', 
                    'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC')

    illegal_romans_symbols = ('AAA', 'xax', 'ccb')
    illegal_romans_repeat = ('MMMM', 'DD', 'MMMCMMMMCM')
    illegal_romans_subtract = ('CMC', 'DCM', 'LD')

    def test_check_roman_basic_symbols(self):
        for integer, numeral in self.known_values:
            self.assertEqual(RomanNumerals.check_roman_basic_symbols(numeral), True)
        for numeral in self.illegal_romans_symbols:
            self.assertEqual(RomanNumerals.check_roman_basic_symbols(numeral), False)

    def test_check_roman_repeat_rules(self):
        for integer, numeral in self.known_values:
            self.assertEqual(RomanNumerals.check_roman_repeat_rules(numeral), True)
        for numeral in self.illegal_romans_repeat:
            self.assertEqual(RomanNumerals.check_roman_repeat_rules(numeral), False)

    def test_check_roman_subtract_rules(self):
        for integer, numeral in self.known_values:
            self.assertEqual(RomanNumerals.check_roman_subtract_rules(numeral), True)
        for numeral in self.illegal_romans_subtract:
            self.assertEqual(RomanNumerals.check_roman_subtract_rules(numeral), False)

    def test_check_roman(self):
        for integer, numeral in self.known_values:
            self.assertEqual(RomanNumerals.check_roman(numeral), True)
        for numeral in self.illegal_romans:
            self.assertEqual(RomanNumerals.check_roman(numeral), False)
            

    def test_to_arabic(self):
        for integer, numeral in self.known_values:
            self.assertEqual(RomanNumerals.to_arabic(numeral), integer)


if __name__ == '__main__':
    unittest.main()
