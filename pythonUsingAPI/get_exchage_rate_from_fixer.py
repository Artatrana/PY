
# Gets Exchange rate from using fixer API
# into the target Data Warehouse (a PostgreSQL database).
# This script runs under Python 3.4 and requires psycopg2


import requests
import json
import datetime
import pandas as pd

# example of url="http://data.fixer.io/api/latest?access_key=your_legacy_access_key&base=USD&symbols=EUR,PEN,AUD"

def get_pd_old_fixer_api(access_key, base, symbols):
    # generate comma separated list of symbol currencies
    str_symbols = ",".join(str(x) for x in symbols)
    # generate url with access key, base currency, and list of comma separated currencies to be converted
    date = "2019-01-03"
    url = "http://data.fixer.io/api/"+date+"?access_key=" + access_key + "&base=" + base + "&symbols=" + str_symbols
    # send the http request
    response = requests.get(url)
    # retrieve the json output
    data = response.text
    parsed = json.loads(data)
    # generate the list of currencies values
    data = []
    for symbol in symbols:
        if symbol != base:
            data.append(parsed["rates"][symbol])
        else:
            # symbol coincides with base currency
            data.append("1")
    cols = {base}
    # create the pandas data frame for this base currency, and values of the converted currencies
    df = pd.DataFrame(data=data, columns=cols, index=symbols)
    return df


def main():
    #access_key = "your_legacy_access_key"
    access_key = "d66276e34daf98b4b149f3eee09ee3a5"
    # get_pd_old_fixer_api(access_key, base, symbols)
    symbols = ["USD","GBP","INR"]
    #generate the pandas currencies data frame for each base currency
    pd_euro = get_pd_old_fixer_api(access_key,'EUR', symbols)
    #pd_usa = get_pd_old_fixer_api(access_key, 'USD', symbols)
    #pd_pen = get_pd_old_fixer_api(access_key, "GBP", symbols)
    #pd_aud = get_pd_old_fixer_api(access_key, "INR", symbols)
    date_time = datetime.datetime.now().strftime("%A %d %B %Y %H:%M:%S:%f")
    print(f"\nOn {date_time} the currency table is:\n")
    pd_total = [pd_euro]
    # we concatenate the pandas data frames on the column axis
    result = pd.concat(pd_total, axis=1, join="outer", sort=False)
    print(result)
if __name__ == '__main__':
    main()
