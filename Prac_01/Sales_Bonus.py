"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
Under_Bonus = 0.10
Over_Bonus = 0.15

Get_Sales_Input = int(input("How much did you make in Sales?: "))
while Get_Sales_Input <= 0:
    print("Invalid")
    Get_Sales_Input = int(input("How much did you make in Sales?: "))
else:
    if Get_Sales_Input < 1000:
        print(Get_Sales_Input * Under_Bonus)
    else:
        print(Get_Sales_Input * Over_Bonus)

