"""
скачать текст
загрузить ТХТ файл
ТОП 10/20 глаголов/существительных/прилагательных в этом тексте
создать картинку - облако слов
"""

class TextAnalyzer:
    def __init__(self, file="text.txt", mode="r", encoding="UTF-8"):
        self.file = file
        self.mode = mode
        self.encoding = encoding
        self.open_file()
        self.make_text()
        self.print_text()

    def open_file(self):
        self.content = open(self.file, self.mode, encoding=self.encoding)

    def make_text(self):
        self.text = "".join(self.content)

    def print_text(self):
        print(self.text)

TextAnalyzer()