import PySimpleGUI as sg
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

