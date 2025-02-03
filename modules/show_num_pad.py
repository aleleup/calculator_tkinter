import tkinter as tk
from functions import set_numbers
from functions.utilities import column, row

row, column, set_numbers = [row.row, column.column, set_numbers.set_numbers]

def show_num_pad(button_frame, numbers_sym_array, operation_history_array, sym1, sym2, display_text):
    for i in range(10):
        number_button = tk.Button(
            button_frame,
            text=i,
            font=("Arial", 20), 
            command=lambda num=f'{i}': set_numbers(num, numbers_sym_array, operation_history_array, sym1, sym2, display_text))
        number_button.grid(row=row(i), column=column(i))





