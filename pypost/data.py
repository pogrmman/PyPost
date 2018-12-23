### Builtins ###
from re import findall

def process(data):
    # Append semicolon to simplify pattern matching
    if data[-1] != ";":
        data = data + ";"
    # Seperate data items into tuples and build dictionary
    seperated = findall(r"(.+?)\s{0,1}=\s{0,1}(.+?)\s{0,1};\s{0,1}", data)
    data = dict(seperated)
    return data
