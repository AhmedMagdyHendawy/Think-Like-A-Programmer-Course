'''

Python Course: Think like a programmer - Session 2
Excercise: Prompt the user for a number and check if it's prime or not

July, 2019

'''


x = int(input("Enter a number: "))

is_prime = True

for i in range(2, (x // 2) + 1):
    if x % i == 0:
        is_prime = False
        break
        

if is_prime:
    print("the number " + str(x) + " is a prime number!")
else:
    print("the number " + str(x) + " is not prime number!")
        
    
