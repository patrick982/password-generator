
import random

# A function do shuffle all the characters of a string


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


# Generate a random characters (ASCII based)
uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
special1 = chr(random.randint(33, 47))
special2 = chr(random.randint(33, 47))

# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + \
    str(number1) + str(number2) + special1 + \
    special2 + lowercaseLetter1 + lowercaseLetter2
password = shuffle(password)

# Ouput
print(password)
