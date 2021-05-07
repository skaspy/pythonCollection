import random

i = 0
active = True
number_to_guess = random.randint(0, 100)

while active:
    i = i +1
    print() # improves the layout
    print(i)
    user_input = int(input("Please enter a number: "))

    if (user_input == number_to_guess):
        print("You won! Congratulation!")
        active = False
        break
    elif user_input > number_to_guess:
        print("Your number is too big.")
    else:
        print("Your number is too small.")

    if (i == 7):
        print("Too bad. You lost!")
        print("The secret number was " + str(number_to_guess))
        active = False

print("The End. Wanna play again? ;-)")
