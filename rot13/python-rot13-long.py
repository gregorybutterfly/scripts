"""ROT13 LONG VERSION"""

import string

# generate an alphabet
alphabet = string.ascii_lowercase

print(alphabet)

def message_code(lst):
    """ code message """
    
    for letter in list(lst.lower()):
        if letter in alphabet:
            res = alphabet.index(letter) + 13
            if res > len(alphabet):
                res = res - len(alphabet)
                return alphabet[res]
            else:
                return alphabet[res]

def message_decode(lst):
    "" decode message """

    for letter in lst:
        result = alphabet.index(letter) - 13
        if result < 0:
            result = result + len(alphabet)
            return alphabet[result]
        else:
            return alphabet[result]

to_code = "rotate"
coded = []
decoded = []

for letter in to_code:
    coded.append(message_code(letter))

for letter in coded:
    decoded.append(message_decode(letter))

print("To code: ", to_code)
print("Coded: ", "".join(coded))
print("Decoded: ", "".join(decoded))
