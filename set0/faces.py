#accepts a str as input and returns that same input with any :) converted to 🙂 and any :( converted to 🙁
def convert(str):
    return (str.replace(":)", "🙂").replace(":(", "🙁"))

def main():
    print(convert(input()))

main()
