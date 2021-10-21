import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def get_yearly_rates(amount,currency,converted_currency,amount_of_days):
    
    today_date = datetime.datetime.now()
    date_1year = (today_date - datetime.timedelta(days=1 * amount_of_days))

    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/"

    headers = {
        'x-rapidapi-host': "currency-conversion-and-exchange-rates.p.rapidapi.com",
        'x-rapidapi-key': "bafa666024msh1b0139152aa6c2dp189e5fjsnec894e5b254a"
              }

    payload = {"base":currency, "amount":amount, "start_date":date_1year.date(),"end_date":today_date.date()}
    response = requests.request("GET", url, headers=headers,params=payload)
    data = response.json()

    currency_history = {}
    rate_history_array = []

    for item in datetime.date["rates"]:
        current_date = item
        currency_rate = data["rates"][item][converted_currency]

        currency_history[current_date] = [currency_rate]
        rate_history_array.append(currency_rate)

    pd_data = pd.DataFrame(currency_history).transpose()
    pd_data.columns = ["Rate"]
    pd.set_option("display.max_rows", None)
    print(pd_data)    

get_yearly_rates(1,"EUR","GBP",90)    





#print(response.text)