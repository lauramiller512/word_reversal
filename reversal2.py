print("This function will reverse all the letters within the string while keeping the words in their origin place")

string = input("Enter text to be reversed: " )

new_string = (string[::-1]) # reverses the entire string
# print(new_string)

x = new_string.split()
# print(x)

reversed = ' '.join(reversed(x))
print(reversed)