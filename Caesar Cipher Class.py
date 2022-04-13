from string import ascii_lowercase

class CaesarCypher:
    def __init__(self, enter_word, shift):
        self.enter_word = enter_word
        self.shift = shift

    def encode(self):
        new_word = []
        for i in range(len(self.enter_word)):
            if ascii_lowercase.index(self.enter_word[i]) + self.shift > 25:
                new_word.append(ascii_lowercase[self.shift + 24 - ascii_lowercase.index(self.enter_word[i])])
            else:
                index = ascii_lowercase.index(self.enter_word[i])
                new_word.append(ascii_lowercase[index + self.shift])
                new_word_string = ('').join(new_word)
        # print("The encoded word is ", new_word, end='')
        return new_word_string

    def decode(self):
        new_word = []
        for i in range(len(self.enter_word)):
            if ascii_lowercase.index(self.enter_word[i]) - self.shift < 0:
                new_word.append(ascii_lowercase[ascii_lowercase.index(self.enter_word[i]) - self.shift + 26])
            else:
                index = ascii_lowercase.index(self.enter_word[i])
                new_word.append(ascii_lowercase[index - self.shift])
                new_word_string = ('').join(new_word)
        # print("The original word was ", ('').join(new_word), end='')
        return new_word_string

caesar_cipher = CaesarCypher("", 1)
print(caesar_cipher.decode())