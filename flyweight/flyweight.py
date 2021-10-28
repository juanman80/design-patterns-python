class Word:
    def __init__(self, text):
        self.text = text
        self.capitalize = False

    def __str__(self):
        return self.text.upper() if self.capitalize else self.text


class Sentence(list):
    separator = ' '
    def __init__(self, plain_text):
        for text in plain_text.split(self.separator):
            self.append(Word(text))

    def __str__(self):
        return self.separator.join(str(w) for w in self)

if __name__ == "__main__":
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)  # writes "hello WORLD"