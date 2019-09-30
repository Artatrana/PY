# Gets Exchange rate from using fixer API
# into the target Data Warehouse (a  database).
# Note: for simplycity I have used input for paramter inputself.
# can be used commnd line argument using sys or getopt module
# Also not sure what is meat by display the result neatly : so showinf latest rate
# For avarage took the supplied date for simplycity

import requests
import json
import pandas as pd
import datetime
import sqlite3

#Date range will generate the iterable date between two supplied dates
def daterange(start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )


class ExchageRate:

    #This will inset exchage rate for all the currency for supplied start and end_date
    #we can define end_date as 2 years back from start_date
    def get_rate_fixer_api(self, cur,date,access_key, base):

        # generate url with access key, base currency, and list of comma separated currencies to be converted
        url = "http://data.fixer.io/api/"+str(date)+"?access_key=" + access_key + "&base=" + base
        try:
            # send the http request
            response = requests.get(url)
        except requests.ConnectionError as error:
            print (error)
            sys.exit(1)

        # retrieve the json output
        data = response.text
        parsed = json.loads(data)
        # generate the list of currencies values
        rate_dict = parsed["rates"]
        for key in rate_dict:
            conv_rate = rate_dict[key]
            try:
                cur.execute("INSERT INTO RATE (base_code , date, rate, currency_code) VALUES ( ?,?, ? , ? )", ( base,date,conv_rate,key ))
            except Exception as e:
                print ("Error while getting data through API", e)
                sys.exit(1)

    # this will return avarage_Rate for spectifi currency and suppllied date range
    #using database function
    def get_avarage_rate(self, conn,currency_code,start_date,end_date):
        df= pd.read_sql_query('SELECT rate FROM RATE where currency_code=? and date >= ? and date <= ?'
             ,conn, params=(currency_code,start_date,end_date))

        avg = round(df["rate"].mean(),3)
        print("Average Excnage Rate for {} between {} and {} is:{} ".format(currency_code,start_date, end_date, avg ))
        return avg
    # this will display latest all exchange reate
    def display_rate(self, conn):
        df= pd.read_sql_query('SELECT * FROM RATE where date >= (select max(date)-1 from RATE)',conn)
        df_display= df.set_index('date')
        print()
        print("*** Latest Exchange Rate All currencies ***")
        print()
        print(df_display)


def main():

    #This will create table to store the data in the database
    conn = sqlite3.connect('spider.sqlite3')
    cur = conn.cursor()

    #cur.execute("DELETE FROM RATE")
    cur.execute("CREATE TABLE IF NOT EXISTS RATE ( base_code TEXT, date date, rate number, currency_code TEXT )")
    cur.execute("DELETE FROM RATE")

    #access_key = "your_access_key"
    access_key = "d676e34daf98b4b149f3eeee3a5"

    #base currency , ( assumption Data entry is right Code )
    base = input('''Please enter the base currency like EUR or USD OR GBP etc.
    Or just enter for default EUR \n''')
    if base == '' or base is None:
        #setting base currency as Euro
        base = 'EUR'
        print("Since no base currency supplied, base currency ser to EUR")

    #Setting of date
    date_entry = input('''Please enter date till which rate to be populateed in 'YYYY-MM-DD' formatself.
    Or just enter for default as today\n''')

    if date_entry == '' or date_entry is None:
        end_date = date=datetime.datetime.now().date()
        print("Since no date supplied, date set to today")
    else:
        year, month, day = map(int, date_entry.split('-'))
        #Assuing date data entry is write foramt
        end_date = datetime.date(year, month, day)

    #start_date is always 2 year prior date from the end date entered
    start_date = end_date - datetime.timedelta(days=730)
    #For testing I have use only last 5 days
    #start_date = end_date - datetime.timedelta(days=5)
    #For 2 years data
    #start_date = end_date - datetime.timedelta(days=730)
    print("Base currency --> ",base)
    print("Start date --> ",start_date)
    print("End date --> ",end_date)

    erate = ExchageRate()
    for date in daterange(start_date, end_date):
        erate.get_rate_fixer_api(cur,date,access_key, base)
    conn.commit()

    #display and get avarage fro specified date
    #For convience I have use the date range supplied earlier
    #and used a hard coded Currecy code, these can be easily parameterize
    erate.get_avarage_rate(conn,'INR',start_date, end_date)

    #display the latest rate for all the currencies
    erate.display_rate(conn)


    conn.close()

if __name__ == '__main__':
    main()
