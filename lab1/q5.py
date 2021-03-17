# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab1 Q5

from random import randint

quit = False

while(not quit):
    a = randint(-99,99)
    b = randint(-99,99)
    c = randint(-99,99)
    x = input("Does (" + str(a) + "x^2)+(" + str(b) + "x)+(" + str(c) + ") has real solution(s)? ")
    ans = "yes" if (b**2 - 4 * a * c >= 0) else "no"
    if (x.lower() != "quit"):
        print("Right!") if (x.lower() == ans) else print("Wrong!")
    else:
        quit = True
        print("Bye!")

    