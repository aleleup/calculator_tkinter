import tkinter as tk
from functions import set_numbers
set_numbers = set_numbers.set_numbers

def show_sym(button_frame, numbers_sym_array, operation_history_array, sym):
    btn_dot = tk.Button(button_frame, text='.', font=("Arial", 20),  command=lambda n='.':set_numbers(n, numbers_sym_array, operation_history_array, sym))
    btn_dot.grid(row=3, column=0, sticky="news")
    btn_equal = tk.Button(button_frame, text='=', font=("Arial", 20),  command=lambda n='=':set_numbers(n, numbers_sym_array, operation_history_array, sym))
    btn_equal.grid(row=3, column=2, sticky="news")

    btn_plus = tk.Button(button_frame, text='+', font=("Arial", 20),  command=lambda n='+':set_numbers(n, numbers_sym_array, operation_history_array, sym))
    btn_plus.grid(row=0, column=4, sticky="news")
    minus = tk.Button(button_frame, text='-', font=("Arial", 20),  command=lambda n='-':set_numbers(n, numbers_sym_array, operation_history_array, sym))
    minus.grid(row=1, column=4, sticky="news")
    times = tk.Button(button_frame, text='*', font=("Arial", 20),  command=lambda n='*':set_numbers(n, numbers_sym_array, operation_history_array, sym))
    times.grid(row=2, column=4, sticky="news")
    devided = tk.Button(button_frame, text='/', font=("Arial", 20),  command=lambda n='/':set_numbers(n, numbers_sym_array, operation_history_array, sym))
    devided.grid(row=3, column=4, sticky="news")