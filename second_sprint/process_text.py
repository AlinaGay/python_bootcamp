class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        text = text.lower()
        new_text = ''
        for letter in text:
            if letter in self.alphabet:
                if is_encrypt:
                    new_letter_position = self.alphabet.index(letter) + shift
                else:
                    new_letter_position = self.alphabet.index(letter) - shift  

                if new_letter_position > len(self.alphabet) - 1:
                    new_letter_position = new_letter_position % len(self.alphabet)
                elif new_letter_position < 0:
                    new_letter_position = len(self.alphabet) + new_letter_position
                new_letter = self.alphabet[new_letter_position]
            else:
                new_letter = letter
            new_text += new_letter
        return new_text


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 