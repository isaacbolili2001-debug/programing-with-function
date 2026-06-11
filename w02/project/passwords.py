
# Checking if my text files exist on my laptop before the program opens it.

import os

# declaring Global Scope variables
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

"""This is the main function, inside of it, i put all functions possible for this program, and i called them"""

def main():
    """this is a prompt message to explain to the user what to do."""
    print("\n welcome to the Password Strength Checker")
    
    while True:
        password_test = input("\nEnter a password to test (or 'q' to quit): ") 
        if password_test.lower() == "q":
            print("Goodbye!")
            break
        strength = password_strength(password_test)
        print(f"Password Strength: {strength}")

def word_in_file(word, filename, case_sensitive=False):
    if not os.path.exists(filename):
        return False
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_word = line.strip()
            if case_sensitive:
                if clean_word == word:
                    return True
            else:
                if clean_word.lower() == word.lower():
                    return True
    return False
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
        
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
        
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
        
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
        
    return 1 + word_complexity(password)

if __name__ == "__main__":
    main()