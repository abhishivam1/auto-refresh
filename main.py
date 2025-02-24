#made by @abhishivam1
import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

layout = [
    [sg.Text("Enter the URL to open:")],
    [sg.InputText(key='url')],
    [sg.Button("Submit"), sg.Button("Cancel")]
]

window = sg.Window("URL Input", layout)
event, values = window.read()
window.close()

url = values['url']

if event == sg.WIN_CLOSED or event == 'Cancel':
    exit()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)

try:
    while True:
        time.sleep(8)
        driver.refresh()
except KeyboardInterrupt:
    driver.quit()
