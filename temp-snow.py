#weather and snow spreadsheet
import bs4, requests

#get the website
def getdate(weatherapp):

    res = requests.get(weatherapp)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select("#dailyWeatherListItem0 > div.daily-weather-list-item__date-and-warnings > a")
    return elems[0].text

date = getdate("https://www.yr.no/en/forecast/daily-table/2-3030142/France/Provence-Alpes-C%C3%B4te%20d'Azur/Hautes-Alpes/Brian%C3%A7on")
date_month = date.split()[1]
date_day = date.split()[2]

#get the temp
def gettemp(weatherapp):

    res = requests.get(weatherapp)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select("#dailyWeatherListItem0 > div.daily-weather-list-item__forecast > div.daily-weather-list-item__temperature")
    return elems[0].text

temp = gettemp("https://www.yr.no/en/forecast/daily-table/2-3030142/France/Provence-Alpes-C%C3%B4te%20d'Azur/Hautes-Alpes/Brian%C3%A7on")
temp_all = temp.split()[2][12:18]

#get the precip 
def getprecip(weatherapp):
    
    res = requests.get(weatherapp)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select("#dailyWeatherListItem0 > div.daily-weather-list-item__forecast > div.daily-weather-list-item__precipitation")
    return elems[0].text

precip = getprecip("https://www.yr.no/en/forecast/daily-table/2-3030142/France/Provence-Alpes-C%C3%B4te%20d'Azur/Hautes-Alpes/Brian%C3%A7on")
precip_no = precip.split()[1]


print(date_month + date_day + '\n' + temp_all + '\n'+ precip_no)



#print to an excel sheet
