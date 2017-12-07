#!/usr/bin/env python
#coding=utf-8
#
# Merchant's Guide to the Galaxy
#  excutor for reading messages from file and output, both python2 and python3 supported
#  test: python main.py test.txt
#  exec: python main.py {input.txt}
#    
#
import sys
import os

from merchant_robot import MerchantRobot
from file_reader import read_file

DEFAULT_ANSWER = "I have no idea what you are talking about"

def learn_and_answer(input_file):
    info = read_file(input_file)
    error_msgs = info['error_msgs']
    
    if len(info['ref_words']) > 0:
        # init the robot with default answer
        robot = MerchantRobot(DEFAULT_ANSWER)

        # build the robot's ref words book
        result = robot.learn_knowledge(info['ref_words'], info['price_msgs'])
        if result:
            error_msgs.extend(result)

        # use to robot to answer questions
        result = robot.answer_questions(info['questions'])
        if result:
            print("\n".join(result))
        if error_msgs:
            print("\n".join(error_msgs))
    else:
        print("no ref words found")

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    if not os.path.isfile(input_file):
        print("Can't find the input file: " + input_file)
        exit(1)
    learn_and_answer(input_file)