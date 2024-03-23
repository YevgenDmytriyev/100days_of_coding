alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encoded_text = ''
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + shift) % 26  # Ensure we stay within the alphabet range
            encoded_char = alphabet[shifted_index]
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text 
  #TODO-2: Inside the encrypt function, shift each letter of the text #forwards in the alphabet by the shift amount and print the encrypted text.
  #e.g. 
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
result = encrypt(text, shift)
print(f"The encoded text is: {result}")