import tkinter as tk
from functions import row, set_numbers, column

row, column, set_numbers = [row.row, column.column, set_numbers.set_numbers]

def show_num_pad(button_frame, numbers_sym_array, operation_history_array, sym):
    for i in range(10):
        number_button = tk.Button(
            button_frame,
            text=i,
            font=("Arial", 20), 
            command=lambda num=f'{i}': set_numbers(num, numbers_sym_array, operation_history_array, sym))
        number_button.grid(row=row(i), column=column(i))





