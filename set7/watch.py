"""a function called parse that expects a str of HTML as input,
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and
returns its shorter, shareable youtu.be equivalent as a str."""

import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    matches = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"', s)
    if matches:
        return "https://youtu.be/" + matches.group(1)
    return None


if __name__ == "__main__":
    main()
