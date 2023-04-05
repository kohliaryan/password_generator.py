import random
import math

def length_of_password():
    while True:
        try:
            length = int(input("What should be length of your password: "))
            return length
        except ValueError:
            print("Please enter a valid integer")

def choose_specifications():
    print("\nChoose one out of the following specifications- ")
    print("\t1. Only numerical")
    print("\t2. Only alphabetical")
    print("\t3. Alphanumeric")

    choice = int(input("Enter your option: "))
    if choice in [1, 2, 3]:
        return choice
    else:
        print("Please enter a valid option")
        return choose_specifications()

def numerical_password(length):
    start_limit = math.pow(10 , (length-1))
    end_limit = (math.pow(10, length)) - 1
    return random.randint(start_limit, end_limit)

def alphabetical_password(length):
    password = ''
    for i in range(length):
        character = chr(random.randint(65, 90))
        password += character
    return password

def alphanumeric_password(length):
    password = ''
    for i in range(length):
        choose = random.randint(0 , 1)
        if choose == 0:
            digit = random.randint(0 , 9)
            password += str(digit)
        elif choose == 1:
            character = chr(random.randint(65, 90))
            password += character
    return password

def another_password():
    while True:
        user_want = input("Do you want to generate another password? (Y/n): ")
        if user_want.lower() == 'y':
            return True
        elif user_want.lower() == 'n':
            return False
        else:
            print("Please enter a valid option")

def generate_password():
    length = length_of_password()
    specifications = choose_specifications()

    if specifications == 1:
        password = numerical_password(length)
    elif specifications == 2:
        password = alphabetical_password(length)
    elif specifications == 3:
        password = alphanumeric_password(length)

    return password

print("\nHello! I am password generator.")

while True:
    password = generate_password()
    print(f"\nYour password is {password}")
    print("Password generated successfully.")
    if not another_password():
        break

print("Thanks for using password generator!")
