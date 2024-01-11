import random

def create_passwords(input_file, output_file, num_passwords):
    with open(input_file, 'r') as file:
        words = file.read().splitlines()

    passwords = []
    for _ in range(num_passwords):
        num_numbers = random.randint(0, 4)  # Randomly choose the number of numbers in the password
        password = ''.join(random.choice(words) for _ in range(random.randint(2, 4)))
        password = password.replace(" ", "")  # Remove spaces from password
        password += ''.join(random.choice('0123456789') for _ in range(num_numbers))  # Add random numbers

        # Add random chance for each letter to be capital
        if random.random() < 0.25:  # 25% chance for the word to start with a capital letter
            password = password.capitalize()
        else:
            password = ''.join(random.choice([char.upper(), char]) for char in password)

        passwords.append(password)

    
    with open(output_file, 'w') as file:
        file.write('\n'.join(passwords))

#set variables
input_file = input("Enter the name of the file you want to use: ")
output_file = 'passwords.txt'
num_passwords = 1000000

create_passwords(input_file, output_file, num_passwords)
