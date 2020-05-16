def reverse_words(string):
    # words = string.split()
    # string = "".join(reversed(string))
    # string = (reversed(x)) 
    # return (string) 

    new_string = " ".join("".join(reversed(word)) for word in string.split())
    return (new_string)

n = input("Enter text to be reversed: " )

print (reverse_words(n))