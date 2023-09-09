def abcIndex(i):
    i = i.lower()

    if i == "a":
        return 1
    elif i == "b":
        return 2
    elif i == "c":
        return 3
    elif i == "d":
        return 4
    elif i == "e":
        return 5
    elif i == "f":
        return 6
    elif i == "g":
        return 7
    elif i == "h":
        return 8
    elif i == "i":
        return 9
    elif i == "j":
        return 10
    elif i == "k":
        return 11
    elif i == "l":
        return 12
    elif i == "m":
        return 13
    elif i == "n":
        return 14
    elif i == "o":
        return 15
    elif i == "p":
        return 16
    elif i == "q":
        return 17
    elif i == "r":
        return 18
    elif i == "s":
        return 19
    elif i == "t":
        return 20
    elif i == "u":
        return 21
    elif i == "v":
        return 22
    elif i == "w":
        return 23
    elif i == "x":
        return 24
    elif i == "y":
        return 25
    elif i == "z":
        return 26
    else:
        return 0
def numIndex(i):
    if i == 0: return " "
    if i == 1: return "a"
    if i == 2: return "b"
    if i == 3: return "c"
    if i == 4: return "d"
    if i == 5: return "e"
    if i == 6: return "f"
    if i == 7: return "g"
    if i == 8: return "h"
    if i == 9: return "i"
    if i == 10: return "j"
    if i == 11: return "k"
    if i == 12: return "l"
    if i == 13: return "m"
    if i == 14: return "n"
    if i == 15: return "o"
    if i == 16: return "p"
    if i == 17: return "q"
    if i == 18: return "r"
    if i == 19: return "s"
    if i == 20: return "t"
    if i == 21: return "u"
    if i == 22: return "v"
    if i == 23: return "w"
    if i == 24: return "x"
    if i == 25: return "y"
    if i == 26: return "z"
def index(input):
    if type(input) == str:
        if len(input) > 1:
            output = []
            for i in input:
                output.append(int(abcIndex(i)))
            return output
        elif len(input) == 1:
            return abcIndex(input)
        return abcIndex(input)
    elif type(input) == int:
        return numIndex(input)
    elif type(input) == list:
        output = ""
        for i in input:
            output = output + numIndex(int(i))
        return output
def shift(input, shift):
    if type(input) == str:
        input = index(input)
        isString = True
    else: isString = False


    output = []
    for i in input:
        j = i + shift
        if j > 26:
            j -= 27
        elif j < 0:
            j += 27
        output.append(j)

    if isString:
        output = index(output)
    return output
