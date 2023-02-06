#finds middle character of a word
def middle(word):
    length = len(word)
    if length == 0:
        return ""
    if length % 2 ==1:
        return word[length//2] #brackets used to access middle character of length//2 (rounded down)
    else:
        return ""


word = input("Enter a word: ")
print(middle(word))