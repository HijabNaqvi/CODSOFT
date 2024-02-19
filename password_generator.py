# Python Pasword Generator
import random
import string

# Password Generator Function
def password_generator(length):
    # Define character sets
    upper = string.ascii_uppercase
    special_char = string.punctuation
    letters = string.ascii_letters
    numbers = string.digits

    # Ensure at least one uppercase letter and one special character
    password = random.choice(upper) + random.choice(special_char)

    # Generate remaining characters
    remaining_length = length - 2
    all_characters = upper + special_char + letters + numbers
    password += "".join(random.choice(all_characters) for i in range(remaining_length))
    return(password)

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

length = int(input("What should be the length of your password? \n"))
gen_password = password_generator(length)
print("Your password suggestion is: \n", gen_password)



'''
Time complexity: O(n)
Space complexity: O(n)
'''