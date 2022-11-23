import random
import math
import modul1

a = True
while a:
    while True:
        while True:
            try:
                lower = int(input("Enter Lower bound:- "))
                upper = int(input("Enter Upper bound:- "))
                break
            except:
                print("Not a number")

        if upper - lower > 1:
            break
        else:
            print('Number difference must be at least 2')

    x = random.randint(lower, upper)
    print("\n\tYou've only ",
          round(math.log(upper - lower + 1, 2)),
          " chances to guess the integer!\n")
    count = 0


    # Class
    class calculate:
        while count < math.log(upper - lower + 1, 2):
            count += 1
            while True:
                try:
                    guess = int(input("Guess a number:- "))
                    break
                except:
                    print("Not a number")

            if x == guess:
                print("Congratulations you did it in ",
                      count, " try")
                correct = 1
                break
            elif x > guess:
                print("You guessed too small!")
                correct = 0
            elif x < guess:
                print("You Guessed too high!")
                correct = 0


    modul1.printer()
    modul1.IsItGood()

    while True:
        print('go again?')
        print('Y / N')
        answer = input()
        if answer.upper() == 'N':
            a = False
            break
        elif answer.upper() == 'Y':
            break
        else:
            print('invalid input')
