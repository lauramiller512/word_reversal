# def reverse_words(string):
#     new_string = " ".join("".join(reversed(word)) for word in string.split())
#     return (new_string)

def reverse_words(string):
    new_string = ''.join(reversed(string)) # reverses the entire string
    return (new_string)

n = input("Enter text to be reversed: " )

print (reverse_words(n))