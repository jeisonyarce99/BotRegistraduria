# Librerías
from re import S
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver_path = 'C:\\Users\\yarce\\Downloads\\chromedriver_win32\\chromedriver.exe'
s = Service(driver_path)

driver = webdriver.Chrome(service=s, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('https://wsp.registraduria.gov.co/certificado/Datos.aspx')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#ContentPlaceHolder1_TextBox1')))\
    .send_keys('1032417574')
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'select#ContentPlaceHolder1_DropDownList1')))\
    .send_keys('09')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'select#ContentPlaceHolder1_DropDownList2')))\
    .send_keys('Agosto')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'select#ContentPlaceHolder1_DropDownList3')))\
    .send_keys('2006')

url_ok = 'https://wsp.registraduria.gov.co/certificado/Respuesta.aspx' 
get_url = driver.current_url   
while get_url != url_ok:
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#ContentPlaceHolder1_TextBox2')))\
        .send_keys('LANAP')
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#ContentPlaceHolder1_Button1')))\
        .click()
    alt = driver.switch_to.alert
    alt_text = alt.text
    alt.accept() 
    get_url = driver.current_url

time.sleep(2)
newURl = driver.window_handles[0]

driver.switch_to.window(newURl)

# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'input#ContentPlaceHolder1_TextBox2')))\
#     .send_keys('LANAP')
# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'input#ContentPlaceHolder1_Button1')))\
#     .click()

# # PUEDEN PASAR 2 ESCENARIOS
# # EL CODIGO DEL CAPCHA SEA INCORRECTO
# #print(driver.getCurrentUrl())
# #EL CODIGO DEL CAPCHA SEA CORRECTO

# alt = driver.switch_to.alert
# alt_text = alt.text
# alt.accept()
# url_ok = 'https://wsp.registraduria.gov.co/certificado/Respuesta.aspx'
# get_url = driver.current_url
# print("The current url is:"+str(get_url))

    

# s = Service(get_url)
# driver = webdriver.Chrome(service=s)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#ContentPlaceHolder1_Button1.botongenerarcert')))\
    .click()

driver.quit()