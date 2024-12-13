import tkinter as tk
from modules import show_num_pad,  show_sym
import sys
from dotenv import load_dotenv

x = load_dotenv("PYTHONDONTWRITEBYTECODE")
sys.dont_write_bytecode = True


show_num_pad, show_sym = [show_num_pad.show_num_pad, show_sym.show_sym]
        

def render_calculator():
    sym = ["+", "-", "*", "/", "="]
    numbers_sym_array = []
    operation_history_array = []
    root = tk.Tk()
    root.geometry("600x400")
    
    button_frame = tk.Frame(root)
    for i in range(4):
        button_frame.columnconfigure(i, weight=1)
   
    show_num_pad(button_frame, numbers_sym_array, operation_history_array, sym)
    show_sym(button_frame, numbers_sym_array, operation_history_array, sym)
    button_frame.pack()

    root.mainloop()


render_calculator()
