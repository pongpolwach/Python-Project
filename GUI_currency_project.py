# Import items
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser 
from tkinter.colorchooser import *
from tkinter import ttk
import requests

# To drag an API from fixer.io
response = requests.get("http://data.fixer.io/api/latest?access_key=00d8aa0be4f027aa0b7757c5fca58787&format=1")
data = response.json()
rates = data["rates"]

# Create root and define size
root = Tk()
root.title("Currency Converter Project")
root.geometry("500x180+200+200")

# Create a Menu
myMenu = Menu()
root.config(menu = myMenu)

# Define colour function
def bgcolour():
    color = colorchooser.askcolor()
    coloeHex = color[1]
    root.config(bg = coloeHex)

# Add command to menu items
menuitem = Menu()
menuitem.add_command(label = "Edit Colour", command = bgcolour)
menuitem.add_command(label = "Exit", command = root.destroy)

# Add menu items to Menu
myMenu.add_cascade(label = "File",menu = menuitem)

# Create notebook
notebook = ttk.Notebook(root)
notebook.pack(pady = 15)

# Create frame
frame1 = Frame(notebook)
frame2 = Frame(notebook)

# Naming titles
notebook.add(frame1, text = "Currency converter")
notebook.add(frame2, text = "About")

# To input float value
amount = DoubleVar()
# To show 1 if there is no attemp
amount.initialize(1)

# Create input box
Label(frame1, text = "Amount", font = ("Arial", 10), padx = 10).grid(row = 0, sticky = W)
et1 = Entry(frame1, font = ("Arial", 10), width = 35, textvariable = amount)
et1.grid(row = 0, column = 1)

# Create first combobox
choice = StringVar(value = "Please choose a currency")
Label(frame1, text = "1 st Currency", padx = 10, font = ("Arial",10)).grid(row = 1, sticky = W)
combo1 = ttk.Combobox(frame1, width = 30, font = ("Arial", 10), textvariable = choice)
# Not to use too much API
combo1["values"] = ("AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM",
       "BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTC",
       "BTN","BWP","BYN", "BYR","BZD", "CAD","CDF","CHF","CLF","CLP","CNY",
       "COP","CRC", "CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP",
       "ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD",
       "GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP",
       "INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR",
       "KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL",
       "LTL","LVL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRO",
       "MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR",
       "NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON",
       "RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL",
       "SOS","SRD", "STD","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP",
       "TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VEF","VND",
       "VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPF","YER","ZAR",
       "ZMK","ZMW","ZWL")
combo1.grid(row = 1, column = 1)

# Create second combo box
choice2 = StringVar(value = "Please choose a currency")
Label(frame1, text = "2 nd Currency", padx = 10, font = ("Arial", 10)).grid(row = 2,sticky = W)
combo2 = ttk.Combobox(frame1, width = 30, font = ("Arial", 10), textvariable = choice2)
# Not to double API usage when I test
combo2["values"] = ("AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM",
       "BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTC",
       "BTN","BWP","BYN", "BYR","BZD", "CAD","CDF","CHF","CLF","CLP","CNY",
       "COP","CRC", "CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP",
       "ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD",
       "GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP",
       "INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR",
       "KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL",
       "LTL","LVL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRO",
       "MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR",
       "NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON",
       "RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL",
       "SOS","SRD", "STD","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP",
       "TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VEF","VND",
       "VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPF","YER","ZAR",
       "ZMK","ZMW","ZWL")
combo2.grid(row = 2, column = 1)

# Create output box
Label(frame1, text = "Converted", font = ("Arial", 10), padx = 10).grid(row = 3, sticky = W)
et2 = Entry(frame1, font = ("Arial", 10), width = 35)
et2.grid(row=3,column=1)

# Create clear function
def clear():
  et1.delete(0, END)
  et2.delete(0, END)
  combo1.delete(0, END)
  combo2.delete(0, END)
  combo1.insert(0, "Please choose a currency")
  combo2.insert(0, "Please choose a currency")

# Create calculate function
def calculate():
  a = amount.get()
  unit1 = choice.get()
  unit2 = choice2.get()
  if float(a) >= 0:
    result = round(float(a) * (float(rates[unit2]) / float(rates[unit1])), 3)
    et2.insert(0, result)
  # For those who entered negative amount  
  else:
    messagebox.showerror("Error", "You entered negative amount")

# Create buttons
Button(frame1, text="Calculate", font = ("Arial", 10),width = 15, command = calculate).grid(row = 4, column = 1, sticky = W)
Button(frame1, text="Clear", font = ("Arial", 10), width = 15, command = clear).grid(row = 4, column = 1, sticky = E)

# Write down information
Label(frame2, text = "Project: Currency Converter", font = ("Arial", 15)).grid(row = 1)
Label(frame2, text = "Creator: Pongpol Wachiralappaitoon", font = ("Arial", 15)).grid(row = 2)
Label(frame2, text = "Propose: Natthapong Jungteerapanich", font = ("Arial", 15)).grid(row = 3)
Label(frame2, text = "Institute: SIIE, KMITL", font = ("Arial", 15)).grid(row = 4)

# Run this root
root.mainloop()