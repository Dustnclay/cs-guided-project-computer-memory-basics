

def csRaindrops(number):
    water = ""
    if number % 3 == 0:
        water += "pling"

    if number % 5 == 0:
        water += "plang"

    if number % 7 == 0:
        water += "plong"

    if water == "":
        water = number

    print(water)


csRaindrops(28)
csRaindrops(30)
csRaindrops(34)