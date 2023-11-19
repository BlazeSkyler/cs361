import time
import tkinter as tk
from tkinter import ttk, messagebox
# from tkinter import *


# global variables
type_of_conversion = ""
unit1 = ""
unit2 = ""


class PickTypeConversion:
    """
    Constructor of "Home Page"
    """
    def __init__(self, master):
        # set title and size of main page
        self.master = master
        self.master.title("UNIT CONVERTER")
        # self.master.geometry("500x300")

        # Welcome user to application in bold
        self.welcome = tk.Label(self.master, text="Welcome to the Unit Converter")
        self.welcome.config(font=("Cambria", 24, 'bold'))
        self.welcome.pack(padx=5, pady=5)

        # describe program to user
        self.desc = tk.Label(self.master, text="This is a conversion application that supports\ntime and temperature conversions.")
        self.desc.config(font=("Times New Roman", 14))
        self.desc.pack(padx=5)

        self.instruct = tk.Label(self.master, text="To begin using the application, select\n the type of conversion you would like to complete below.")
        self.instruct.config(font=("Times New Roman", 14))
        self.instruct.pack(padx=5)

        # buttons to get user input
        # frame holds all widgets to organize
        self.frame = tk.Frame(self.master)

        # buttons to display conversions offered
        # when button clicked, open page for conversion
        self.timeBut = tk.Button(self.frame, text="Time", height=3, width=10, bg='gray', command=lambda *args: self.check_input(0))
        self.tempBut = tk.Button(self.frame, text="Temperature", height=3, width=10, bg='gray', command=lambda *args: self.check_input(1))

        # using grid to organize in ui
        self.timeBut.grid(row=0, column=0, padx=5, pady=5)
        self.tempBut.grid(row=0, column=1, padx=5, pady=5)

        # place frame
        self.frame.pack(pady=10)

    """
    Checks which button is clicked by user and opens page accordingly
    """
    def check_input(self, value):
        # update global variable
        global type_of_conversion

        # opens next page based on user selection
        if (value == 0):
            type_of_conversion = "Time"
            self.nextWindow = tk.Tk()
            self.app = TimeUnit(self.nextWindow)
            self.master.destroy()

        if (value == 1):
            type_of_conversion = "Temp"
            self.nextWindow = tk.Tk()
            self.app = TempUnit(self.nextWindow)
            self.master.destroy()


class SelectUnit:
    """
    Parent constructor of Select Unit page
    """
    def __init__(self, master):
        self.master = master

        # set title and size of main page
        self.master.title("UNIT CONVERTER")
        # self.master.geometry("500x300")
        self.empty = False
        
        # back button to allow undo function
        self.topFrame = tk.Frame(self.master)
        self.backBut = tk.Button(self.topFrame, text="Back", command=self.undo)
        self.backBut.pack(anchor='w', padx=5, pady=5)
        self.topFrame.pack(fill='x')

        # label for page
        self.l = tk.Label(self.master, text="Select Units")
        self.l.config(font=("Cambria", 24, 'bold'))
        self.l.pack(padx=5, pady=5)

        # page instructions for the user
        self.instruct1 = tk.Label(self.master, text="Use the text boxes or the dropdown menus to\nselect the units for your conversion.")
        self.instruct1.config(font=("Times New Roman", 14))
        self.instruct1.pack(padx=5)

        self.instruct2 = tk.Label(self.master, text="The left box is the unit you are converting from.\nThe right box is the desired unit you are converting to.")
        self.instruct2.config(font=("Times New Roman", 14))
        self.instruct2.pack(padx=5)

        self.instruct3 = tk.Label(self.master, text="Units supported are displayed in the dropdown menu.")
        self.instruct3.config(font=("Times New Roman", 14))
        self.instruct3.pack(padx=5)

        # buttons to get user input
        # frame holds all widgets to organize
        self.frame = tk.Frame(self.master)

        # Combobox and Button collect user input
        self.combo1 = ttk.Combobox(self.frame)
        self.to_text = tk.Label(self.frame, text="to")
        self.to_text.config(font=("Times New Roman", 14))
        self.combo2 = ttk.Combobox(self.frame)
        self.confirmBut = tk.Button(self.frame, text="Confirm", command=self.check_input)
        # using grid to organize in ui
        self.combo1.grid(row=0, column=0, padx=5, pady=5)
        self.to_text.grid(row=0, column=1, padx=5, pady=5)
        self.combo2.grid(row=0, column=2, padx=5, pady=5)
        self.confirmBut.grid(row=0, column=3, padx=5, pady=5)
        # place frame
        self.frame.pack(padx=5, pady=10)


    """
    Destorys current window and opens previous window    
    """
    def undo(self):
        self.lastWindow = tk.Tk()
        self.app = PickTypeConversion(self.lastWindow)
        self.master.destroy()


    """
    Gets user inputs and checks if valid
    """
    def check_input(self):
        # makes selection not case sensitive
        self.selection1 = self.combo1.get().lower()
        self.selection2 = self.combo2.get().lower()

        # empty selection
        if (self.selection1 == "" or self.selection2 == ""):
            self.empty = True
            messagebox.showerror("Error", "Select a Unit")
            return
        

    def open_next(self):
        self.nextWindow = tk.Tk()
        self.app = InputNums(self.nextWindow)
        self.master.destroy()
            

class TimeUnit(SelectUnit):
    """
    Constructor of TimeUnit child
    """
    def __init__(self, master):
        super().__init__(master)

        # change title to confirm selection w/ user
        self.l.config(text="Time Conversion\nSelect Units")

        # add time units offered to dropdowns
        self.offered = ['seconds (s)', 'minutes (min)', 'hours (hr)']
        self.combo1.config(values=self.offered)
        self.combo2.config(values=self.offered)


    """
    Call parent method and check for valid time units
    """
    def check_input(self):
        super().check_input()
        global unit1, unit2

        # check for valid selections and change string to be uniform with rest of program
        if (self.empty is not True):
            if (self.selection1 == "seconds (s)" or self.selection1 == "seconds" or self.selection1 == "second" or self.selection1 == "secs" or self.selection1 == "sec" or self.selection1 == "s"):
                unit1 = "sec"
            elif (self.selection1 == "minutes (min)" or self.selection1 == "minutes" or self.selection1 == "minute" or self.selection1 == "mins" or self.selection1 == "min"):
                unit1 = "min"
            elif (self.selection1 == "hours (hr)" or self.selection1 == "hours" or self.selection1 == "hour" or self.selection1 == "hrs" or self.selection1 == "hr"):
                unit1 = "hr"
            else:
                messagebox.showerror("Error", "Invalid Input Unit")
                return

            # same process for second box
            if (self.selection2 == "seconds (s)" or self.selection2 == "seconds" or self.selection2 == "second" or self.selection2 == "secs" or self.selection2 == "sec" or self.selection1 == "s"):
                unit2 = "sec"
            elif (self.selection2 == "minutes (min)" or self.selection2 == "minutes" or self.selection2 == "minute" or self.selection2 == "mins" or self.selection2 == "min"):
                unit2 = "min"
            elif (self.selection2 == "hours (hr)" or self.selection2 == "hours" or self.selection2 == "hour" or self.selection2 == "hrs" or self.selection2 == "hr"):
                unit2 = "hr"
            else:
                messagebox.showerror("Error", "Invalid Output Unit")
                return

            # warn user if both units are the same
            if (self.selection1 == self.selection2):
                match = messagebox.askyesno("Warning", "Input Unit Matches Output Unit.\nDo you wish to continue?")
                    # user chooses not to continue
                if (match == False):
                    return

            # open next page
            super().open_next()

        # reset empty var
        self.empty = False


class TempUnit(SelectUnit):
    """
    Constructor of TempUnit child
    """
    def __init__(self, master):
        super().__init__(master)

        # change title to confirm selection w/ user
        self.l.config(text="Temperature Conversion\nSelect Units")

        # add temp units offered to dropdowns
        self.offered = ['Farenheit (F)', 'Celcius (C)']
        self.combo1.config(values=self.offered)
        self.combo2.config(values=self.offered)


    def check_input(self):
        super().check_input()
        global unit1, unit2

        # check for valid selections and change string to be uniform with rest of program
        if (self.empty is not True):
            if (self.selection1 == "farenheit (f)" or self.selection1 == "farenheit" or self.selection1 == "f"):
                unit1 = "F"
            elif (self.selection1 == "celcius (c)" or self.selection1 == "celcius" or self.selection1 == "c"):
                unit1 = "C"
            else:
                messagebox.showerror("Error", "Invalid Input Unit")
                return

            # same process for second box
            if (self.selection2 == "farenheit (f)" or self.selection2 == "farenheit" or self.selection2 == "f"):
                unit2 = "F"
            elif (self.selection2 == "celcius (c)" or self.selection2 == "celcius" or self.selection2 == "c"):
                unit2 = "C"
            else:
                messagebox.showerror("Error", "Invalid Output Unit")
                return

            # warn user if both units are the same
            if (self.selection1 == self.selection2):
                match = messagebox.askyesno("Warning", "Input Unit Matches Output Unit.\nDo you wish to continue?")
                    # user chooses not to continue
                if (match == False):
                    return
                
            # open next page
            super().open_next()

        # reset empty var
        self.empty = False


class InputNums:
    """
    Constructor for InputNums page
    """
    def __init__(self, master):
        self.master = master

        # set title and size of main page
        self.master.title("UNIT CONVERTER")
        self.master.geometry("500x300")
        self.empty = False
        
        # back button to allow undo function
        self.topFrame = tk.Frame(self.master)
        self.backBut = tk.Button(self.topFrame, text="Back", command=self.undo)
        self.backBut.pack(anchor='w', padx=5, pady=5)
        self.topFrame.pack(fill='x')

        # label for page
        self.l = tk.Label(self.master, text="Input Numbers")
        self.l.config(font=("Cambria", 24, 'bold'))
        self.l.pack(padx=5, pady=5)

        # page instructions for the user
        self.instruct1 = tk.Label(self.master, text="Use the text boxes or the dropdown menus to\nselect the units for your conversion.")
        self.instruct1.config(font=("Times New Roman", 14))
        self.instruct1.pack(padx=5)

        self.instruct2 = tk.Label(self.master, text="The left box is the unit you are converting from.\nThe right box is the desired unit you are converting to.")
        self.instruct2.config(font=("Times New Roman", 14))
        self.instruct2.pack(padx=5)

        self.instruct3 = tk.Label(self.master, text="Units supported are displayed in the dropdown menu.")
        self.instruct3.config(font=("Times New Roman", 14))
        self.instruct3.pack(padx=5)

        # buttons to get user input
        # frame holds all widgets to organize
        self.frame = tk.Frame(self.master)

        # get user input and confirm previous selections with user
        self.num = tk.Entry(self.frame)
        self.inputUnit_confirm = tk.Label(self.frame, text=unit1)
        self.inputUnit_confirm.config(font=("Times New Roman", 14))
        self.outputUnit_confirm = tk.Label(self.frame, text="to " + unit2)
        self.outputUnit_confirm.config(font=("Times New Roman", 14))
        self.confirmBut = tk.Button(self.frame, text="Confirm", command=self.check_input)
        # using grid to organize in ui
        self.num.grid(row=0, column=0, padx=5, pady=5)
        self.inputUnit_confirm.grid(row=0, column=1, padx=5, pady=5)
        self.outputUnit_confirm.grid(row=1, column=0, padx=5, pady=5)
        self.confirmBut.grid(row=1, column=1, padx=5, pady=5)
        # place frame
        self.frame.pack(padx=5, pady=10)

    """
    Destorys current window and opens previous window    
    """
    def undo(self):
        self.lastWindow = tk.Tk()

        if (type_of_conversion == "Time"):
            self.app = TimeUnit(self.lastWindow)
        if (type_of_conversion == "Temp"):
            self.app = TempUnit(self.lastWindow)
            
        self.master.destroy()


    """
    Checks for valid inputs using microservice
    """
    def check_input(self):
        # microservice
        stringToSend = type_of_conversion, unit1, unit2

        print(stringToSend)
        # send to microservice

        # sleep

        # get msg from microservice

        # if valid
            # convert

        # return

def main():
    root = tk.Tk()
    app = PickTypeConversion(root)
    root.mainloop()

if __name__ == '__main__':
    main()