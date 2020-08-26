

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = Celsius_to_Fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit_input = float(input("Fahrenheit: "))
            celsius_conversion = Fahrenheit_to_Celsius(fahrenheit_input)
            print("Result: {:.2f} C".format(celsius_conversion))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def Celsius_to_Fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def Fahrenheit_to_Celsius(fahrenheit_input):
    celsius_conversion = 5 / 9 * (fahrenheit_input - 32)
    return celsius_conversion
main()

"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

