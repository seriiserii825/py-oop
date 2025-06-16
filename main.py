from InputValidator import InputValidator


my_object = {}


def set_key() -> str:
    while True:
        key = InputValidator.get_string("Enter a key: ", allow_empty=False)
        if key not in my_object:
            return key
        print(f"Key '{key}' already exists. Please enter a different key.")


def set_value(key: str) -> None:
    value = InputValidator.get_string(
        f"Enter a value for '{key}': ", allow_empty=False)
    my_object[key] = value


for _ in range(3):
    key = set_key()
    set_value(key)

print(f'my_object: {my_object}')
