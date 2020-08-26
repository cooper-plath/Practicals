"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""




def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Enter score: "))
    Main_Score = User_Score(score)
    print(Main_Score)

def User_Score(score):

    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"

main()