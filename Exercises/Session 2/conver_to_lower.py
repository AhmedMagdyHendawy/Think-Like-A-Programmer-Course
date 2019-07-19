'''

Python Course: Think like a programmer - Session 2
Excercise: Prompt the user to enter his name and convert it to be in lower case letters

July, 2019

'''
s = input("Enter Your Name")
s_new = ""

for c in s:
    if c == ' ':
        s_new += c
        continue
    if (ord(c) < 97):
        c = chr(ord(c) + 32)
    s_new += c
    

print(s_new)
    

