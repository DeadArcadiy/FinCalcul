import tkinter
from tkinter import ttk
from decimal import *
from calculator import Calculator
from interface import Inputs
import re

class Controller:
    def __init__(self,num,root) -> None:
        self.inputs = Inputs(num,root=root)
        self.result_display = tkinter.ttk.Entry(root, state=tkinter.DISABLED,text = 'Output')
        self.calcul = Calculator(num)

    def check(self, inputs):
        checked = []
        for num_str in inputs:
            num_str = str(num_str.replace(",", "."))
            if self.is_valid_number(num_str):
                number = str(num_str.replace(" ", ""))
                checked.append(str(number))
            else:
                print(num_str)
                return []
        return checked

    def is_valid_number(self, num_str):
        pattern = r"^-?\d+(?:\.\d+)?$|^-?\d{1,3}(?: \d{3})*(?:\.\d+)?$"
        return bool(re.match(pattern, num_str))

    def change_output(self,result):
        self.result_display.config(state=tkinter.NORMAL)  
        self.result_display.delete(0, tkinter.END)
        self.result_display.insert(0, result)
        self.result_display.config(state=tkinter.DISABLED) 

    def plus_callback(self):
        nums = self.check(self.inputs.getvalues())
        if len(nums) == 0:
            self.change_output("Something wrong!")
        else:
            try:
                self.change_output(self.calcul.plus(nums))
            except:
                self.change_output("Something wrong!")

    def mupytiply_callback(self):
        nums = self.check(self.inputs.getvalues())
        if len(nums) == 0:
            self.change_output("Something wrong!")
        else:
            try:
                self.change_output(self.calcul.mupytiply(nums))
            except:
                self.change_output("Something wrong!")

    def minus_callback(self):
        nums = self.check(self.inputs.getvalues())
        if len(nums) == 0:
            self.change_output("Something wrong!")
        else:
            try:
                self.change_output(self.calcul.minus(nums))
            except:
                self.change_output("Something wrong!")

    def divide_callback(self):
        nums = self.check(self.inputs.getvalues())
        if len(nums) == 0:
            self.change_output("Something wrong!")
        else:
            try:
                self.change_output(self.calcul.divide(nums))
            except:
                self.change_output("Something wrong!")