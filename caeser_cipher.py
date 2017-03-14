import string, re

class Caesar(object):
    """A Caesar Cipher with the ability encode and decode messages.
    Caeser Ciphers have the following properties:

    Attributes:
        key: An integer that represents the value with which the alphabet is shifted.
        encoded_message: A jumpled string ready for decoding.
    """

    def __init__(self, encoded_message, key):
        """Return a Caesar object whose encoded_message is *encoded_message* and
        key is *key*."""
        self.encoded_message = encoded_message
        self.key = key


    def decode_or_encode(self):
        """Decoded secret (type: string) and return a string."""
        alphabet = string.ascii_lowercase

        # Shift alphabet with a push-pop stack methodology
        shifted_alphabet = alphabet[self.key:] + alphabet[:self.key] 

        # Deciphers text by referencing a dictionary of key-value pairs of old alphabet index with the shifted alphabet index
        codex = str.maketrans(alphabet, shifted_alphabet)

        # Return deciphered string
        return self.encoded_message.translate(codex)


# Engine
continues = 1
while continues:
    print('Welcome to Caesar Cipher.\n')
    
    # Get the message
    try:
        encoded_message = str(input('What is the message you would like encoded/decoded? '))
    except Exception as e:
        print('The user did not enter a string-convertible input.')
        print(e)
        break

    # Get the key
    try:
        key = int(input('What is the key value for decoding the message? '))
    except ValueError as verr:
        print('The user did not enter an integer.')
        print(verr)
        break
    except Exception as e:
        print('Something went wrong...')
        print(e)
        break

    # Run the cipher
    cipher = Caesar(encoded_message, key)
    print('\nDecoded/encoded message:', cipher.decode_or_encode())
    print()

    try:
        continues = int(input("Keep decoding? (1 for Yes, 0 for No) "))
        print()
    except ValueError as verr:
        print('The user did not enter an integer.')
        print(verr)
        break
    except Exception as e:
        print('Something went wrong...')
        print(e)
        break 
