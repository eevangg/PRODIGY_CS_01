def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                if mode == 'E':   
                    shifted = chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    shifted = chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                if mode == 'E':   
                    shifted = chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    shifted = chr((ord(char) - 65 - shift) % 26 + 65)
            
            result += shifted
        else:
            result += char
    return result

def main():
    choice = input("Do you want to perform encryption or decryption? (E/D): ")
    if choice == 'E':
        text = input("Input the text you want to encrypt: ")
    elif choice == 'D':
        text = input("Input the text you want to decrypt: ")
    else:
        print("Invalid input. Terminating program...")
        return
    
    shift = int(input("Enter a positive shift value: "))
    print("Original text: " + text)
    print("New text: " + caesar_cipher(text, shift, choice))

if __name__ == "__main__":
    main()