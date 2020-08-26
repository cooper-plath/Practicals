

NAME_LENGTH = 4


def get_password():
    Name_Input = str(input("Word?:"))
    Word_Count = len(Name_Input)
    while len(Name_Input) < NAME_LENGTH:
        print("Invalid")
        Name_Input = str(input("Word?:"))
        Word_Count = len(Name_Input)
    return Word_Count






def main(NAME_LENGTH):
    get_password()
    for i in range(Word_Count):
        print("*", end="")

main()

