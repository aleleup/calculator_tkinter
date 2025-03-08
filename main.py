import tkinter as tk
from modules import show_num_pad,  show_sym

show_num_pad, show_sym = [show_num_pad.show_num_pad, show_sym.show_sym]
        

def render_calculator():
    math_sym1 = ["+", "-", "*", "/", 'x', "=", ]
    math_sym2 = ["(", ")", "^", "^1/", "!"]
    result_list = []
    numbers_sym_array = []
    operation_history_array = []
    root = tk.Tk()
    root.geometry("600x400")
    
    display_text = tk.StringVar()
    display_text.set(operation_history_array)
    numbers_renderer = tk.Label(root, font=("Arial", 20), textvariable=display_text, width=80, height=2, anchor="center")
    numbers_renderer.pack()
    button_frame = tk.Frame(root)
    for i in range(4):
        button_frame.columnconfigure(i, weight=1)
   
    show_num_pad(button_frame, numbers_sym_array, operation_history_array, math_sym1, math_sym2,display_text, result_list)
    show_sym(button_frame, numbers_sym_array, operation_history_array, math_sym1, math_sym2,display_text, result_list)
    button_frame.pack()

    root.mainloop()


render_calculator()
