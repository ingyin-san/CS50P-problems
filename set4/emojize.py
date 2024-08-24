"""prompts the user for a str in English and then
outputs the “emojized” version of that str,
converting any codes (or aliases) therein to their corresponding emoji."""

import emoji

emojiStr = input("Input: ").strip()
print("Output: ", emoji.emojize(emojiStr, language='alias'))
