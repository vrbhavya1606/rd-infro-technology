import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return

        # Generate the password
        password = generate_password(length)
        
        # Display the password
        print("Generated password:", password)
    
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
