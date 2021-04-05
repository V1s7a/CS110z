'''
PEX 2 - Vigenere Cipher 
Author: NAME GOES HERE
Course: CS110, Fall 2020
'''

#from cs110 import autograder
#import crypto_helper

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Get message from the user
#message = input()
# Write the first line of the encrypt function (3.1 of PEX 2 Writeup)
# Example:  def encrypt . . .
# Include your logic design inside this function as comments

#The first function is going to take the input and convert it to numbers and make it into cypher text
def encrypt(message, key):
    #Use the function generate_keystream
    #keystream = crypto_helper.generate_keystream(message, key)    
    #Start with an empty list
    messageNum = []
    keyNum = []
    encryptedNum = []
    encryptedMessage = []
    #Use the two parameters of the orginal message and the key
    #Create a loop that will run through every letter of the message in the string
    for i in message:
        #Create an equation set to any variable that will convert all 26 letters in the alphabet into a number
        #Create a loop that convert the key string into numbers
        for j in alphabet:
            if i == j:
                messageNum.append(alphabet.index(j))
                break
            elif i == ' ':
                messageNum.append(' ')
                break
    print(messageNum)
    #convert key to number and return value in keyNum
    for i in key:
        for j in alphabet:
            if i == j:
                keyNum.append(alphabet.index(j))
                break
    print(keyNum)

    #Add this rule into a new list and store variable into the new list
    #Use a for loop to go through the added list and convert the number back into a letter
    for i in messageNum:
        if i == ' ':
            encryptedNum.append('')
        else:
            x = i
            for j in keyNum:
                if x > 26:
                    y = x % 26
                    x = y
                else:
                    x = x + j
            encryptedNum.append(x)
    print(encryptedNum)

    for i in encryptedNum:
        if i == ' ':
            encryptedMessage.append(' ')
        else:
            for j in alphabet:
                if alphabet.index(j) == i:
                   encryptedMessage.append(j)
                   break

            

    return encryptedMessage

        
        #Should the number exceed 26, call Modulo to wrap the numbers around the alphabet again to get a number, then convert to letter
    #Add this rule into the function and store variable into the function 
    #Print final encrypted message
    
    
#The second function is going to convert the encrypt function into plain text using the key
def decrypt(message, key):
    #Use the function generate_keystream    
    #Start with an empty list
    #Use the two parameters of the encrypted message and the key
    #Create a loop that will run through every letter of the message in the string
    #Create an equation set to any variable that will convert all 26 letters in the alphabet into a number
    #Create a loop that convert the key string into numbers
    #Subtract number version of keystream from the number version of the encrypted message
    #Use a for loop to go through the added list and convert the number back into a letter
        #Call Modulo to wrap the numbers around the alphabet again to get a number, then convert to letter
    #Add this rule into the list and store variable into the string
    #Print final decrypted message
    
   
#This function is going to use the key and turn the message into the secret code
    print("hello")
def crack_message(message):
    #Start with an empty list
    #Use the parameter of the given file
    #Create a loop that will run through every letter possible upper case four letter combination
    #Create a loop that convert the key string into numbers
    #Subtract number version of keystream from the number version of the encrypted message
    #Use a for loop to go through the added list and convert the number back into a letter
        #Call Modulo to wrap the numbers around the alphabet again to get a number, then convert to letter
    #Add this rule into the list and store variable into the string
    #Call the functions all_english using the new decrypted string as the parameter
    #When function is false, run through more four letter combinations
    #When function is true, code is cracked
    #Print decrypted message
    #Print four letter key
    print("hello")
'''
Uncomment this code when you are ready to test it
'''
# TEST CODE FOR THE ENCRYPT FUNCTION
ciphertext = encrypt("I LOVE COMPUTER SCIENCE", "CYBER")
print(ciphertext)

# TEST CODE FOR THE DECRYPT FUNCTION
#plaintext = decrypt("K JPZV EMNTLVCS WTKCOGV", "CYBER")
#print(plaintext)

# TEST CODE FOR THE CRACK MESSAGE FUNCTION
#cracked_key = crack_message("sample_message.txt")
#print(cracked_key)