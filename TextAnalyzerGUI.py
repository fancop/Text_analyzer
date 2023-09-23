import tkinter as tk
from tkinter import colorchooser, filedialog
import TextAnalyzer
import tkinter.messagebox as messagebox

color = ""  
file_path = ""

def show_color_picker():
    global color
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1]:
        print("Выбранный цвет:", color[1])
        canvas.itemconfig(color_square, fill=color[1])
    else:
        print("Цвет не выбран!")

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=[("Text Files", "*.txt")])
    if file_path:
        print("Выбранный файл:", file_path)

def run():
    if not file_path:
        messagebox.showerror("Ошибка", "Файл не выбран!")
        return
    if not color:
        messagebox.showerror("Ошибка", "Цвет не выбран!")
        return
    
    pos_list = []
    if noun_var.get():
        pos_list.append("NOUN")
    if verb_var.get():
        pos_list.append("VERB")
    if adjective_var.get():
        pos_list.append("ADJS")
    if adverb_var.get():
        pos_list.append("ADVB")
    
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
adverb_var = tk.BooleanVar()
cb_noun = tk.Checkbutton(window, text="Включить Существительные", font=("Bahnschrift", 19), variable=noun_var)
cb_verb = tk.Checkbutton(window, text="Включить Глаголы", font=("Bahnschrift", 19), variable=verb_var)
cd_adjective = tk.Checkbutton(window, text="Включить прилагательные", font=("Bahnschrift", 19), variable=adjective_var)
cd_adverb = tk.Checkbutton(window, text="Включить наречия", font=("Bahnschrift", 19), variable=adverb_var)
label2 = tk.Label(window, text="Ширина:", font=("Bahnschrift", 19))
label3 = tk.Label(window, text="Высота:", font=("Bahnschrift", 19))
button = tk.Button(window, font=("Bahnschrift", 17), text="сделать вордклауд", command=run)
button2 = tk.Button(window, font=("Bahnschrift", 17), text="выбрать цвет", command=show_color_picker)
button3 = tk.Button(window, font=("Bahnschrift", 17), text="выбрать файл", command=select_file)
entry = tk.Entry(window, font=("Bahnschrift", 18))
entry2 = tk.Entry(window, font=("Bahnschrift", 18))
entry3 = tk.Entry(window, font=("Bahnschrift", 18))
canvas = tk.Canvas(window, width=50, height=50)
color_square = canvas.create_rectangle(0, 0, 50, 50, fill="white")

label.grid(row=0, column=0, padx=6, pady=6)
entry.grid(row=1, column=0, padx=6, pady=6)
button3.grid(row=2, column=0, padx=6, pady=6)
button2.grid(row=3, column=0, padx=6, pady=6)
canvas.grid(row=3, column=1, padx=6, pady=6)
label2.grid(row=4, column=0, padx=6, pady=6)
entry2.grid(row=5, column=0, padx=6, pady=6)
label3.grid(row=6, column=0, padx=6, pady=6)
entry3.grid(row=7, column=0, padx=6, pady=6)
cb_noun.grid(row=8, column=0)  
cb_verb.grid(row=8, column=1)  
cd_adjective.grid(row=9, column=0)
cd_adverb.grid(row=9, column=1)
button.grid(row=10, column=0, columnspan=2, padx=6, pady=6)

window.mainloop()