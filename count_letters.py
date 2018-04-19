"""Letters Counter will count number of each letter found in a given file"""

# import string to use string.ascii_letters which will print out an alphabet containing small and Large letters.
import string

# === LONG VERSION ===
print('=== LONG VERSION ===')
print(' ')


def count_letters(filename):
    """ A simple function to count number of letters found in a given file."""

    # A dictionary to store found letters
    letters = {}

    # Open a file with context manager and assign its contents to 'data' variable. It will work for test purpose.
    with open(filename, 'r') as f:
        data = f.read()

        # for each character found in data...
        for l in data:
            # if that character is a letter of an alphabet...
            if l in string.ascii_letters:
                # add that letter to our letters dictionary and increment the counter + 1
                letters[l] = letters.get(l, 0) + 1

    # return letters dictionary
    return letters


count_letters('letters.txt')

for letter, counter in count_letters('letters.txt').items():
    print('Letter "{}" found {} times!'.format(letter, counter))
