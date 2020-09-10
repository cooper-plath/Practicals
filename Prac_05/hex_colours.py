COLOUR_CHART = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "BlanchedAlmond": "#ffebcd", "Brown": "#a52a2a",
                "CadetBlue": "#98f5ff", "Chocolate": "chocolate",
                "coral": "#ff7f50", "CornflowerBlue": "#6495ed",
                "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400"}

Colour_Input = str(input("Colour: "))

#
Valid = False
while not Valid:
    if Colour_Input in COLOUR_CHART:
        print(COLOUR_CHART.get(Colour_Input))
        Valid = True
    else:
        print("Invalid")
        Colour_Input = str(input("Colour: "))