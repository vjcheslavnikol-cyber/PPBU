from tkinter import *


def answer(event=None):
    answ = num.get().strip()
    result.configure(text=answ)


root = Tk() # window
root.title('Старт')
WIDTH = root.winfo_screenwidth() # получим ширину экрана
HEIGHT = root.winfo_screenheight() # получим высоту экрана
# print(WIDTH, HEIGHT)
X = 300
Y = 140

root.geometry(f'{X}x{Y}+{WIDTH // 2 - X // 2}+'
              f'{HEIGHT // 2 - Y // 2 - 25}')
# root.geometry('300x300')

prompt = Label(text='Введите значение', font='Arial 15')
prompt.pack()
# prompt.pack() # по умолчанию сверху
# prompt.pack(side=TOP)
# prompt.pack(side=LEFT)
# prompt.pack(side=BOTTOM)
# prompt.pack(side=RIGHT)
num = Entry(width=5, font='Arial 12', justify='center')
num.pack()

result = Label(text='   ', font='Arial 15', bg='lightgray')
result.pack(pady=10)

btn = Button(text='Выполнить', command=answer)
btn.pack()


num.bind('<Return>', answer)


root.mainloop()