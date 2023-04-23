import tkinter as tk
import threading
import requests
from bs4 import BeautifulSoup
import re


# def __init__(self):
#     self.gold_price_in_egypt_in_egp = get_gold_price_in_egypt()
#     self.global_gold_price_in_usd = get_global_gold_price_in_usd()
#     self.usd_price_in_black_market = gold_price_in_egypt_in_egp / global_gold_price_in_usd

def get_gold_price_in_egypt():
    url = 'https://www.masrawy.com/gold'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    curr_gold_details = soup.find('div', class_='currGoldDtls')
    gram_price_in_egypt = 0
    if curr_gold_details is not None:
        numbers = re.findall(r'\d+\.\d+|\d+', curr_gold_details.text.strip())
        gram_price_in_egypt = float(numbers[1])
    else:
        print('Element not found.')
    return gram_price_in_egypt


def get_global_gold_price_in_usd():
    url = 'https://www.arabictrader.com/ar/commodities/gold-price/%D8%B3%D8%B9%D8%B1-%D8%A7%D9%84%D8%B0%D9%87%D8%A8'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    curr_gold_details = soup.find('div', class_='table-responsive')
    gram_price_in_usd = 0
    if curr_gold_details is not None:
        numbers = re.findall(r'\d+\.\d+|\d+', curr_gold_details.text.strip())
        gram_price_in_usd = float(numbers[3])
    else:
        print('Element not found.')
    return gram_price_in_usd



def calculate_total_assets(gold , usd , egp , stocks_assets):
    return float(gold or 0 )*gold_price_in_egypt_in_egp + float(usd or 0) *usd_price_in_black_market +float(egp or 0) +float(stocks_assets or 0)

    

def submit():
    # Create loading message window
    loading_window = tk.Toplevel(window)
    loading_window.title("Loading...")
    loading_label = tk.Label(loading_window, text="Calculating...")
    loading_label.pack()

    # Get input values
    gold_values = gold.get()
    stocks_values = stocks.get()
    usd_values = usd.get()
    egp_values = egp.get()
    
    # Do something with the input values, e.g. print them
    total_assets = calculate_total_assets(gold_values,usd_values,egp_values , stocks_values)

    # Update output with calculated result
    output.delete('1.0', tk.END) # clear the previous content
    output.insert(tk.END, f"Total assets: {total_assets:,}")
    output.tag_configure("center", justify='center')
    output.tag_add("center", "1.0", "end")

    # Destroy loading message window
    loading_window.destroy()



gold_price_in_egypt_in_egp = get_gold_price_in_egypt()
global_gold_price_in_usd = get_global_gold_price_in_usd()
usd_price_in_black_market = gold_price_in_egypt_in_egp / global_gold_price_in_usd

window = tk.Tk()
window.title("Input Form")
window.geometry("600x450")

tk.Label(window, text="Gold:").grid(row=0, column=0, padx=10, pady=10, sticky="W")
gold = tk.Entry(window)
gold.grid(row=0, column=1, sticky="E")

tk.Label(window, text="Stocks:").grid(row=1, column=0, padx=10, pady=10, sticky="W")
stocks = tk.Entry(window)
stocks.grid(row=1, column=1, sticky="E")

tk.Label(window, text="USD:").grid(row=2, column=0, padx=10, pady=10, sticky="W")
usd = tk.Entry(window)
usd.grid(row=2, column=1, sticky="E")

tk.Label(window, text="EGP:").grid(row=3, column=0, padx=10, pady=10, sticky="W")
egp = tk.Entry(window)
egp.grid(row=3, column=1, sticky="E")

submit_button = tk.Button(window, text="Submit", command=submit)






submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

output = tk.Text(window, height=5, width=50)
output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
