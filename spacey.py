def spacer(input):

    output = ""
    for i in input:
        output = output + i + " "
    return output
    
def deSpacer(input):
    if input is None:
        return
    
    output = ''
    for i in range(len(input)):
        if i % 2 == 0:
            output += input[i]
    return output