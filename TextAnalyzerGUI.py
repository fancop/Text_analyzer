import tkinter as tk
from tkinter import colorchooser, filedialog
import TextAnalyzer

color = ""  
file_path = ""

def show_color_picker():
    global color
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1]:
        print("Выбранный цвет:", color[1])
    else:
        print("Цвет не выбран!")

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=[("Text Files", "*.txt")])
    if file_path:
        print("Выбранный файл:", file_path)

def run():
    pos_list = []
    if noun_var.get():
        pos_list.append("NOUN")
    if verb_var.get():
        pos_list.append("VERB")
    if adjective_var.get():
        pos_list.append("ADJECTIVE")
    
    TextAnalyzer.TextAnalyzer(
        file_name=file_path,
        pos_list=pos_list,
        num=int(entry.get()),
        background=color[1],
        width=int(entry2.get()),
        height=int(entry3.get())
    )

window = tk.Tk()
label = tk.Label(window, text="Сколько слов должно быть", font=("Bahnschrift", 19))
noun_var = tk.BooleanVar()
verb_var = tk.BooleanVar()
adjective_var = tk.BooleanVar()
cb_noun = tk.Checkbutton(window, text="Включить Существительные", font=("Bahnschrift", 19), variable=noun_var)
cb_verb = tk.Checkbutton(window, text="Включить Глаголы", font=("Bahnschrift", 19), variable=verb_var)
cd_adjective = tk.Checkbutton(window, text="Включить прилагательные", font=("Bahnschrift", 19), variable=adjective_var)
label2 = tk.Label(window, text="Ширина:", font=("Bahnschrift", 19))
label3 = tk.Label(window, text="Высота:", font=("Bahnschrift", 19))
button = tk.Button(window, font=("Bahnschrift", 17), text="сделать вордклауд", command=run)
button2 = tk.Button(window, font=("Bahnschrift", 17), text="выбрать цвет", command=show_color_picker)
button3 = tk.Button(window, font=("Bahnschrift", 17), text="выбрать файл", command=select_file)
entry = tk.Entry(window, font=("Bahnschrift", 18))
entry2 = tk.Entry(window, font=("Bahnschrift", 18))
entry3 = tk.Entry(window, font=("Bahnschrift", 18))

label.pack(anchor="nw", padx=6, pady=6)
button3.pack(anchor="nw", padx=6, pady=6)
entry.pack(anchor="nw", padx=6, pady=6)
button.pack(anchor="nw", padx=6, pady=6)
button2.pack(anchor="nw", padx=6, pady=6)
label2.pack(anchor="nw", padx=6, pady=6)
entry2.pack(anchor="nw", padx=6, pady=6)
label3.pack(anchor="nw", padx=6, pady=6)
entry3.pack(anchor="nw", padx=6, pady=6)
cb_noun.pack(anchor="nw", padx=6, pady=6)  
cb_verb.pack(anchor="nw", padx=6, pady=6)  
cd_adjective.pack(anchor="nw", padx=6, pady=6)

window.mainloop()