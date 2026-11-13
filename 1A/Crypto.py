from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
from PIL import Image
import json




def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def exchange():
    base_code = base_combobox.get().strip()
    coin_id = crypto_id[base_code]
    # print(coin_id)
    if coin_id:
        if base_code:
            try:
                response = requests.get(f'https://api.coinlore.net/api/ticker/?id={coin_id}')
                response.raise_for_status()
                data = response.json()
                for item in data:
                    if item['symbol'] == base_code:
                        pr = item['price_usd']
                        target_label.configure(text=f'{pr}')
                return None
            except Exception as er:
                mb.showerror('Ошибка', er)
        else:
            mb.showwarning('Внимание', 'Введите код валюты')
    else:
        mb.showwarning('Внимание', 'Введите код валюты')


currencies = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'XRP': 'XRP',
    'SOL': 'Solana',
    'TRX': 'TRON',
    'ZEC': 'Zcash',
    'DOGE': 'Dogecoin',
    'XMR': 'Monero',
    'ADA': 'Cardano',
    'USDT': 'Tether',
}
crypto_id = {
    'BTC': '90',
    'ETH': '80',
    'XRP': '58',
    'SOL': '48543',
    'TRX': '2713',
    'ZEC': '134',
    'DOGE': '2',
    'XMR': '28',
    'ADA': '257',
    'USDT': '518',
}

root = Tk()
root.title('Курс обмена криптовалют к USD')
root.geometry('360x280')
root.iconbitmap("Crypto.ico")

Label(root, text='Выберите криптовалюту').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
base_combobox.pack()
base_combobox.current(0)

base_label = ttk.Label()
base_label.config(text='Bitcoin', font='Arial 14')
base_label.pack(pady=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)



target_label = ttk.Label(text='', width=10, font='Arial 18', background='white', anchor='center', borderwidth=2, relief='groove')
target_label.pack(pady=10)


Button(text='Курс обмена к доллару США', command=exchange).pack(pady=10, padx=10)



root.mainloop()


