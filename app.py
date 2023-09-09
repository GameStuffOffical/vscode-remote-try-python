#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import markovify
from spacey import spacer
from spacey import deSpacer

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return app.send_static_file("index.html")
def removeDuplicates(dupList):
    noDupList = []
    for element in dupList:
            if element not in noDupList:
                noDupList.append(element)
    return noDupList
def multiModel(texts = [], state_size = 1):
    models = []
    for i in texts:
        with open(i) as f:
            text = f.read()

            models.append(markovify.NewlineText(text, state_size))
            f.close()
    return markovify.combine(models)

# for i in range(5):
    # print(multiModel(["corpus/cabinet man.txt", "corpus/ultimate showdown.txt","corpus/touch tone telephone.txt"], 1).make_sentence())

with open("corpus/units.txt") as f:
     text = f.read()
     e = markovify.NewlineText(spacer(text), state_size = 1)
     f.close

for i in range(100):
    print(deSpacer(e.make_sentence()))