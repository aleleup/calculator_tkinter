import tkinter as tk
from functions import set_numbers
from functions.utilities import column, row

row, column, set_numbers = [row.row, column.column, set_numbers.set_numbers]

def show_num_pad(button_frame, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list):
    for i in range(10):
        number_button = tk.Button(
            button_frame,
            text=i,
            font=("Arial", 20), 
            command=lambda num=f'{i}': set_numbers(num, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
        number_button.grid(row=row(i), column=column(i))


    button_pi = tk.Button(
            button_frame,
            text='π',
            font=("Arial", 20), command=lambda num='π': set_numbers(num, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
    
    button_pi.grid(row=2, column=4)

    button_e = tk.Button(
            button_frame,
            text='e',
            font=("Arial", 20), command=lambda num='e': set_numbers(num, numbers_sym_array, operation_history_array, sym1, sym2, display_text, result_list))
    button_e.grid(row=3, column=4)