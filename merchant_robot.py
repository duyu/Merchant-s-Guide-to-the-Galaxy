# define a MerchantRobot
#   * it should be able to build a dictionary for languages and prices
#   * words_book: a dictionary for numerals' translation
#   * prices: a dictionary for recording goods' prices

from roman_numerals import RomanNumerals

class MerchantRobot:
    words_book = {}
    prices_book = {}

    default_answer = ""
    def __init__(self, default_answer):
        self.default_answer = default_answer

    def build_words_book(self, ref_words):
        # deal with ref_words: glob is I
        # return the error messages in ref_words
        error_msgs = []
        for item in ref_words:
            patterns = item.split(' ')
            if len(patterns) == 3 and patterns[1] == 'is':
                if patterns[0] not in self.words_book:
                    self.words_book.update({patterns[0]: patterns[2]})
                elif self.words_book[patterns[0]] != patterns[2]:
                    # word seems to be changed
                    print("update Word " + patterns[0] + " from " + self.words_book[patterns[0]]
                        + " to " + patterns[2])
                    self.words_book.update({patterns[0]: patterns[2]})
                else:
                    # the word is in book but it does not required updating
                    continue
            else:
                # bad pattern 
                error_msgs.append(item)
        return error_msgs
    
    def build_prices_book(self, prices_words):
        # deal with ref_words: glob glob Silver is 34 Credits
        # return the error_msgs in prices_words
        error_msgs = []
        for item in prices_words:
            patterns = item.split(' ')
            # find the position of good name and price
            try:
                good_pattern_price = int(patterns[-2])
            except ValueError:
                print("That's not an int:", patterns[-2])
                error_msgs.append(item)
            
            good_name = patterns[-4]
            
            amount_arabic = self.translate_ref_to_arabic(patterns[:-4])
            if amount_arabic:
                good_price = float(good_pattern_price)/amount_arabic
                if good_name not in self.prices_book:
                    self.prices_book.update({good_name: good_price})
                elif good_name in self.prices_book and self.prices_book[good_name] != good_price:
                    print("update price of " + good_name + " from " + self.prices_book[good_name]
                        + " to " + good_price)
                    self.prices_book.update({good_name: good_price})
                else:
                    # duplicated message
                    continue
            else:
                print('Error while updaing prices dict with:', good_name, amount_arabic)
                error_msgs.append(item)
        return error_msgs

    def translate_ref_to_arabic(self, ref_words_list):
        # convert amount pattern to abrabic
        roman_nums = []
        for item in ref_words_list:
            if item in self.words_book:
                roman_nums.append(self.words_book[item])
            else:
                print('Error amount pattern', item)
                return None
        
        return RomanNumerals.to_arabic(''.join(roman_nums))

    def learn_knowledge(self, ref_words, prices_msgs):
        error_msgs = []
        error_msgs.extend(self.build_words_book(ref_words))
        error_msgs.extend(self.build_prices_book(prices_msgs))
        return error_msgs

    def answer_questions(self, questions):
        # answer the questions
        answers = []
        for item in questions:
            # how much is pish tegj glob glob ?
            if 'how much is' in item:
                answer_num = self.translate_ref_to_arabic(item.split()[3:-1])
                answers.append(" ".join(item.split()[3:-1]) + ' is ' + str(answer_num))
            # how many Credits is glob prok Silver ?
            elif 'how many Credits' in item:
                good_name = item.split()[-2]
                good_amount = self.translate_ref_to_arabic(item.split()[4:-2])
                if good_amount is not None and good_name in self.prices_book:
                    good_price = int(good_amount * self.prices_book[good_name])
                    answers.append(" ".join(item.split()[4:-1]) + ' is ' + str(good_price) + ' Credits')
                else:
                    answers.append(self.default_answer + ": " + " ".join(item.split()[4:-1]))
            else:
                answers.append(self.default_answer)
        return answers