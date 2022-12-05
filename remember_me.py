import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'json/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
#    username = 'Michael' # When using Spyder
    filename = 'json/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
#        print(f"Is the correct username: {username}? (y or n)") # For Spyder
        ans = input(f"Is the correct username: {username}? (y or n)")
#        ans = 'y' # For Spyder
        if 'y' in ans:
            pass
        else:
            username = get_new_username()
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
