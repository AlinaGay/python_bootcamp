class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        original_text = list(original_text.split(" "))
        ciphered_text = []
        for word in original_text:
            ciphered_word = ''
            for char in word:
                char = char.lower()
                if char in [',', '.', '!', ':', ';', '"', '(', ')']:
                    shifted_letter = char
                else:
                    shifted_letter_position = self.alphabet.index(char) + shift
                    if shifted_letter_position > (len(self.alphabet) - 1):
                        shifted_letter_position = shifted_letter_position % len(self.alphabet)
                    shifted_letter = self.alphabet[shifted_letter_position]
                print('char', char, 'shifted_letter', shifted_letter)    
                ciphered_word += shifted_letter
            ciphered_text.append(ciphered_word)
        return ' '.join(ciphered_text)

    def decipher(self, cipher_text, shift):
        cipher_text = list(cipher_text.split(" "))
        original_text = []
        for word in cipher_text:
            original_word = ''
            for char in word:
                char = char.lower()
                if char in [',', '.', '!', ':', ';', '"', '(', ')', '—']:
                    original_letter = char
                else:
                    original_letter_position = self.alphabet.index(char) - shift
                    if original_letter_position < 0:
                        original_letter_position = len(self.alphabet) + original_letter_position
                    elif original_letter_position > (len(self.alphabet) - 1):
                        original_letter_position = original_letter_position % len(self.alphabet)    
                    original_letter = self.alphabet[original_letter_position]
                    print('char', char, 'original_letter', original_letter)
                original_word += original_letter
            original_text.append(original_word)
        return ' '.join(original_text)


cipher_master = CipherMaster()
""" print(cipher_master.cipher(
    original_text='Пришло ревью в шифрованном виде. Кажется, нас расскрыли!',
    shift=2
)) """
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))

#print('сткънр тждюа д ъкцтрдвппро дкёж. мвижфуб, пву твуумтэнк!' == 'сткънр тждюа д ъкцтрдвппро дкёж. мвижфуб, пву твуумтэнк!')