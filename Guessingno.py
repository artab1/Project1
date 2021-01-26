import random

Highest_number = 10
guess = int(input("Please enter your lucky number from 1 to {}:".format(Highest_number)))
answer= random.randint(1,Highest_number)

if guess == answer:
    print("You are so lucky, you won the lottery")
elif guess > answer:
    print("please guess lower next time, Do you wanna play again")
    guess=int(input())
    if guess == answer:
            print("Finally, you made it")
    else:
            print("you lose")
elif guess < answer:
    print("please guess higher next time, Do you want to try again")
    guess=int(input())
    if guess == answer:
            print("Finally, you made it")
    else:
            print("you lose") 
