#!/usr/bin/env python 
import random

lottery = random.randint(0, 99)

guess = eval(input("Enter your lottery pick (two digits): "))

lottery_1 = lottery // 10
lottery_2 = lottery % 10

guess_1 = guess // 10
guess_2 = guess % 10 

print("The lottery number is", lottery)

if guess == lottery:
    print("Exact match: you win $10,000")
elif (guess_2 == lottery_1 and \
      guess_1 == lottery_2):
    print("Match all digits: you win $3,000")
elif (guess_1 == lottery_1 
    or guess_1 == lottery_2 
    or guess_2 == lottery_1 
    or guess_2 == lottery_2): 
    print("Match one digit: you win $1,1000")
else:
    print("Sorry, no match")
