string = input("Enter text to be reversed: " )

print (string)

def reverse_words(string):
    string = "".join(reversed(string))
    x = string.split()
    # string = (reversed(x)) 
    return (string) 

print (string)