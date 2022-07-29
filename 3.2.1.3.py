#!/bin/python3
secret_number = 777
guess=0
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while guess!=secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess=int(input("What is your guess? "))

print("Well done, muggle! i guess you're free now.")
