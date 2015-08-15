"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'secret3.txt'
MODE = 'd'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    open_deck = open(DECK_FILENAME, 'r')
    open(DECK_FILENAME, 'r')
    deck = (cipher_functions.read_deck(open_deck))
    open_file = open(MSG_FILENAME, 'r')
    open(MSG_FILENAME, 'r')
    message = (cipher_functions.read_messages(open_file))
    print (cipher_functions.process_messages(deck, message, MODE))
   

    pass

main()



   

