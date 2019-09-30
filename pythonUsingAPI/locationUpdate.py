from bs4 import BeautifulSoup 
import requests
#zip_code = request.GET.get('zip')
zip_code = '94538'
api_key = '8Am3FfltgwsN3IGxgDXcXS8gyh0pJiLScQ3obgsj94O6ssUwnNW8tWVENsw4CBzP'
units = 'degrees'

def get_location_detail(zip_code):

    try:
        #r = requests.get(url, params={'s': thing})
        response = requests.get("http://www.zipcodeapi.com/rest/"+api_key+"/info.json/"+zip_code+"/<units>")
    except requests.exceptions.RequestException as e:  
        print (e)
        sys.exit(1)
    
    data = response.json()
    lv_lat = data['lat']
    lv_lag = data['lng']
    lv_city = data['city']
    lv_state = data['state']
    return([lv_lat, lv_lag, lv_city, lv_state])


ord_data = "C:\Artatrana\exercise\ordersChanged.csv"
ord_new_data = "C:\Artatrana\exercise\ordersChanged_new.csv"
    
import csv
 
with open(ord_data, newline='') as File:  
    reader = csv.reader(File)
    with open(ord_new_data, mode='w') as new_order:
        writer = csv.writer(new_order, delimiter=',')
        # set headers here, grabbing headers from reader first
        writer.writerow(next(reader) + ['Latitude']+['Longitude']+['City']+['State'])
        counter = 0
        for row in reader:
            if counter < 5 and row[3]!= 'zipcode':
                additionalData = get_location_detail(row[3])
                print (additionalData)
                row.append(additionalData[0])
                row.append(additionalData[1])
                row.append(additionalData[2])
                row.append(additionalData[3])
                print(row)
                writer.writerow(row)
            
            counter += 1




