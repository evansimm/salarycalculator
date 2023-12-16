# Python Project: Password Creator

import random

capitalLetters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowerLetters = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
specialCharacters = "?,.<>!%$[]}{*)(|@#%^&-_=+"

capital,lower,digits,special = True,True,True,True

finalPassword = ""

if capital:
    finalPassword += capitalLetters
if lower:
    finalPassword += lowerLetters
if digits:
    finalPassword += numbers
if special:
    finalPassword += specialCharacters

passwordLength = 16
passwordQuantity = 10

for x in range(passwordQuantity):
    password = "".join(random.sample(finalPassword,passwordLength))
    print(password)