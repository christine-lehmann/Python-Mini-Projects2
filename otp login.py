import random

generatorotp = random.randint(000000,100000)
username=input("Username: ")
print("Hello!", username)
print("Here is your otp for login", generatorotp)

password = input("Enter the otp to login: ")
if password==str(generatorotp):
    print("Successfully Login!")
else:
    password !=str(generatorotp)
    print("Failed to login")