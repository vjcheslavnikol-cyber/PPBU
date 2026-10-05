from tkinter import *
from tkinter import ttk

def answer(event):
    answ = num.get().strip()
    result.configure(text=answ)


root = Tk() # window
root.title('Старт')
WIDTH = root.winfo_screenwidth() # получим ширину экрана
HEIGHT = root.winfo_screenheight() # получим высоту экрана

X = 400
Y = 500

root.geometry(f'{X}x{Y}+{WIDTH // 2 + 400}+'
              f'{HEIGHT // 2 - Y // 2 - 25}')
# root.geometry('300x300')


# ttk.Style().configure('My.TButton',
#                        font='Arial 12',
#                        foreground='red',
#                       padding=10,
#                       background="green"
#                        )

prompt = ttk.Label(text='Введите значение', style='My.TLabel')
prompt.pack()

num = Entry(width=10)
num.pack(pady=10)

border_frame = Frame(
    root,
    highlightbackground="black",
    highlightthickness=5,
    bd=0
)
border_frame.pack(pady=20) # Кнопка внутри рамки
# Кнопка внутри рамки
btn = ttk.Button(border_frame, text='Ответ', style='My.TButton')
btn.pack()

result = Label(text='   ', font='Arial 15', bg='lightgray')
result.pack(pady=10)



num.bind('<Return>', answer)


root.mainloop()