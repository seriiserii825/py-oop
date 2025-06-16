my_object = {}

def set_key() -> str:
    """Set a key in the my_object dictionary."""
    while True:
        key = input("Enter a key: ")
        if not key:
            print("Key cannot be empty. Please try again.")
            continue
        if key in my_object:
            print(f"Key '{key}' already exists. Please enter a different key.")
            continue
        my_object[key] = None
        return key

def set_value(key: str) -> None:
    """Set a value for the given key in the my_object dictionary."""
    while True:
        value = input(f"Enter a value for '{key}': ")
        if not value:
            print("Value cannot be empty. Please try again.")
            continue
        my_object[key] = value
        return

for _ in range(3):
    key = set_key()
    set_value(key)

print(f'my_object: {my_object}')
