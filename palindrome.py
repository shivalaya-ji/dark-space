def is_palindrome(text):
    """
    Check if the given text is a palindrome.

    Parameters:
        text (str): The string to check.

    Returns:
        bool: True if the cleaned text is a palindrome, False otherwise.

    Notes:
        Non-alphanumeric characters are removed and case is ignored.
    """
    # Validate input: must be a non-empty string
    if not isinstance(text, str) or text is None:
        return False
    # Remove non-alphanumeric characters and convert to lowercase
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    # Check if the string equals its reverse
    return clean_text == clean_text[::-1]

def main():
    """
    Entry point for testing palindrome functionality.
    Prompts the user for input and prints whether it is a palindrome.
    """
    test_string = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(test_string):
        print(f"'{test_string}' is a palindrome!")
    else:
        print(f"'{test_string}' is not a palindrome.")

if __name__ == "__main__":
    main()