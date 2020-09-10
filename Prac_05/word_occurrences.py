Text_Input = str(input("Text: "))
Text_Dict = {}
Parts_of_Input = Text_Input.split()
print(Parts_of_Input)
for part in Parts_of_Input:
    Word_Count = Text_Dict.get(part, 0)
