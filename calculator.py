import tkinter
from tkinter import ttk
from decimal import *


class Calculator:

    def __init__(self,num) -> None:
        self.num = num

    def output(self, digit):
        number = round(Decimal(digit), 6)
        int_part = int(number)
        frac_part = number - int_part
        formatted_int_part = '{:,}'.format(int_part).replace(',', ' ')
        if frac_part:
            if str(frac_part)[0] == '-':
                formatted_frac_part = str(frac_part)[3:].rstrip('0')
            else:
                formatted_frac_part = str(frac_part)[2:].rstrip('0')
            return f"{formatted_int_part}.{formatted_frac_part}"
        else:
            return formatted_int_part

    def plus(self, digits):
        try:
            result = str(Decimal(digits[0]) + Decimal(digits[1]))
            return self.output(result)
        except:
            return "Something wrong!"

    def mupytiply(self,digits):
        try:
            result = str(Decimal(digits[0]) * Decimal(digits[1]))
            return self.output(result)
        except:
            return str("Something wrong!")

    def minus(self,digits):
        try:
            result = str(Decimal(digits[0]) - Decimal(digits[1]))
            return self.output(result)
        except:
            return str("Something wrong!")

    def divide(self,digits):
        try:
            result = str(Decimal(digits[0]) / Decimal(digits[1]))
            return self.output(result)
        except:
            return str("Something wrong!")

        
