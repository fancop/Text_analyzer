"""
скачать текст
загрузить ТХТ файл
ТОП 10/20 глаголов/существительных/прилагательных в этом тексте
создать картинку - облако слов
"""

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            text = file.read()
            print(text)

reader = FileReader("text.txt")
reader.read_file()