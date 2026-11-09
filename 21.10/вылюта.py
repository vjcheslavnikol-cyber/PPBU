from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json
import pprint



def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def update_base_label_1(event):
    code = base_combobox_1.get()
    name = currencies[code]
    base_label_1.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    # code = combobox.get()
    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                # currency_name  = currency[code]
                mb.showinfo('Курс обмена',
                            f'Курс к {base}: {exchange_rate:.2f} {target} за 1 {base}')
            else:
                mb.showinfo('Ошибка', f'Валюта {target_code} не найденна')
        except Exception as er:
            mb.showerror('Ошибка', er)
    else:
        mb.showwarning('Внимание', 'Введите код валюты')



currencies = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

root = Tk()
root.title('Курс обмена валют к USD')
root.geometry('360x280')

Label(root, text='Базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)

base_label = ttk.Label()
base_label.pack()
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

Label(root, text='Вторая базовая валюта').pack()
base_combobox_1 = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox_1.pack(pady=3, padx=10)

base_label_1 = ttk.Label()
base_label_1.pack()
base_combobox_1.bind('<<ComboboxSelected>>', update_base_label_1)

Label(root, text='Целевая валюта', ).pack(padx=10)

target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack()


Button(text='Плучить курс обмена к доллару', command=exchange).pack(pady=10, padx=10)



root.mainloop()

# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p.pprint(data)

