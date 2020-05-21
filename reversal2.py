# this file is for testing ways of reversing and splitting strings

# ::-1 reverses all items in the array
# a[start:stop] slice notation: first number is where to start in array
# second number is where it stops

# .join method joins words together into a string

# 'for word in': iterate through each character in the string

# So this is splitting each word in the string, reversing the letters within the word,
# and then joining the words back together again

print("This function will reverse all the letters within the string while keeping the words in their origin place")

string = input("Enter text to be reversed: " )

new_string = (string[::-1]) # reverses the entire string
# print(new_string)

x = new_string.split()
# print(x)

reversed = ' '.join(reversed(x))
print(reversed)