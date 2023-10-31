#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = str(number)
last = number2[-1]
last = int(last)
if number < 0:
    last = -last
if last > 5:
    message = "greater than 5"
elif last == 0:
    message = "0"
elif last < 6:
    message = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, last, message))
