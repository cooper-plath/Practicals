# TOTAL_NUMBERS = 5
# Numbers_List = []
# for i in range(TOTAL_NUMBERS):
#     Numbers_Input = int(input("Number: "))
#     Numbers_List.append(Numbers_Input)
# # print(Numbers_List)
# print("The first number is {}".format(Numbers_List[0]))
# print("The last number is {}".format(Numbers_List[-1]))
# print(f"The smallest number is {min(Numbers_List)}")
# print(f"The largest number is {max(Numbers_List)}")
# print(f"The average of the number is {sum(Numbers_List)/TOTAL_NUMBERS}")



usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
User_Input = str(input("Username?: "))

if User_Input in usernames:
    print("Access granted")
else:
    print("Access denied")