import os
import random
import math
import turtle
print("======= Random Number game =======================")
print("|                                                                                               |")
print("|                                                                                               |")
print("|                                                                                               |")
print("|                                                                                               |")
print("|                                                                                               |")
print("| Welcome To Random Number Game Please Type your name |")
print("================================================")
print(" ")
print(" ")
print(" ")
name = input(">")

print("============ Random Number game ==================================")
print("|                                                                                                                             |")
print("|                                                                                                                             |")
print("|                                                                                                                             |")
print("|                                                                                                                             |")
print("|                                                                                                                             |")
print("|     Hey", name," Whats the Lowest amount You want to be able to guess :             |")
print("===============================================================")
print(" ")
print(" ")
print(" ")

lower = int(input("> "))

os.system('cls')

print("======= Random Number game ==================================")
print("|                                                                                                                    |")
print("|                                                                                                                    |")
print("|                                                                                                                    |")
print("|                                                                                                                    |")
print("|                                                                                                                    |")
print("|     Sounds Good! The Highest amount You want to be able to guess?           |")
print("============================================================")
print(" ")
print(" ")
print(" ")
upper = int(input(">"))
x = random.randint(lower, upper)
os.system('cls')

print("======= Random Number game =======================")
print("|                                                                                               |")
print("|                                                                                               |")
print("|                                                                                               |")
print("|                                                                                               |")
print("|                                                                                               |")
print("ok", name,"\n\tYou've only got ",
       round(math.log(upper - lower + 1, 2)),
      " trys to guess the number!\n")
print("================================================")
print(" ")
print(" ")
print(" ")

count = 0
 
while count < math.log(upper - lower + 1, 2):
    count += 1
 

    guess = int(input(">"))
    if x == guess:
        os.system('cls')
        print("======= Random Number game =======================")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|     Good Game You won!, you won in",
              count, " Try's                          |")
        print(" Heres a Medal!                                                                       |")
        print("================================================")
        ws=turtle.Screen()
        geekyTurtle = turtle.Turtle()
        for i in range(5):
                geekyTurtle.forward(100)
                geekyTurtle.right(144)
        print(" ")
        print(" ")
        exit()
        break
    elif x > guess:
        os.system('cls')
        print("======= Random Number game =======================")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|     Your Guess Was to Small, Try again                                   |")
        print("================================================")
        print(" ")
        print(" ")
        print(" ")
    elif x < guess:
        os.system('cls')
    os.system('cls')
        print("======= Random Number game =======================")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|                                                                                               |")
        print("|     Your Guess Was to High, Try again                                   |")
        print("================================================")
        print(" ")
        print(" ")
        print(" ")

if count >= math.log(upper - lower + 1, 2):
    os.system('cls')
    print("======= Random Number game =======================")
    print("|                                                                                               |")
    print("|                                                                                               |")
    print("|                                                                                               |")
    print("|                                                                                               |")
    print("|    \nThe number is %d" % x,                                                    )
    print("|     You Tried Your Best... but you lost :(  good game", name,"      |")
    print("================================================")
    exit()

