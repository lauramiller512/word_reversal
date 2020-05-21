import unittest
import reversal_function

# def reverse_words(string):
#     new_string = " ".join("".join(reversed(word)) for word in string.split())
#     return (new_string)

# n = input("Enter text to be reversed: " )

# print (reverse_words(n))

class TestReversalFunction(unittest.TestCase):

    # method needs to start with test_
    def test_add(self):
        result = reversal_function.reverse_words("Hello there")
        self.assertEqual(result, "olleH ereht")