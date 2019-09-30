#Python code to use panda and open the csv file
#And add needed columns. I have tested with 25 records as more records are getting key error
import pandas as pd
import sys
from bs4 import BeautifulSoup 
import requests

zip_code = '94538'
api_key = '8Am3FfltgwsN3IGxgDXcXS8gyh0pJiLScQ3obgsj94O6ssUwnNW8tWVENsw4CBzP'
units = 'degrees'
#This function will return other detail by supplying zipcode
def get_other_detail(zip_code,param):
    zip_code = str(zip_code)

    try:
        #r = requests.get(url, params={'s': thing})
        response = requests.get("http://www.zipcodeapi.com/rest/"+api_key+"/info.json/"+zip_code+"/<units>")
    except requests.exceptions.RequestException as e:  
        print (e)
        sys.exit(1)
        
    try:
        data = response.json()
        lv_lat = data['lat']
        lv_lng = data['lng']
        lv_city = data['city']
        lv_state = data['state']
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e)
        sys.exit(1)
    
    if param == 1:
        return lv_lat
    elif param == 2:
        return lv_lng
    elif param == 3:
        return lv_city
    elif param == 4:
        return lv_state
    

ord_data = "C:\Artatrana\exercise\orders25records.csv"
csv_input = pd.read_csv(ord_data)
csv_input['Latitude'] = csv_input['zipcode'].apply(get_other_detail,param=1)
csv_input['Longitude'] = csv_input['zipcode'].apply(get_other_detail, param=2)
csv_input['City'] = csv_input['zipcode'].apply(get_other_detail, param=3)
csv_input['State'] = csv_input['zipcode'].apply(get_other_detail, param=4)
csv_input.to_csv(ord_data, index=False)

print("Module completed Successfully !!!")

