import random
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)
upperCase1 = chr(random.randint(65,90))
upperCase2 = chr(random.randint(65,90))
lowerCase1 = chr(random.randint(97,122))
lowerCase2 = chr(random.randint(97,122))
special1 = chr(random.randint(33,64))
special2 = chr(random.randint(33,64))
number1 = chr(random.randint(48,57))
number2 = chr(random.randint(48,57))
password = upperCase1 + upperCase2 + lowerCase1 + lowerCase2 + special1 + special2 + number1 +number2
password = shuffle(password)

print (password)