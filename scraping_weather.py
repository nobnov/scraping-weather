import re
import urllib.request

from bs4 import BeautifulSoup

url = urllib.request.urlopen('https://www.jma.go.jp/jp/week/315.html')
soup = BeautifulSoup(url, 'lxml')

city = soup.find("th", {"class": "cityname"}).text
days = soup.find("table", {"id": "infotablefont"}).find_all("tr")[0].find_all("th")
max_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[4].find_all("td")
min_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[5].find_all("td")

weather = []

daylist = []
weeklist = []
for day in days:
    day = day.text

    if '日付' not in day:
        weeklist.append(day[-1])
        daylist.append(day[:-1])

maxtemplist = []
for maxtemp in max_temp:
    maxtemp = maxtemp.text

    if '最高' not in maxtemp:
        maxtemp = maxtemp.replace('\n', '').replace('\t', '').replace('(', '{').replace(')', '}')
        maxtemp = re.sub('{.*?}', '', maxtemp)

        if '／' in maxtemp:
            maxtemp = None
        else:
            maxtemp = int(maxtemp)

        maxtemplist.append(maxtemp)

mintemplist = []
for mintemp in min_temp:
    mintemp = mintemp.text

    if '最低' not in mintemp:
        mintemp = mintemp.replace('\n', '').replace('\t', '').replace('(', '{').replace(')', '}')
        mintemp = re.sub('{.*?}', '', mintemp)

        if '／' in mintemp:
            mintemp = None
        else:
            mintemp = int(mintemp)

        mintemplist.append(mintemp)

weather.append(city)
weather.append(weeklist)
weather.append(daylist)
weather.append(maxtemplist)
weather.append(mintemplist)

print(weather)
