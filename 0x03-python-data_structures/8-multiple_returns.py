#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        ist_leta = (sentence[0],)
    else:
        ist_leta = None
    length = (len(sentence),)
    return length, ist_leta
