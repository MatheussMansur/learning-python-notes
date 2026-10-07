# Exercise: check if a word typed by the user is a palindrome


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


def main():
    user_input = input("Enter a WORD to be tested as a palindrome: ")
    if is_palindrome(user_input):
        print(user_input + " is a palindrome!")
    else:
        print(user_input + " is NOT a palindrome!")


if __name__ == "__main__":
    main()
