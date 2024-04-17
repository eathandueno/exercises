#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        # Define string variables for text entry fields
        self.miles_driven = tk.StringVar()
        self.gallons_used = tk.StringVar()
        self.mpg = tk.StringVar()

        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.miles_driven).grid(column=1, row=0)

        ttk.Label(self, text="Gallons of Gas Used:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.gallons_used).grid(column=1, row=1)

        ttk.Label(self, text="Miles Per Gallon:").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.mpg).grid(column=1, row=2)

        ttk.Button(self, text="Calculate", command=self.calculate).grid(column=0, row=3)
        ttk.Button(self, text="Clear").grid(column=1, row=3)

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def get_float(self, value):
        try:
            return float(value)
        except ValueError:
            messagebox.showerror("Error", "Invalid input: Please enter a number.")
            return None

    def calculate(self):
        miles = self.get_float(self.miles_driven.get())
        gallons = self.get_float(self.gallons_used.get())
        if miles is not None and gallons is not None:
            mpg = round(miles / gallons, 2)
            self.mpg.set(mpg)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MPG Calculator")
    MyFrame(root)
    root.mainloop()