#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or sentence == "":
        x = None
    else:
        x = sentence[0]
    y = len(sentence)
    tp = (y, x)
    return tp
