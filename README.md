# python-web-scrapping

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://emalls.ir/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
################################################
import requests as req

resp = req.get("https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Apple-iPhone-13-Pro-Max-1T-Mobile-Phone~id~4883053")

print(resp.text)
################################################
import requests as req
import re

resp = req.get("https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Apple-iPhone-13-Pro-Max-1T-Mobile-Phone~id~4883053")

content = resp.text

stripped = re.sub('<[^<]+?>', '', content)
print(stripped)
###############################################
import requests as req

resp = req.get("https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Apple-iPhone-13-Pro-Max-1T-Mobile-Phone~id~4883053")

print(resp.status_code)
print(resp.history)
print(resp.url)

print(resp.text)
##############################################
import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests

layout = [[sg.Text('Enter the url.')],
                 [sg.InputText()],
                 [sg.Submit(), sg.Exit()],
                 [sg.Help()]]

window = sg.Window("Web Scrapping", layout)

page_number = 1

while True :
    event,values = window.read()

    print(event)
    print(values)
    mydivs = str()
    print(values)
    model_to_brand_number = dict()

    brand_number = model_to_brand_number[values]

    page_number = 1

    url =f"https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Samsung-Galaxy-A70-6-128GB-Mobile-Phone~id~2304289"
    values["url"] = url
    print(values)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    mydivs = soup.find_all("div", {"class": "c-price--value-wrapper"})
    price_list = list
    for span in mydivs:
        try:
            price_list.append(span.contents[0].split("\n")[1].strip())
        except:
            True
        break

window.read()
window.close()
#####################################################
from bs4 import BeautifulSoup
import requests
from csv import writer

url= f"https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['title', 'location', 'price', 'area']
    thewriter.writerow(header)

    for list in lists:
        title = lists.find('a', class_='listing-search-item_link--title').text.replace('\n', '')
        location = lists.find('div', class_='listing-search-item_link--location').text.replace('\n', '')
        price = lists.find('span', class_='listing-search-item_link--price').text.replace('\n', '')
        area = lists.find('span', class_='listing-search-item_link--description').text.replace('\n', '')

        info = [title, location, price, area]
        print(info)
        thewriter.writerow(info)

#########################################################
from bs4 import BeautifulSoup
import requests

for page_number in range(3):
    model = "sumsung"
    url = f"https://www.digikala.com/search/category-mobile-phone/?brands[0]=18&page=1"
    print(url)
    page = requests.get(url)
    print(page)

    soup = BeautifulSoup(page.content,'html.parser')
    mydivs = soup.find_all("div", {"class": "c-price--value-wrapper"})

    print(str(mydivs))
 #####################################################
 import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests

layout = [[sg.Text('Enter the url.')],
                 [sg.InputText()],
                 [sg.Submit(), sg.Exit()],
                 [sg.Help()]]

window = sg.Window("Web Scrapping", layout)

page_number = 1

while True :
    event,values = window.read()

    print(event)
    print(values)
    mydivs = str()
    print(values)
    model_to_brand_number = dict()

    brand_number = model_to_brand_number[values]

    page_number = 1

    url =f"https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Samsung-Galaxy-A70-6-128GB-Mobile-Phone~id~2304289"
    values["url"] = url
    print(values)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    mydivs = soup.find_all("div", {"class": "c-price--value-wrapper"})
    price_list = list
    for span in mydivs:
        try:
            price_list.append(span.contents[0].split("\n")[1].strip())
        except:
            True
        break

window.read()
window.close()

*import PySimpleGUI as sg
from bs4 import BeautifulSoup
from urllib.request import urlopen

layout = [[sg.Text('Enter the url.')],
                 [sg.InputText()],
                 [sg.Submit(), sg.Exit()],
                 [sg.Help()]]

window = sg.Window("Web Scrapping", layout)

page_number = 1

while True :
    event,values = window.read()

    print(event)
    print(values)
    mydivs = str()
    print(values)
    model_to_brand_number = dict()

    page_number = 1

    url = "https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Samsung-Galaxy-M30s-64GB~id~2805425"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup.get_text())

    mydivs = soup.find_all("div", {"class": "c-price--value-wrapper"})
    price_list = list
    for span in mydivs:
        try:
            price_list.append(span.contents[0].split("\n")[1].strip())
        except:
            True
        break

window.read()
window.close()




