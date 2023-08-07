#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import markovify

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")




def spacer(input):
    output = ""
    for i in input:
        output = output + i + " "
    return output
    
def deSpacer(input):
    output = ''
    for i in range(len(input)):
        if i % 2 == 0:
            output += input[i]
    return output

# def sortFile(filename):
#     out = list()
#     with open (filename) as fin:
#         for line in fin:
#             out.append(line)
    
#     out.sort()
#     out2 = ""
#     for i in out:
#         out2 = out2 + i + """
# """
#         out = out2
#         return out
#     f = open(filename, "w")
#     f.write(out)

def removeDuplicates(dupList):
    noDupList = []
    for element in dupList:
            if element not in noDupList:
                noDupList.append(element)
    return noDupList

with open("corpus.txt") as f:
    text = f.read()

model = markovify.NewlineText(spacer(text), state_size = 3)
f.close()

out = ''
for i in range(10000):
    out = out + deSpacer(model.make_sentence(test_output = True, tries = 100, state_size =3)) + """
"""

f = open ("output.txt", "w")
f.write(out)
f.close()

output = list()

filename = "output.txt"
with open (filename) as fin:
    for line in fin:
        output.append(line.strip())
output.sort()
output = removeDuplicates(output)
# print(output)

with open(filename, 'w') as fout:
    for line in output:
        fout.write("  " + line + '\n')