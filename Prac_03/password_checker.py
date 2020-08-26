

NAME_LENGTH = 4


def main():
    password = get_password()
    asterik_count(password)

def get_password():
    Name_Input = str(input("Word?:"))
    while len(Name_Input) < NAME_LENGTH:
        print("Invalid")
        Name_Input = str(input("Word?:"))
    return Name_Input

def asterik_count(password):
    Word_Count = len(password)
    for i in range(Word_Count):
        print("*", end="")


main()

