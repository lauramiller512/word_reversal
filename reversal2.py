string = input("Enter text to be reversed: " )

new_string = (string[::-1]) # reverses the entire string
print(new_string)

x = new_string.split()
print(x)

reversed = ' '.join(reversed(x))
print(reversed)


# print(x[::-1])
