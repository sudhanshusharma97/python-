import random
from random import randint
x = randint(0,20)

print("Guess the number")
print ("   ")
c = int(input())
print ("   ")
print ('the generated number is, ' + str(x))
print ("   ")
if c > x:
    print("   ")
    print(" and your number is too high " )
    print("   ")
elif c < x:
    print("   ")
    print(" and your number is too low " )
    print ("   ")
else:
    print(" and your the number is correct, Congratulations you've won the game")
    print("")
input()
