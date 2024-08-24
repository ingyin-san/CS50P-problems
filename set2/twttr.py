"""prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase"""

string = input("Input: ")

print("Output: ", end = "")
for s in string:
    if s not in "AEIOUaeiou":
        print(s, end = "")
print()
