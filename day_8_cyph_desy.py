alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
  cipher_text = ''
  for char in plain_text:
      if char in alphabet:
          index = alphabet.index(char)
          shifted_index = (index + shift) % 26  # Ensure we stay within the alphabet range
          encoded_char = alphabet[shifted_index]
          cipher_text += encoded_char  # Handle non-alphabetic characters
      else:
          cipher_text += char
  return cipher_text
  
def decrypt(text, shift):
  decipher_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      back_position = position - shift
      decipher_text += alphabet[back_position]
    else:
      decipher_text += letter  # Handle non-alphabetic characters
  return decipher_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == 'encode':
            result = encrypt(text, shift)
            print(f"The encoded text is {result}")
        else:
            result = decrypt(text, shift)
            print(f"The decoded text is {result}")
        break
    else:
        print('Wrong choice, please try again')
