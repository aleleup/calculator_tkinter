import tkinter as tk
from functions import set_numbers
set_numbers = set_numbers.set_numbers

def show_sym(button_frame, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list):
    btn_dot = tk.Button(button_frame, text='.', font=("Arial", 20),  command=lambda n='.':set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
    btn_dot.grid(row=3, column=0, sticky="news")

    btn_equal = tk.Button(button_frame, text='=', font=("Arial", 20),  command=lambda n='=':set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
    btn_equal.grid(row=3, column=2, sticky="news")

    btn_delete = tk.Button(button_frame, text='del', font=("Arial", 20),  command=lambda n='del':set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
    btn_delete.grid(row=0, column=4, sticky="news")

    btn_clear = tk.Button(button_frame, text='clr', font=("Arial", 20),  command=lambda n='clr':set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
    btn_clear.grid(row=1, column=4, sticky="news")

    for element in sym1:
        if element == "=":
            continue
        btn = tk.Button(button_frame, text=element, font=("Arial", 20),  command=lambda n=element:set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
        btn.grid(row=sym1.index(element), column=5, sticky="news")

    for element in sym2:
        btn = tk.Button(button_frame, text=element, font=("Arial", 20),  command=lambda n=element:set_numbers(n, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
        btn.grid(row=sym2.index(element), column=6, sticky="news")