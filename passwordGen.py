# console.log
import random;

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p''q','r','s','t','u','v','w','x','y','z']


passwdlen = int(input("Enter the length of password you want to generate "))

generatedPassword = ""

for i in range(passwdlen):
    randomIndex = random.randint(0,25)
    newChar = alphabets[randomIndex]
    generatedPassword = generatedPassword + newChar
    
print("your new password:\n%s",generatedPassword)