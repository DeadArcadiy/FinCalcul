import tkinter
from tkinter import ttk
from decimal import *


def getnums():
    return str(first_digit.get()).replace(',','.'),str(second_digit.get()).replace(',','.')


def change_output(result):
    result_display.config(state=tkinter.NORMAL)  
    result_display.delete(0, tkinter.END)
    result_display.insert(0, result)
    result_display.config(state=tkinter.DISABLED) 


def plusCallBack():
    a,b = getnums()
    try:
        change_output(Decimal(a) + Decimal(b))
    except:
        change_output("Something wrong!")


def minusCallBack():
    a,b = getnums()
    try:
        change_output(Decimal(a) - Decimal(b))
    except:
        change_output("Something wrong!")
    

if __name__ == '__main__':
    top = tkinter.Tk()
    top.geometry("500x300")

    label = ttk.Label(text="Denis Borychev 12 group")
    label.pack(anchor=tkinter.N)

    first_digit = tkinter.ttk.Entry(top)
    first_digit.pack(anchor=tkinter.N, padx=8, pady=8)
    
    second_digit = tkinter.ttk.Entry(top)
    second_digit.pack(anchor=tkinter.N, padx=8, pady=8)
    
    plus_button = tkinter.Button(top, text="Plus", command=plusCallBack,width=7,height=2)
    plus_button.pack(anchor=tkinter.N, padx=8, pady=8)
    
    minus_button = tkinter.Button(top, text="Minus", command=minusCallBack,width=7,height=2)
    minus_button.pack(anchor=tkinter.N, padx=8, pady=8)
    
    result_display = tkinter.ttk.Entry(top, state=tkinter.DISABLED,text = 'Output')  # поле вывода с состоянием "только для чтения"
    result_display.pack(anchor=tkinter.N, padx=8, pady=8)

    top.resizable(False, False) 
    top.mainloop()
