import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the defined character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main program
if __name__ == '__main__':
    try:
        length = int(input("Enter the desired password length: "))
        if length < 6:
            print("Password length should be at least 6 characters.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
