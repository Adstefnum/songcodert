from music_cipher_functions import *

text = input("Enter the text:")
encrypt(text)

again = input("Would you like to hear it again?(yes/no):")

while again.lower() == 'yes':
	encrypt(text)

	break