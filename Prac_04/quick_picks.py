import random

Lowest_Number = 1
Highest_Number = 45



def main():

    User_Input = int(input("How many quick picks? "))
    for i in range(User_Input):
        for length in range(6):
            number = random.randint(Lowest_Number, Highest_Number)

            print(number)






main()

