#!/usr/bin/env python
#coding=utf-8
#
# Merchant's Guide to the Galaxy
#  utils part for handling currencies and translations
#

import os


# A roman numerals class for dealing with the roman numerals
# 
class RomanNumerals:
    CURRENCY = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self):
        pass

    @staticmethod
    def check_roman_basic_symbols(roman_string):
        """
        * input: string
        * output: boolean, whether all the symbols in this string are legal
        """
        all_legal_symbols = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

        # basic check for symbols
        if not roman_string or not all(c in all_legal_symbols for c in roman_string):
            return False
        else:
            return True

    @staticmethod
    def check_roman_repeat_rules(roman_string):
        """
        * input: roman_string
        * output: boolean, whether this string fit with the repeat rules.

        The symbols "I", "X", "C", and "M" can be repeated three times in succession, 
        but no more. (They may appear four times if the third and fourth are separated 
        by a smaller value, such as XXXIX.) "D", "L", and "V" can never be repeated.
        """
        can_never_be_repeated = ('D', 'L', 'V')
        can_be_repeated = ('I', 'X', 'C', 'M')
        MAX_REPEAT_COUNT_I = 3
        MAX_REPEAT_COUNT_X = 4 # this can only be repeated for 4 times while it's 'XXXIX'
        MAX_REPEAT_COUNT_C = 4 # this can only be repeated for 4 times while it's 'CCCXC'
        MAX_REPEAT_COUNT_M = 4 # this can only be repeated for 4 times while it's 'MMMCM'

        for item in can_never_be_repeated:
            if roman_string.count(item) > 1:
                return False
        if roman_string.count('I') > MAX_REPEAT_COUNT_I:
            return False
        if roman_string.count('X') > MAX_REPEAT_COUNT_X \
            or (roman_string.count('X') == 4 and 'XXXIX' not in roman_string):
            return False
        if roman_string.count('C') > MAX_REPEAT_COUNT_C \
            or (roman_string.count('C') == 4 and 'CCCXC' not in roman_string):
            return False
        if roman_string.count('M') > MAX_REPEAT_COUNT_M \
            or (roman_string.count('M') == 4 and 'MMMCM' not in roman_string):
            return False
        
        return True

    @staticmethod
    def check_roman_subtract_rules(roman_string):
        """
        * input: roman_string
        * output: boolean, whether this string fit with the subtract rules.

        "I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and 
        "C" only. "C" can be subtracted from "D" and "M" only. "V", "L", and "D" can never 
        be subtracted. Only one small-value symbol may be subtracted from any large-value symbol.
        A number written in [16]Arabic numerals can be broken into digits. For example, 1903 is 
        composed of 1, 9, 0, and 3. To write the Roman numeral, each of the non-zero digits should 
        be treated separately. Inthe above example, 1,000 = M, 900 = CM, and 3 = III. Therefore, 1903 = MCMIII.

        each roman should not subtract anything:
          1. if the next abric plus it is not less than itself: i.e. CMC
          2. current arabic should not be larger than the last one: i.e. DCM
        """
        can_be_subtracted_from = { 'C': {'D', 'M'}, 'I': {'V', 'X'}, 'X': {'L', 'C'} }
        can_never_be_subtracted = ('V', 'L', 'D')

        last_subtract_roman = 0 # last roman number that was subtracted from
        last_arabic_value = 9999 # the last generated arabic value, 9999 means the biggest and never reachable value
        current_arabic_value = 0
        i = 0
        while i < len(roman_string):
            # the last symbol does not need to check with the subtract rules
            if (i < len(roman_string) - 1) and RomanNumerals.CURRENCY[roman_string[i]] < RomanNumerals.CURRENCY[roman_string[i+1]]:
                # if the after symbol is bigger than the before one, meaning there's a subtract:
                if roman_string[i] in can_never_be_subtracted:
                    return False
                if roman_string[i+1] not in can_be_subtracted_from[roman_string[i]]:
                    return False

                current_arabic_value = RomanNumerals.CURRENCY[roman_string[i+1]] - RomanNumerals.CURRENCY[roman_string[i]]
                if current_arabic_value > last_arabic_value:
                    return False
                if last_subtract_roman != 0 and current_arabic_value + last_arabic_value >= last_subtract_roman:
                    return False
                else:
                    last_subtract_roman = RomanNumerals.CURRENCY[roman_string[i+1]]
                    last_arabic_value = current_arabic_value
                    i = i + 2 # skip the subtract one
            # if it's the last symbol or it's not followed by a bigger symbol
            else:
                current_arabic_value = RomanNumerals.CURRENCY[roman_string[i]]
                if current_arabic_value > last_arabic_value:
                    return False
                if last_subtract_roman != 0 and current_arabic_value + last_arabic_value >= last_subtract_roman:
                    return False
                else:
                    last_arabic_value = current_arabic_value
                    last_subtract_roman = 0
                    i = i + 1
            
        return True

    @staticmethod
    def check_roman(roman_string):
        """
        * input: string, a string you wanna check if it's roman numerals
        * output: boolean, whether it's a legal roman numerals or not
        """
        return RomanNumerals.check_roman_basic_symbols(roman_string) \
            and RomanNumerals.check_roman_repeat_rules(roman_string) \
            and RomanNumerals.check_roman_subtract_rules(roman_string)


    @staticmethod
    def to_arabic(symbols):
        """
        Convert roman numerals to arabic numbers:
        Numbers are formed by combining symbols together and adding the values. 
        For example, MMVI is 1000 + 1000 + 5 + 1 = 2006. Generally, symbols are 
        placed in order of value, starting with the largest values. When smaller 
        values precede larger values, the smaller values are subtracted from the 
        larger values, and the result is added to the total. For example 
        MCMXLIV = 1000 + (1000 − 100) + (50 − 10) + (5 − 1) = 1944.
        """
        if not RomanNumerals.check_roman(symbols):
            return None
        numbers = [ RomanNumerals.CURRENCY[s] for s in symbols ]

        for i in range(len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                numbers[i] = -numbers[i]
        
        return sum(numbers)