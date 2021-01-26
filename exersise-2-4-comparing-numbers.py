import math
import sys
import time
import random

first = float(input("please input your first number for comparastion"))
time.sleep(3)
second = float(input("please input your second number for comparastion"))
time.sleep(3)
if (first) > (second):
    print((first,"is greater thean",second)) 
elif (second) > (first):
    print(second,"is greater than",first)
elif (first) == (second):
    print((first,"is equal to ",second))
else:
    print("error")
    sys.exit
