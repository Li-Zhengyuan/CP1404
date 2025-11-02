NAME_TO_CODE = {
    "ABSOLUTE ZERO": "#0048ba",
    "ACID GREEN": "#b0bf1a",
    "ALICEBLUE": "#f0f8ff",
    "ALIZARIN CRIMSON: "#e32636",
    "AMARANTH": "#e52b50",
    "AMBER": "#ffbf00",
    "AMETHYST": "#9966cc",
    "ANTIQUEWHITE": "#faebd7",
    "BLACK": "#000000",
    "Deep Peach": "#ffcba4"
}

name = input("Enter a name: ").upper()
while name != "":
    try:
        print(f"{name} is {NAME_TO_CODE[name]}")
    except KeyError:
        print("Not a valid name.")
    name = input("Enter a name: ").upper()