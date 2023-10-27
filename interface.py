import tkinter as tk
from tkinter import ttk
from decimal import *
from param import *


class Inputs:
    def __init__(self, num, root) -> None:
        self.num = num
        self.fields = []
        self.radiobuttons = []
        self.operators = []
        self.rounding = tk.StringVar(value=roundings[0]["name"])
        for i in range(num):
            # Entry
            entry = ttk.Entry(root)
            entry.pack(pady=5, padx=10, fill='x', expand=True)
            self.fields.append(entry)
            
            # Radiobuttons for all inputs except for the last one
            if i < num - 1:
                self.operators.append(tk.StringVar(value=buttonsvalue[0]["name"]))
                rb_frame = ttk.Frame(root)
                rb_frame.pack(pady=5, padx=10, fill='x', expand=True)
                for val in buttonsvalue:   
                    rb = ttk.Radiobutton(rb_frame, value=val["name"], text=val["name"], variable=self.operators[i])
                    rb.pack(side=tk.LEFT, padx=5)
                    self.radiobuttons.append(rb)
            else:
                rb_frame = ttk.Frame(root)
                rb_frame.pack(pady=5, padx=10, fill='x', expand=True)
                for val in roundings:   
                    rb = ttk.Radiobutton(rb_frame, value=val["name"], text=val["name"], variable=self.rounding)
                    rb.pack(side=tk.LEFT, padx=5)
                    self.radiobuttons.append(rb)

    def get_values(self):
        values = [str(i.get()) for i in self.fields]
        return values  

    def get_operators(self):
        operators = [str(i.get()) for i in self.operators]
        return operators
    
    def get_roundings(self):
        return self.rounding.get()