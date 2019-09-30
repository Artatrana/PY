import requests
import json
import datetime
import pandas as pd
import sqlite3



#access_key = "your_legacy_access_key"
access_key = "d66276e34daf98b4b149f3eee09ee3a5"
# get_pd_old_fixer_api(access_key, base, symbols)
symbols = ["EUR", "USD", "PEN", "AUD"]
#Base
base = 'EUR'
# generate url with access key, base currency, and list of comma separated currencies to be converted
url = "http://data.fixer.io/api/latest?access_key=" + access_key + "&base=" + base
# send the http request
response = requests.get(url)
# retrieve the json output
data = response.text
parsed = json.loads(data)
# generate the list of currencies values
rate_dict = parsed["rates"]
for key in rate_dict:
    print(key,"-->",rate_dict[key])
