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

# Covid api
response2 = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
data2 = response2.json()
data = (data2[0])
new_case = data["new_case"]
update_time = data["update_date"]
a,b=update_time.split(" ")
update_time = a+" at "+b
new_death = data["new_death"]
new_recovered = data["new_recovered"]

# Weather api
response3=requests.get("https://data.tmd.go.th/api/WeatherForecastDaily/V1/")
data3=response3.json()
DailyForecast = data3["DailyForecast"]
Des_Overall = DailyForecast["DescEng"]
RegionsForecast = DailyForecast["RegionsForecast"]
Northern = RegionsForecast[0]
Northeastern = RegionsForecast[1]
Central = RegionsForecast[2]
Eastern = RegionsForecast[3]
Southern_East = RegionsForecast[4]
Southern_West = RegionsForecast[5]
Metropolitan = RegionsForecast[6]
Des_Northern = Northern["DescriptionEng"]
Des_Northeasten = Northeastern["DescriptionEng"]
Des_Central = Central["DescriptionEng"]
Des_Eastern = Eastern["DescriptionEng"]
Des_Southern_East = Southern_East["DescriptionEng"]
Des_Southern_West = Southern_West["DescriptionEng"]
Des_Metropolitan = Metropolitan["DescriptionEng"]

# Create root and define size
root = Tk()
root.title("Traveller Help")
root.geometry("500x180+200+200")

# Create a Menu
myMenu = Menu()
root.config(menu = myMenu)

# Define colour function
def bgcolour():
    color = colorchooser.askcolor()
    coloeHex = color[1]
    root.config(bg = coloeHex)

def update():
  # To drag an API from fixer.io
  response = requests.get("http://data.fixer.io/api/latest?access_key=00d8aa0be4f027aa0b7757c5fca58787&format=1")
  data = response.json()
  rates = data["rates"]

  # Covid api
  response2 = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
  data2 = response2.json()
  data = (data2[0])
  new_case = data["new_case"]
  update_time = data["update_date"]
  a,b=update_time.split(" ")
  update_time = a+" at "+b
  new_death = data["new_death"]
  new_recovered = data["new_recovered"]

  # Weather api
  response3=requests.get("https://data.tmd.go.th/api/WeatherForecastDaily/V1/")
  data3=response3.json()
  DailyForecast = data3["DailyForecast"]
  Des_Overall = DailyForecast["DescEng"]
  RegionsForecast = DailyForecast["RegionsForecast"]
  Northern = RegionsForecast[0]
  Northeastern = RegionsForecast[1]
  Central = RegionsForecast[2]
  Eastern = RegionsForecast[3]
  Southern_East = RegionsForecast[4]
  Southern_West = RegionsForecast[5]
  Metropolitan = RegionsForecast[6]
  Des_Northern = Northern["DescriptionEng"]
  Des_Northeasten = Northeastern["DescriptionEng"]
  Des_Central = Central["DescriptionEng"]
  Des_Eastern = Eastern["DescriptionEng"]
  Des_Southern_East = Southern_East["DescriptionEng"]
  Des_Southern_West = Southern_West["DescriptionEng"]
  Des_Metropolitan = Metropolitan["DescriptionEng"]

  et3.delete(0, END)
  et3.insert(0, new_recovered)
  et4.delete(0, END)
  et4.insert(0, new_case)
  et5.delete(0, END)
  et5.insert(0, new_death)
  et6.delete(0, END)
  et6.insert(0, update_time)

# Add command to menu items
menuitem = Menu()
menuitem.add_command(label = "Edit Colour", command = bgcolour)
menuitem.add_command(label = "Update", command= update)
menuitem.add_command(label = "Exit", command = root.destroy)

# Add menu items to Menu
myMenu.add_cascade(label = "File",menu = menuitem)

# Create notebook
notebook = ttk.Notebook(root)
notebook.pack(pady = 15)

# Create frame
frame1 = Frame(notebook)
frame2 = Frame(notebook)
frame3 = Frame(notebook)

# Naming titles
notebook.add(frame1, text = "Currency converter")
notebook.add(frame2, text = "Covid")
notebook.add(frame3, text = "Weather")

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
  amount.initialize(1)

# Create calculate function
def calculate():
  a = amount.get()
  a=float(a)
  unit1 = choice.get()
  unit2 = choice2.get()
  if a>=0:
    et2.delete(0, END)
    result = round(float(a) * (float(rates[unit2]) / float(rates[unit1])), 3)
    et2.insert(0, result)
  # For those who entered negative amount  
  else:
    messagebox.showerror("Error", "You entered negative amount")

# Create buttons
Button(frame1, text="Calculate", font = ("Arial", 10),width = 15, command = calculate).grid(row = 4, column = 1, sticky = W)
Button(frame1, text="Clear", font = ("Arial", 10), width = 15, command = clear).grid(row = 4, column = 1, sticky = E)

# To input float value
text3 = DoubleVar()
text3.initialize(0)

# To create label
Label(frame2, text = "New Recovered", font = ("Arial", 10), padx = 10).grid(row = 0, sticky = W)
et3 = Entry(frame2, font = ("Arial", 10), width = 35, textvariable = text3)
et3.grid(row = 0, column = 1)
et3.delete(0, END)
et3.insert(0, new_recovered)

# To input float value
text4 = DoubleVar()

# To create label
Label(frame2, text = "New Case", font = ("Arial", 10), padx = 10).grid(row = 1, sticky = W)
et4 = Entry(frame2, font = ("Arial", 10), width = 35, textvariable = text4)
et4.grid(row = 1, column = 1)
et4.delete(0, END)
et4.insert(0, new_case)

# To input float value
text5 = DoubleVar()

# To create label
Label(frame2, text = "New Deaths", font = ("Arial", 10), padx = 10).grid(row = 2, sticky = W)
et5 = Entry(frame2, font = ("Arial", 10), width = 35, textvariable = text5)
et5.grid(row = 2, column = 1)
et5.delete(0, END)
et5.insert(0, new_death)

# To input float value
text6 = DoubleVar()

# To create label
Label(frame2, text = "Updated Time", font = ("Arial", 10), padx = 10).grid(row = 3, sticky = W)
et6 = Entry(frame2, font = ("Arial", 10), width = 35, textvariable = text6)
et6.grid(row = 3, column = 1)
et6.delete(0, END)
et6.insert(0, update_time)

# To Create space
Label(frame3, text = "").grid(row = 0, sticky = W)

# Create combobox
zone = StringVar(value = "Please choose a zone")
Label(frame3, text = "Forecast", padx = 10, font = ("Arial",10)).grid(row = 1, sticky = W)
combo3 = ttk.Combobox(frame3, width = 30, font = ("Arial", 10), textvariable = zone)
combo3["values"] = ("Overall Thailand","Bangkok and Neighborhood","North","Northeastern","Central","East","Southern (East Coast)","Southern (West Coast)")
combo3.grid(row = 1, column = 1)

# To Create space
Label(frame3, text = "").grid(row = 2, sticky = W)

# Define function
def Forecastupdate():
    a = zone.get()
    if a == "Overall Thailand":
      messagebox.showinfo(a+" Weather", Des_Overall)
    elif a == "Bangkok and Neighborhood":
      messagebox.showinfo(a+" Weather", Des_Metropolitan)
    elif a == "North":
      messagebox.showinfo(a+" Weather", Des_Northern)
    elif a == "Northeastern":
      messagebox.showinfo(a+" Weather", Des_Northeasten)  
    elif a == "Central":
      messagebox.showinfo(a+" Weather", Des_Central) 
    elif a == "East":
      messagebox.showinfo(a+" Weather", Des_Eastern)   
    elif a == "Southern (East Coast)":
      messagebox.showinfo(a+" Weather", Des_Southern_East)  
    elif a == "Southern (West Coast)":
      messagebox.showinfo(a+" Weather", Des_Southern_West)
    else:
      messagebox.showerror("Error","No Key")          

# Create update button
Button(frame3, text="Show", font = ("Arial", 10),width = 15, command = Forecastupdate).grid(row = 3, column = 1, sticky = W)

# Run this root
root.mainloop()
