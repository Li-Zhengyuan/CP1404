NAME_TO_CODE = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "AntiqueWhite2": "#ffefdb",
    "Deep Peach": "#ffcba4"
}

name = input("Enter a name: ").upper()
while name != "":
    try:
        print(NAME_TO_CODE[name])
    except KeyError:
        print("Not a valid key.")
    name = input("Enter a name: ").upper()