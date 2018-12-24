### Builtins ###
from re import findall

def process(data):
    # Append semicolon to simplify pattern matching
    if data[-1] not in (",",";"):
        data = data + ";"
    # Seperate data items into tuples and build dictionary
    seperated = findall(r"(.+?)\s{0,1}(=|:)\s{0,1}(.+?)\s{0,1}(;|,)\s{0,1}", data)
    seperated = [(tup[0], tup[2]) for tup in seperated]
    data = dict(seperated)
    return data
