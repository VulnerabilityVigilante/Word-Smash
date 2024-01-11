import random
import string

def create_passwords(input_file, output_file, num_passwords):
    with open(input_file, 'r') as file:
        words = file.read().splitlines()

    passwords = set()  # Use a set to store unique passwords

    while len(passwords) < num_passwords:
        num_numbers = random.randint(0, 4)  # Randomly choose the number of numbers in the password
        password = ''.join(random.choice(words) for _ in range(random.randint(2, 4)))
        password = password.replace(" ", "")  # Remove spaces from password

        # Add random chance for each letter to be capital
        if random.random() < 0.25:  # 25% chance for the word to start with a capital letter
            password = password.capitalize()
        else:
            password = ''.join(random.choice([char.upper(), char]) for char in password)

        # Add random chance for special characters
        if random.random() < 0.2:  # 20% chance for special characters
            num_special_chars = random.randint(0, 3)  # Randomly choose the number of special characters
            special_chars = random.choices(string.punctuation, k=num_special_chars)
            password += ''.join(special_chars)

        password += ''.join(random.choice('0123456789') for _ in range(num_numbers))  # Add random numbers

        if password not in passwords:  # Check if the password is already in the set
            passwords.add(password)  # Add the password to the set

    with open(output_file, 'w') as file:
        file.write('\n'.join(passwords))

#set variables
input_file = input("Enter the name of the file you want to use: ")
output_file = 'passwords.txt'
num_passwords = 1000000

create_passwords(input_file, output_file, num_passwords)
