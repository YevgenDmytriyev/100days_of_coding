def caesar(text, shift, direction):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  cipher_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode": 
        new_position = (position + shift) % 26
      elif direction == "decode":
        new_position = (position - shift) % len(alphabet)
      cipher_text += alphabet[new_position]
    else:
      cipher_text += letter  # Handle non-alphabetic characters
  return cipher_text

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

result = caesar(text, shift, direction)
print(f"The result is {result}")
