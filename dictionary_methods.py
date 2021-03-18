myDict = {
    "fast": "In a Quick Manner",
    "Neeraj": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Neeraj': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "neeraj": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("neeraj")) # Prints value associated with key "harry"
print(myDict["neeraj"]) # Prints value associated with key "harry"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("neeraj2")) # Returns None as harry2 is not present in the dictionary
print(myDict["neeraj2"]) # throws an error as harry2 is not present in the dictionary