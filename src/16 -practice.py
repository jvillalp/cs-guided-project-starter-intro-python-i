def stupid_addition(x,y):
    if type(x) == str and type(y) == str:
        return int(x) + int(y)
    if type(x) == int and type(y) == int:
        return str(x) + str(y)
print(stupid_addition(7,6))
# "76"
print(stupid_addition("6","7"))
# 13

# letters will be a list of single character 
# lowercase strings(a-z)
def mapping(letters):
    #create dictionary
    result = {}
    #loop through the input
    for letter in letters:
        #add to the dictionary
        result[letter] =letter.upper()
        # make the letter uppercase for the value
        # leave lowercase for the key

    #return value
    return result
    #dictionary with key-values where the 
    # key is the lowercae letter from input
    # and value is the corrlating uppercase letter
print(mapping(["a", "b", "c"]))