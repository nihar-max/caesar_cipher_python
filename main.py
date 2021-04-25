from logo import logo_caeser_cipher
print(logo_caeser_cipher)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

endgame  =  False
while not endgame:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26


    def ceaser(text, shift, direction):
        complete_word = ""
        for i in text:

            if i in alphabet:
                index = alphabet.index(i)
                if direction == "encode":
                    new_index = index + shift
                else:
                    new_index = index - shift
                new_word = alphabet[new_index]
                complete_word = complete_word + new_word
            else:
                complete_word = complete_word + i
        print(f"Here's the {direction}d result: {complete_word}")


    ceaser(text, shift, direction)


    user = input("Type Yes for continue or else Type no:")
    if user == "no":
        endgame = True
        print("GoodBye")
