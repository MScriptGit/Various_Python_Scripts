#Made by MScript 2024
def encrypt(text,s):

    result = ""
 

    # traverse text

    for i in range(len(text)):

        char = text[i]
 

        # Encrypt uppercase characters

        if (char.isupper()):

            result += chr((ord(char) + s-65) % 26 + 65)
 

        # Encrypt lowercase characters

        else:

            result += chr((ord(char) + s - 97) % 26 + 97)
 

    return result
 
#check the above function

text = input("put text here:")

s = 0

print ("Text  : " + text)
	
while s != 26:

	print ("Shift : " + str(s))

	print ("Cipher: " + encrypt(text,s))
	
	print("\n")

	if s == 26:
		
		break
		
	s += 1
