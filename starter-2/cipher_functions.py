# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# This function will convert all alphabets to upper case alphabets
# and will remove any character that is not an alphabet.

def clean_message(message):
    """ (str) -> str

    Return the uppercase alphabetic value of all characters in the
    message(message).

    >>> clean_message('John')
    'JOHN'
    >>> clean_message('Please Call Me')
    'PLEASECALLME'
    """
    cleaned_message=""
    
    for ch in message:
        if ch.isalpha() == True:
            if ch.isupper() == True:
                cleaned_message = cleaned_message + ch
            elif ch.islower() == True:
                cleaned_message = cleaned_message + ch.upper()
        elif not ch.isalpha():
            ch = ''
            cleaned_message=cleaned_message + ch
                         
    return cleaned_message

# This function will encrypt the letter by adding
# the value of the letter based on it's position to 
# the keystream value and converting it back to a
# letter based on the value. 

def encrypt_letter(character, keystream_value):
    """ (str, int) -> str

    Return the encrypted character based on the integral value
    of the character and the keystream_value.

    >>> encrypt_letter('A', 3)
    'D'
    >>> encrypt_letter('E', 24)
    'C'
    """
# Variable primarily used to simplify the statements below.

    new_char_val=(ord(character) + keystream_value)

    if (new_char_val - 65) <= 25 and (new_char_val - 65) >= 0:
        return (chr((new_char_val - 65)+ 65))
    elif (new_char_val-65) > 25:
        return chr(0 + ((new_char_val - 65)- 25)+ 64)

# This function will decrypt the encrypted character by
# subtracting the keystream value and finding the original 
# position of the character, converting it back to the initial character.

def decrypt_letter(character, keystream_value):
    """ (str, int) -> str

    Return the original character by decrypting the encrypted
    character(encrypted_character) using the keystream
    value(keystream_value).

    >>> decrypt_letter('C', 3)
    'Z'
    >>> decrypt_letter('O', 9)
    'F'
    """
# Variable primarily used to simplify the statements below.

    decr_char_val=(ord(character) - keystream_value)

    if (decr_char_val - 65) <= 25 and (decr_char_val - 65) >= 0:
            return (chr(decr_char_val))
    else:
        return chr(decr_char_val + 26)

# This function will swap the card with the card under it in the deck.

def swap_cards(deck, index):
    """ (list of int, int) -> NoneType

    Return the deck of cards by swapping the card with index(index)
    with the card below it in the deck(deck).

    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>swap_cards(deck, 3)
    [1, 4, 7, 13, 10, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 27]
    >>>swap_cards(deck, 9)
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 28, 6, 9, 12, 15, 18, 21, 24,
    26, 2, 5, 8, 11, 14, 17, 20, 23, 27]
    """

    if (index) <= 26:
        temp = deck[index+1]
        deck[index+1] = deck[index]
        deck[index] = temp
    elif (index == 27):
        temp = deck[0]
        deck[0] = deck[index]
        deck[index] = temp



# This function will find Joker 1 in the deck and
# replace it with the card below it in the deck.

def move_joker_1(deck):
    """ (list of int) -> NoneType

    Return the deck(deck) after swapping joker 1 with the
    number below it in the deck.

    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>move_joker_1(deck)
    >>>deck
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2,
    27, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>move_joker_1(deck)
    >>>deck
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2,
    5, 27, 8, 11, 14, 17, 20, 23, 26]
    """
    i=0
    for num in deck:
        if num != JOKER1:
            i = i+1
        elif num == JOKER1:        
            return swap_cards(deck, i)
                
                

# This function will find Joker 2 in the deck
# and replace it with the card below it in the deck.

def move_joker_2(deck):
    """ (list of int) -> NoneType

    Swaps joker 2 with the number below it in the deck.

    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>move_joker_2(deck)
    >>>deck
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>move_joker_2(deck)
    >>>deck
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 9, 12, 28, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    """
    index = deck.index(JOKER2)
    temp = []

# If the new position is at the end of this deck,
# the cards are moved according to position,
# in the new temporary deck.

    if (index+2) <= 27:
       temp += deck[0:index]
       temp += deck[(index+1):(index+3)]
       temp.append(JOKER2)
       temp += deck[(index+3):]

# If the new position is at the beginning of
# the deck, then these statements would shift the cards
# into a temporary deck according to position.

    elif (index+2) > 27:

# These statements are specific to if the card will
# take position 1 or position 2 in the deck.

            if (index+2-28) != 0:
                temp += deck[(index+2-28): (index+2-27)]
                temp.append(JOKER2)
                temp += deck[(index+2-27):index]
                temp += deck[(index+1):]
                temp.append(deck[0])
            elif (index+2-28)==0:
                temp.append(JOKER2)
                temp += deck[(index+2-27):index]
                temp += deck[index+1:]
                temp.append(deck[(index+2-28)])

# This finally replaces the cards in the original
# deck with the cards in the new deck.

    for item in range(len(deck)):
        deck[item] = temp[item]
                      
# This function will perform a triple cut by switching
# the cards before the first Joker with the cards after the
# second Joker in the deck.


def triple_cut(deck):
    """ (list of int) -> NoneType

    Amends the deck by finding which Joker comes first, finding all the
    cards before that and placing it after the second joker after which
    it takes the cards that come after the second joker and places it
    before the first.

    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]   
    >>>triple_cut(deck)
    >>>deck
    [2, 5, 8, 11, 14, 17, 20, 23, 26, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25]
    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    >>>triple_cut(deck)
    >>>deck
    [27, 2, 5, 8, 11, 14, 17, 20, 23, 28, 1, 4, 7, 10, 13, 16,
    19, 22, 25, 26, 3, 6, 9, 12, 15, 18, 21, 24]
    """
# Each variable is created so that each segment of the deck
# could be copied to a specific list.

    new_end_cards = []
    new_front_cards = []
    middle_cards = []
    index_joker_2 = deck.index(JOKER2)
    index_joker_1 = deck.index(JOKER1)

# In the situation where Joker 1 comes before Joker 2.    

    if (index_joker_1) < (index_joker_2):
        new_end_cards = deck[0:index_joker_1]
        new_front_cards = deck[(index_joker_2)+1:]
        middle_cards = deck[(index_joker_1):(index_joker_2)+1]

# In the case where Joker 2 comes before Joker 1.      

    else:
        new_end_cards = deck[0:(index_joker_2)]
        new_front_cards = deck[(index_joker_1)+1:]
        middle_cards = deck[index_joker_2:(index_joker_1)+1]

# A temporary list is created and each segment of the deck is copied
# to fit the specifications with the end cards shifted to
# the beginning and vice-versa.

    temp_deck = []
    temp_deck += (new_front_cards)
    temp_deck += (middle_cards)
    temp_deck += (new_end_cards)

#This copies the temporary list values to the deck.
    
    for item in range(len(deck)):
        deck[item] = temp_deck[item]
    
      
# This function will take the value of the last card and take that
# many cards from the front and move it behind the last card.

def insert_top_to_bottom(deck):
    """(list of int) -> NoneType

    Amend the deck(deck) by taking the number of cards equivalent
    to the last number(deck[27]) in the deck from the front of the
    deck and placing them before the last card in the deck.

    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26]
    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, 12, 15,
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, 12, 15, 18, 21,
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 28]

    """
    number_of_cards = deck[27]
    temp_deck = []

# If the last card is not equivalent to any of the jokers,
# this stores the middle segment of the cards in temp_deck and then adds the first
# few cards after that, finally appending the last card.

    if  number_of_cards != JOKER2 and number_of_cards != JOKER1:
        temp_deck += (deck[(number_of_cards):27])
        temp_deck += deck[0:(number_of_cards)]       
        temp_deck.append(number_of_cards)

# If the last card is a Joker then this will use the value of
# JOKER1 and perform the commands above.

    else:
        number_of_cards = JOKER1
        temp_deck += (deck[(number_of_cards):27])
        temp_deck += deck[0:(number_of_cards)]       
        temp_deck.append(deck[27])

# Once the temp_deck is created, this loop will transfer all 
# the values in temp_deck to the original deck hence amending
# the deck according to the function.

    for item in range(len(deck)):
        deck[item]=temp_deck[item]

# This function finds the card at the position of the
# value of the first card in the deck and returns it.

def get_card_at_top_index(deck):
    """(list of int) -> int

    Return the card at the position of the value of
    the first card in the deck(deck).

    >>>get_card_at_top_index([1, 4, 7, 10, 13, 16, 19, 22, 25, 28,
    3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    4
    >>>get_card_at_top_index([19, 4, 7, 10, 13, 16, 1, 22, 25, 26, 3,
    6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 28])
    2
    """
    val_card_1=deck[0]
    
    if (val_card_1 != JOKER2):
        return deck[val_card_1]
    elif (val_card_1 == JOKER2): 
        val_card_1 = JOKER1
        return deck[val_card_1]

# This function gets the next keystream value.

def get_next_value(deck):
    """(list of int) -> int
    
    Return the keystream value for the next card in the deck.

    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>get_next_value(deck)
    11
    >>>deck=[19, 4, 7, 10, 13, 16, 1, 22, 25, 26, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    >>>get_next_value(deck)
    15  
    """
    move_joker_1(deck)
    move_joker_2(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    return (get_card_at_top_index(deck))
    
    
        

# This function performs the algorithm to find the
# next keystream value within the given range.

def get_next_keystream_value(deck):
    """(list of int) -> int

    Return the next keystream value of the deck(deck) that
    is in the range of 0 to 27.

    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>get_next_keystream_value(deck)
    18
    >>>get_next_keystream_value(deck)
    14
    """

# This while loop keeps on repeating all steps of the 
# algorithm till the keystream value returned is within
# the range of 0 and 27.

    keystream_val = (get_next_value(deck))

    while ((keystream_val) <= 0) or ((keystream_val) >= 27):
        keystream_val = (get_next_value(deck))

    return (keystream_val)
        
    
        
        

# This function will encrypt or decrypt a message
# based on the users command.

def process_message(deck, message, encrypt_or_decrypt):
    """(list of int, str, str) -> str

    Return an encrypted or decrypted message based on the input.

    >>> deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_message(deck, 'It does not do to dwell on dreams and forget to live.', 'e')
    'KILRUMFOUVJIGQONHVUSYNADYCPIMXWKIPJAJGVIL'
    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_message(deck, 'AHGKHWHEFXNOJNXSSTKYQOIBQCPAZQPSWLPURNODP', 'd')
    'ITDOESNOTDOTODWELLONDREAMSANDFORGETTOLIVE'   
    """
    encrypted=''
    decrypted=''

# If the user wants the system to encrypt the message, the 
# system performs the algorithm, finds the keystream value,
# cleans the message and decrypts it. 

    if (encrypt_or_decrypt == 'e'):
        message = clean_message(message)
        for letter in message:
            keystream_value=get_next_keystream_value(deck)
            encrypted = encrypted + str(encrypt_letter(letter, keystream_value))
        return encrypted

# If the user wants the system to decrypt the message, the
# system performs the algorithm again, finds the keystream
# value and decrypts the message.

    elif (encrypt_or_decrypt == 'd'):
        for letter in message:
            keystream_value = get_next_keystream_value(deck)
            decrypted = decrypted + str(decrypt_letter(letter , keystream_value))
        return decrypted
    
# This function decrypt and encrypts lists of messages.

def process_messages(deck, list_of_messages, encrypt_or_decrypt):
    """(list of int, list of str, str) -> list of str

    Return the encrypted or decrypted list of messages.

    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_messages(deck, ['John', 'can', 'not', 'go', 'home'], 'e')
    ['BCKJ', 'FEH', 'DAN', 'FJ', 'CYNS']
    >>>deck=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_messages(deck, ['BCKJ', 'FEH', 'DAN', 'FJ', 'CYNS'], 'd')
    ['JOHN', 'CAN', 'NOT', 'GO', 'HOME']

    """
    message_after_process = []
    for message in list_of_messages:
        message_after_process.append(process_message(deck, message, encrypt_or_decrypt))
    return (message_after_process)


# This function will open the mentioned file and add every
# line in the file as a string in the list.

def read_messages(open_file):
    """(file open for reading) -> list of str

    Return a list with each line of the opened file(open_file)
    as a string in the list.

    >>>file='/Users/siddharthgautam/Desktop/starter-2/message_file1.txt'
    >>>open_file=open(file, 'r')
    >>>read_messages(open_file)
    ['It does not do to dwell on dreams and forget to live.', 'Albus Dumbledore']
    >>>file='/Users/siddharthgautam/Desktop/starter-2/secret1.txt'
    >>>open_file=open(file, 'r')
    >>>read_messages(open_file)
    ['TCAVORYZALXEZDUJUFFFMHXXVPYHPYNRWWVHVJAHQ', 'BQRAUFQEYXOVOTU'] 
    """  
    line=open_file.readline()
    list_of_messages = []
    while line != '':
        list_of_messages.append(line.strip('\n'))
        line=open_file.readline()
    return list_of_messages

    
# This function will read the deck and transfer
# every number in the deck to a list.
    
def read_deck(open_deck):
    """(file open for reading) -> list of int

    Return a list with each number in the deck file being a separate
    string in the list.

    >>>deck_file='/Users/siddharthgautam/Desktop/starter-2/deck1.txt'
    >>>open_deck=open(deck_file, 'r')
    >>>read_deck(open_deck)
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>deck_file='/Users/siddharthgautam/Desktop/starter-2/deck2.txt'
    >>>open_deck=open(deck_file, 'r')
    >>>read_deck(open_deck)
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    """
    line = open_deck.readlines()
    list_of_integers = []
    number = ''
    for index in range(len(line)):
        for ch in line[index]:
            if (ch != ' ') and (ch !='\n') and (ch != ''):
                number += ch
            else:
                if number != '':
                    list_of_integers.append(int(number))
                number = ''
    return list_of_integers
