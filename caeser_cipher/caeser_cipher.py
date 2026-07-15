def encrypt(text, shift):
    if not text:
        return ""
    result = ""
    
    for letter in text:
        if not letter.isalpha():
            result += letter
        elif letter.isupper():
            new_letter = (ord(letter)- ord('A') + shift) % 26 + ord('A')
            result += chr(new_letter)
        elif letter.islower():
            new_letter = (ord(letter)- ord('a') + shift) % 26 + ord('a')
            result += chr(new_letter) 
    return result

secret_message = input("Enter your message: ")
encrypted_message = encrypt(secret_message, 3)

print(encrypted_message)

