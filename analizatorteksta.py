import os
from typing import NoReturn
from string import punctuation
from collections import Counter
import re
import pymorphy3
import matplotlib.pyplot as plt
import wordcloud as wc


"""
скачать текст
загрузить ТХТ файл
ТОП 10/20 глаголов/существительных/прилагательных в этом тексте
создать картинку - облако слов
"""

class TextAnalyzer:
    def __init__(self, file_name="text.txt", mode="r", encoding="UTF-8", pos_list=["VERB", "NOUN"],
                 wordcloud_width=800, wordcloud_height=800, wordcloud_background_color="white",
                 wordcloud_min_font_size=10) -> None:
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.pos_list = pos_list
        self.wordcloud_width = wordcloud_width
        self.wordcloud_height = wordcloud_height
        self.wordcloud_background_color = wordcloud_background_color
        self.wordcloud_min_font_size = wordcloud_min_font_size
        self.read_file()
        self.check_empty_file()
        self.prepare_text()
        self.sorting_words()
        self.generate_wordcloud()
        self.save_wordcloud_image()
        self.display_wordcloud()
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
        self.words = re.findall(r'\b[\w-]+\b', self.text)

    def sorting_words(self) -> list:
        morph = pymorphy3.MorphAnalyzer()
        self.words_by_pos = []

        for word in self.words:
            parsed_word = morph.parse(word)[0]
            pos = parsed_word.tag.POS
            if pos in self.pos_list:
                self.words_by_pos.append(parsed_word.normal_form)

        self.top_words = Counter(self.words_by_pos).most_common(10)

    def generate_wordcloud(self) -> None:
        wordcloud_image = wc.WordCloud(width=self.wordcloud_width, height=self.wordcloud_height,
                                       background_color=self.wordcloud_background_color,
                                       min_font_size=self.wordcloud_min_font_size).generate(self.top_words)
        image = wordcloud_image.to_image()

        self.save_wordcloud_image(image)
        self.display_wordcloud(wordcloud_image)

    def save_wordcloud_image(self, image):
        """ Сохраняет облако слов в файл wordcloud.png """
        if not os.access(os.path.dirname(os.path.abspath(__file__)), os.W_OK):
            raise Exception("Ошибка: не удается записать wordcloud.png")

        image.save("wordcloud.png")

    def display_wordcloud(self, wordcloud_image):
        """ Отображает облако слов """
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud_image)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()

    def print_text(self) -> None:
        """ Выводит строку текста на экран """
        print(self.words_by_pos)


TextAnalyzer()