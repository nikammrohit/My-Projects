#Tells where upperCase and lowerCase letters are in a string
#i for i is a list of index while c is the character in the string. enumerate stores location of the index, character
def upper(word):
    #i for i is list of index at c (characters) of loop of 'word' if character is uppercase
    return[i for i,c in enumerate(word) if c.isupper()]
def lower(word):
    #i for i is list of index at c (characters) of loop of 'word' if character is uppercase
    return[i for i,c in enumerate(word) if c.islower()]
word = str(input())
print (upper(word),"\n", lower(word))