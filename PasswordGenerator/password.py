# Importing the 'secrets' module for secure random number generation
import secrets

# Function to create a new password
def create_new(length, characters):
# Generating a random password by choosing characters randomly from the given set
    return "".join(secrets.choice(characters) for _ in range(length))
