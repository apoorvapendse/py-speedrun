import random;
import string

alphabets = string.ascii_letters
numbers = string.digits
special_chars = "!@#$%^&*+_/><"

chars = []

alphabetsFlag = input("Do you want alphabets in your password? (y or n):")
numbersFlag = input("Do you want alphabets in your password? (y or n):")
specialCharsFlag = input("Do you want alphabets in your password? (y or n):")

if alphabetsFlag=='y' or alphabetsFlag =='Y':
    chars.extend(alphabets)
if numbersFlag=='y' or numbersFlag =='Y':
    chars.extend(numbers)
if specialCharsFlag=='y' or specialCharsFlag =='Y':
    chars.extend(special_chars)

print(chars[0])




passwdlen = int(input("Enter the length of password you want to generate "))

generatedPassword = ""

for i in range(passwdlen):
    randomIndex = random.randint(0,len(chars)-1)
    newChar = chars[randomIndex]
    generatedPassword = generatedPassword + newChar
    
print("your new password:",generatedPassword)