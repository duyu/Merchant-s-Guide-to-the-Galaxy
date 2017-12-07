# The Roman Numerals Syntax and Transaction

## Roman Numerals Rules:

1. Basic Rule
only 7 symbols are allowed in a roman numeral: 
```
all_legal_chars = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
```
2. Repeat Rule
The symbols "I", "X", "C", and "M" can be repeated three times in succession, but no more. (They may appear four times if the third and fourth are separated by a smaller value, such as XXXIX.) "D", "L", and "V" can never be repeated.
```
can_never_be_repeated = ('D', 'L', 'V')
can_be_repeated = ('I', 'X', 'C', 'M')
```
3. Subtract Rule
"I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and "C" only. "C" can be subtracted from "D" and "M" only. "V", "L", and "D" can never be subtracted. Only one small-value symbol may be subtracted from any large-value symbol.
```
subtract_rules = { 'C': {'D', 'M'}, 'I': {'V', 'X'}, 'X': {'L', 'C'} }
can_never_be_subtracted = ('V', 'L', 'D')
```
4. Order Rule
A number written in [16]Arabic numerals can be broken into digits. For example, 1903 is composed of 1, 9, 0, and 3. To write the Roman numeral, each of the non-zero digits should be treated separately. Inthe above example, 1,000 = M, 900 = CM, and 3 = III. Therefore, 1903 = MCMIII.
```
# each roman should not subtract anything 
#  if the next abric plus it is not less than itself: i.e. CMC
# current arabic should not be larger than the last one: i.e. DCM
if current_arabic > last_arabic:
    return False
if last_subtract_roman != 0 and current_arabic + last_arabic >= last_subtract_roman:
    return False
```

## Roman Numerals to Arabic numbers
This is then much easier after we checked the legality of roman symbols:
```
CURRENCY = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
numbers = [ RomanNumerals.CURRENCY[s] for s in symbols ]

for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        numbers[i] = -numbers[i]
return sum(numbers)
```