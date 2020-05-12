# ::-1 reverses all items in the array
# a[start:stop] slice notation: first number is where to start in array
# second number is where it stops

# .join method joins words together into a string

# 'for word in': iterate through each character in the string

# So this is splitting each word in the string, reversing the letters within the word,
# and then joining the words back together again


user_input = input("Enter text to be reversed: ")

new_string = " ".join(word[::-1] for word in user_input.split())

print(new_string)