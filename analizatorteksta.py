from typing import NoReturn
from string import punctuation


"""
скачать текст
загрузить ТХТ файл
ТОП 10/20 глаголов/существительных/прилагательных в этом тексте
создать картинку - облако слов
"""

class TextAnalyzer:
    def __init__(self, file_name="text.txt", mode="r", encoding="UTF-8") -> None:
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.read_file()
        self.check_empty_file()
        self.prepare_text()
        self.print_text()

    def read_file(self) -> None | NoReturn:
        """ Пытается открыть файл и считать его в строку """
        try:
            with open(self.file_name, self.mode, encoding=self.encoding) as file:
                self.content = file
                self.text = self.content.read()
        except FileNotFoundError:
            raise Exception(f"Файл {self.file_name} не найден!")

    def check_empty_file(self) -> None | NoReturn:
        """ проверяет пустой ли файл """
        if not self.text:
            raise RuntimeError(f"Файл {self.file_name} пустой!")

    def prepare_text(self):
        """ Приводит текст к нижнему регистру и убирает все лишние знаки препинания """
        self.text = self.text.lower()
        self.words_unclean = self.text.split()
        self.words_clean = []
        for i in range(len(self.words_unclean)):
            for s in punctuation + "—":
                new_word = self.words_unclean[i].replace(s, "")
                if new_word:
                    self.words_clean.append(new_word)
        self.words_clean = list(filter(None, self.words_clean))

    def print_text(self) -> None:
        """ Выводит строку текста на экран """
        print(self.words_clean)
        print(f"В этом тексте {len(self.words_clean)} слов")

TextAnalyzer()