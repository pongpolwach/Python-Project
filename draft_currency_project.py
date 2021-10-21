import requests
import time

# To drag an API from fixer.io
response=requests.get("http://data.fixer.io/api/latest?access_key=00d8aa0be4f027aa0b7757c5fca58787&format=1")
data=response.json()

# To import data from rates
rates=data["rates"]

# To import time from timestamp
timestamp=data["timestamp"]

#To enable a local time
epoch_time = timestamp
local_time = time.ctime(epoch_time)

# Price of vuccines based on USD -The Bangkok Post 16 JAN 2021 AT 04:00
Vuccine={"AZTRAZENECA":4,
         "PFIZER":20,
         "SINOVAC":17,
         "SINOPHARM":33,
         "SPUTNIK-V":10,
         "MODERNA":33,
         "JOHNSON&JOHNSON":10,
         "NOVAVAX":16,
         "GAMELEYA":10}

x=input("Please enter a value here: ").split(" ")

# For those who want only currency rates
if len(x)==1:
  # To capitalized the unit
  unit=x[0].upper()
  # To make sure there is no random word
  if unit in rates:
    print("1",unit,"is equal to",round(rates["THB"]/rates[unit],3),"THB")
    print("The updated rates of exchange time is:", local_time)
  # For those who write down some random words  
  else:
    print("Please enter similar as a form below")  
    print("!!! 1 USD to THB !!!")  
    print("or Sinovac in THB !!")
# For those who want to know only rates
elif len(x)==3:
  # To capitalized all letters
  unit1=x[0].upper()
  unit2=x[2].upper()
  # To make sure there is no random word
  if unit1 in rates and unit2 in rates:
    value=round(float(rates[unit2])/float(rates[unit1]),3)
    print("1",unit1,"is equal to",value,unit2)
    print("The updated rates of exchange time is:", local_time)
  # For those who want to know a price of vuccine in each currency  
  elif unit1 in Vuccine and unit2 in rates:
    V_price=round(Vuccine[unit1]*(rates[unit2]/rates["USD"]),3)
    print("1 dose of",unit1,"cost",V_price,unit2)
  # For those who write down random word  
  else:
    print("Please enter similar as a form below")  
    print("!!! 1 USD to THB !!!")  
    print("or Sinovac in THB !!")
# For those who want to convert currency
elif len(x)==4:
  # To capitalized all letters
  unit1=x[1].upper()
  unit2=x[3].upper()
  # To make sure there is no random word
  if unit1 in rates and unit2 in rates:
    print("The program will convert", unit1, "to", unit2)
    amount=float(x[0])
    # For a normal amount of money case
    if amount>=1:
      print(int(amount),unit1,"is equal to",round(amount*(float(rates[unit2])/float(rates[unit1])),3),unit2)
      print("The updated rates of exchange time is:", local_time)
    # Not to print 0 when amount less than 0.5  
    # If amount is less than 0.5 it will print out 0 as an integer
    else:
      print(float(amount),unit1,"is equal to",round(amount*(float(rates[unit2])/float(rates[unit1])),3),unit2)
      print("The updated rates of exchange time is:", local_time)
  # For those who write down random word    
  else:
    print("Please enter similar as a form below")  
    print("!!! 1 USD to THB !!!")  
    print("or Sinovac in THB !!")
else:
  print("Please enter similar as a form below")  
  print("!!! 1 USD to THB !!!")
  print("or Sinovac in THB !!")