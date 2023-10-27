import tkinter
from tkinter import ttk
from decimal import *
import re
from controller import Controller


if __name__ == '__main__':
    top = tkinter.Tk()
    top.geometry("300x400")
    num = 4

    label = ttk.Label(text="Denis Borychev 12 group")
    label.pack(anchor=tkinter.N)

    cntrl = Controller(num,top)

    divison_buuton = tkinter.Button(top, text="Calculate", command=cntrl.calculate_callback,width=7,height=2)
    divison_buuton.pack(anchor=tkinter.N, padx=1, pady=1)
    
    cntrl.result_display.pack(anchor=tkinter.N, padx=1, pady=1)

    top.resizable(False, False) 
    top.mainloop()
