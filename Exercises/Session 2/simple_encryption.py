'''

Python Course: Think like a programmer - Session 2
Excercise: Prompt the user for a string and encrypt it :D 

July, 2019

'''

def encrypt(s):
	
	s_encrypted = ""

	for c in s:
		asc = ord(c)
		asc = asc * 2 + 4
		c_enc = chr(asc)
		s_encrypted += c_enc

	return s_encrypted




msg = input("talk!\n")

msg_enc = encrypt(msg)

print(" Your msg after encryption: " + msg_enc)



		
		

