import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < 0:
    print("It cannot less than 0")
    number_of_quick_picks = int(input("How many quick picks? "))