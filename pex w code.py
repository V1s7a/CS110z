'''
PEX 2 - Vigenere Cipher 
Author: NAME GOES HERE
Course: CS110, Fall 2020
'''


import crypto_helper

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Get message from the user
message = input()
# Write the first line of the encrypt function (3.1 of PEX 2 Writeup)
# Example:  def encrypt . . .
# Include your logic design inside this function as comments

#The first function is going to take the input and convert it to numbers and make it into cipher text
def encrypt(message):
    #Start with an empty list
    secret_message = []
    #Create a loop that will store the variable and numbers into the encrypt function
    for letter in sentence():
    #Converts all 26 letters in the alphabet into a number
        a = ord(letter) - 26
    #Add this rule into the function and store variable into the function
    secret_message.append(a)
    #Calls the decrypt function to process the output of the encrypt function
    decrypt(message)
    
# Write the first line of the decrypt function (3.2 of PEX 2 Writeup)
# Include your logic design inside this function as comments

#The second function is going to convert the encrypt function into plain text using the key
def decrypt(message):
    for numbers in message():
    #This equation takes the numbers stored from eariler
        a = int(numbers)
    #Equation for making the numbers correspond with a letter
        a = a +26
    #Converts the numbers back into the correspoding characters
        a = chr(a)
#Converts every number to a letter
    #chr()


print(secret_message)
    
# Write the first line of the crack message function (3.3 of PEX 2 Writeup)
# Include your logic design inside this function as comments

#This function is going to use the key and turn the message into the secret code
def crack():
   x = 1;
'''
Uncomment this code when you are ready to test it
'''
# TEST CODE FOR THE ENCRYPT FUNCTION
#ciphertext = encrypt("I LOVE COMPUTER SCIENCE", "CYBER")
#print(ciphertext)

# TEST CODE FOR THE DECRYPT FUNCTION
#plaintext = decrypt("K JPZV EMNTLVCS WTKCOGV", "CYBER")
#print(plaintext)

# TEST CODE FOR THE CRACK MESSAGE FUNCTION
#cracked_key = crack_message("sample_message.txt")
#print(cracked_key)
