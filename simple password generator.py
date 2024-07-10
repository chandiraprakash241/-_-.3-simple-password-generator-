import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("No character types selected for password generation")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Example usage:
password_length = 12
password = generate_password(length=password_length)
print(f"Generated password: {password}")
