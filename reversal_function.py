string = input("Enter text to be reversed: " )

def reverse_words(string):
    string = "".join(reversed(string))
    return string

print (reverse_words(string))