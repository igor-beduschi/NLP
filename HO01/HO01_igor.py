# Python activity for text normalization
# Igor Beduschi - 659318
# special characters remove, change accentuation to normal text, and text downcase.

import unicodedata as uni


normalized_text = ''

# Read text from file, and close after
with open('datasets/Shakespeare.txt') as f:
    # Go through each character in the file
    for char in f.read():
        # Remove (ignore) special characters
        if not uni.category(char).startswith("P"):
            # normalize accents
            char = uni.normalize('NFKD', char).encode('ASCII', 'ignore').decode('ASCII')
            # convert to lowercase
            char = char.lower()
            # add to normalized text string
            normalized_text += char

# Write normalized text to file
with open("HO01/normalized_text.txt", "w+") as txt_file:
    txt_file.write(normalized_text)