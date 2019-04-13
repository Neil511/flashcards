#!/usr/local/bin/python3
"""
    Commands to support:
    1. Question (q) - give a random question from the list
    2. List (l) - takes in an optional argument,
        searches for a Q/A pair and prints it
"""
import random

QUESTIONS = []
correct_answers = 0

with open('questions.txt', 'r') as file:
    contents = file.readlines()
    for line in contents:
        question, answer = line.strip('\n').split(", ")
        QUESTIONS.append((question, answer))
NUMBER_OF_QUESTIONS = len(QUESTIONS)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def correct(expected, actual):
    expected = expected.split(" ")
    actual = actual.split(" ")

    length = len(expected)
    count = 0

    for i in actual:
        if i in expected:
            expected.remove(i)
            count += 1
    # dank semantic analysis
    return float(count) / length >= .70


def question():
    global correct_answers
    if len(QUESTIONS) == 0:
        print("NO QUESTIONS LEFT.")
        print("Score: {}".format(float(correct_answers / NUMBER_OF_QUESTIONS)))
        return
    pair = random.choice(QUESTIONS)
    QUESTIONS.remove(pair)
    answer = input(pair[0] + '\n')
    if correct(pair[1], answer):
        print(bcolors.OKGREEN + "Correct!\n" + bcolors.ENDC)
        correct_answers += 1
    else:
        print(bcolors.FAIL + "Incorect." + bcolors.ENDC)
        print(bcolors.BOLD + pair[1] + '\n' + bcolors.ENDC)


def find(topic=None):
    if topic is None:
        pair = random.choice(QUESTIONS)
        print(pair)
        return

    print(bcolors.OKBLUE + "Searching for {}\n".format(topic) + bcolors.ENDC)
    for pair in QUESTIONS:
        if topic in pair[0] or topic in pair[1]:
            print(pair)


while True:
    cmd = input()
    if cmd is None or cmd == "exit":
        print("Exiting...")
        break
    elif cmd == "q":
        question()
    elif cmd[0] == "l":
        if len(cmd) > 1:
            find(cmd.split(" ")[1])
        else:
            find()
