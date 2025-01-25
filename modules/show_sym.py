import tkinter as tk
from functions import set_numbers
set_numbers = set_numbers.set_numbers

def show_sym(button_frame, numbers_sym_array, operation_history_array, sym, display_text):
    btn_dot = tk.Button(button_frame, text='.', font=("Arial", 20),  command=lambda n='.':set_numbers(n, numbers_sym_array, operation_history_array, sym, display_text))
    btn_dot.grid(row=3, column=0, sticky="news")
    btn_equal = tk.Button(button_frame, text='=', font=("Arial", 20),  command=lambda n='=':set_numbers(n, numbers_sym_array, operation_history_array, sym, display_text))
    btn_equal.grid(row=3, column=2, sticky="news")
    # btn_left_parenthesis = tk.Button(button_frame, text='(', font=("Arial", 20),  command=lambda n='(':set_numbers(n, numbers_sym_array, operation_history_array, sym, display_text))
    # btn_left_parenthesis.grid(row=4, column=2, sticky="news")
    # btn_right_parenthesis = tk.Button(button_frame, text=')', font=("Arial", 20),  command=lambda n=')':set_numbers(n, numbers_sym_array, operation_history_array, sym, display_text))
    # btn_right_parenthesis.grid(row=4, column=3, sticky="news")
    for element in sym:
        if element == "=":
            continue
        btn = tk.Button(button_frame, text=element, font=("Arial", 20),  command=lambda n=element:set_numbers(n, numbers_sym_array, operation_history_array, sym, display_text))
        btn.grid(row=sym.index(element), column=4, sticky="news")