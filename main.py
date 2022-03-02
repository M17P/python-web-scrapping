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
    event,value = window.read()
    print(event,value)
    break
window.read()
window.read()

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('You entered.if you enter Help i cannot help you :)', text_input)
