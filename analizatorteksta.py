"""
скачать текст
загрузить ТХТ файл
ТОП 10/20 глаголов/существительных/прилагательных в этом тексте
создать картинку - облако слов
"""

class TextAnalyzer:
    def __init__(self, file_name="text.txt", mode="r", encoding="UTF-8"):
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.read_file()
        self.prepare_text()
        self.print_text()

    def read_file(self):
        """ Пытается открыть файл и считать его в строку """
        try:
            with open(self.file_name, self.mode, encoding=self.encoding) as file:
                self.content = file
                self.text = self.content.read()
        except FileNotFoundError:
            raise Exception(f"Файл {self.file_name} не найден!")
        
        if not self.text:
            raise Exception("Файл пустой!")

    def prepare_text(self):
        """ Приводит текст к нижнему регистру """
        self.text = self.text.lower()

    def print_text(self):
        """ Выводит строку текста на экран """
        print(self.text)

TextAnalyzer()