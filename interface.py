import tkinter
from tkinter import ttk
from decimal import *

class Inputs:
    def __init__(self,num,root) -> None:
        self.num = num
        self.fields = []
        for i in range(num):
            self.fields.append(tkinter.ttk.Entry(root))
            self.fields[i].pack(anchor=tkinter.N, padx=1, pady=1)
    
    def getvalues(self):
        values = []
        for i in self.fields:
            values.append(str(i.get()))
        return values