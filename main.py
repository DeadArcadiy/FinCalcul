import tkinter
from tkinter import ttk
from decimal import *
import re
from controller import Controller


if __name__ == '__main__':
    top = tkinter.Tk()
    top.geometry("500x300")
    num = 2

    label = ttk.Label(text="Denis Borychev 12 group")
    label.pack(anchor=tkinter.N)

    cntrl = Controller(num,top)

    plus_button = tkinter.Button(top, text="Plus", command=cntrl.plus_callback,width=7,height=2)
    plus_button.pack(anchor=tkinter.N, padx=1, pady=1)
    
    minus_button = tkinter.Button(top, text="Minus", command=cntrl.minus_callback,width=7,height=2)
    minus_button.pack(anchor=tkinter.N, padx=1, pady=1)

    mupytiply_buuton = tkinter.Button(top, text="Multiply", command=cntrl.mupytiply_callback,width=7,height=2)
    mupytiply_buuton.pack(anchor=tkinter.N, padx=1, pady=1)

    divison_buuton = tkinter.Button(top, text="Divide", command=cntrl.divide_callback,width=7,height=2)
    divison_buuton.pack(anchor=tkinter.N, padx=1, pady=1)
    
    cntrl.result_display.pack(anchor=tkinter.N, padx=1, pady=1)

    top.resizable(False, False) 
    top.mainloop()
