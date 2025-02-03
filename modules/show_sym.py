import tkinter as tk
from functions import set_numbers
set_numbers = set_numbers.set_numbers

def show_sym(button_frame, numbers_sym_array, operation_history_array, sym1, sym2, display_text):
    btn_dot = tk.Button(button_frame, text='.', font=("Arial", 20),  command=lambda n='.':set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text))
    btn_dot.grid(row=3, column=0, sticky="news")
    btn_equal = tk.Button(button_frame, text='=', font=("Arial", 20),  command=lambda n='=':set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text))
    btn_equal.grid(row=3, column=2, sticky="news")
   
    for element in sym1:
        if element == "=":
            continue
        btn = tk.Button(button_frame, text=element, font=("Arial", 20),  command=lambda n=element:set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text))
        btn.grid(row=sym1.index(element), column=4, sticky="news")

    for element in sym2:
        btn = tk.Button(button_frame, text=element, font=("Arial", 20),  command=lambda n=element:set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text))
        btn.grid(row=sym2.index(element), column=5, sticky="news")