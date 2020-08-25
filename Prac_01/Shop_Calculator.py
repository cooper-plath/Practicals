
Total_Cost = 0
List_Amount = int(input("How many items?: "))
while List_Amount <= 0:
    print("Invalid amount of items")
    List_Amount = int(input("How many items?: "))
for i in range(List_Amount):
    Item_Cost = float(input("Price of Item?:"))
    Total_Cost += Item_Cost
if Total_Cost >= 100:
    Total_Price = Total_Cost - (Total_Cost * 0.1)
    print(f"Total Price for {List_Amount} items is ${Total_Price:.2f}")
else:
    print(f"Total Price for {List_Amount} items is ${Total_Cost:.2f}")


