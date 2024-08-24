"""prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase"""


def main():
    string = input("Input: ")
    print("Output: ", shorten(string))


def shorten(word):
    short = ''
    
    for s in word:
        if s not in "AEIOUaeiou":
            short += s

    return short


if __name__ == "__main__":
    main()
