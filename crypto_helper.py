# Open file, read data, save words in file as uppercase into a list
with open('words.txt', 'r') as file:
    words_list = file.read().upper().split()


def generate_keystream(message, keyword):
    '''
    This function takes a keyword and turn it into a keystream by repeating
    the letters of the keyword for the entire length of the message.

    Parameters
    ----------
    message : string
        This parameter is a string that contains the encrpyted message.
    keyword : string
        This parameter is a string that is the keyword that will be used to
        crack the Vigenere cipher.

    Returns
    -------
    keystream : string
        This is the repeated keyword that is the same length as the message and
        contains the same spacing as the message

    '''

    keystream = ''
    j = 0
    for i in range(len(message)):
        if message[i] == ' ':
            keystream += ' '
        else:
            keystream += keyword[j % len(keyword)]
            j += 1
    return(''.join(keystream))


def all_english(my_string):
    '''
    The function all_english accepts one parameter, my_string, and returns
    either True or False if my_string contain all English words or not.

    Parameters
    ----------
    my_string : string
        This parameter is used to verify if all the words in the string are
        English.

    Returns
    -------
    BOOLEAN (True or False)
    '''

    # separate all words in my_string
    my_words = my_string.split()
    # check if the first 2 words are english
    if my_words[0] in words_list and len(my_words) > 1:
        if my_words[1] in words_list:
            # verify if the rest of the words are in words_list using list comprehension
            return all(word in words_list for word in my_words[2:])
        else: # first word was english, but the second word was NOT english
            return False
    # length = 1, check if 1 word is english
    elif my_words[0] in words_list:
        return True
    else: # first word was NOT english
        return False
