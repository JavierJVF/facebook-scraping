from clases_instagram.Web_driver import Web_driver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from clases_instagram.Search import Search
import random

#########################################
# Clase para abstraer metodos sobre la Cuenta que se usa
# para ingresar a Instagram, navegar y ubicar la seccion que nos interesa
#############################3##########

class Account_scraper(Web_driver):
    def __init__(self, mail_or_phone_number, password, search=None):
        self.mail_or_phone_number = mail_or_phone_number
        self.password = password
        self.search = search

        super().__init__()
    
    #metodo para iniciar session en facebook mediante unas credenciales ya ingresadas
    def login(self):
        print('logueando')
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(25)
        name_png = 'login_instagram'+self.str_datetime()
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')
        self.set_credentials()
        time.sleep(25)

        name_png = 'login_instagram'+self.str_datetime()
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')

        print('logueado')

    #metodo para realizar el proceso de rellenar el formulario de iniciar sesion
    def set_credentials(self):
        time.sleep(15)
        self.fill_mail_or_phone_number()
        self.fill_password()
        self.click_login()
    
    #Metodo para rellenar el input de mail_or_number
    def fill_mail_or_phone_number(self):
        input_mail_or_phone_number = self.driver.find_element_by_name('username')
        input_mail_or_phone_number.send_keys(self.mail_or_phone_number, Keys.ARROW_DOWN)
    
    #Metodo para rellenar el input de password
    def fill_password(self):
        input_pass = self.driver.find_element_by_name('password')
        input_pass.send_keys(self.password, Keys.ARROW_DOWN)

    #Metodo para hacer click al boton de entrar para enviar los datos ingresados
    def click_login(self):
        button_send = self.driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
        self.driver.execute_script("arguments[0].click();", button_send)
    
    def search_set(self, terminos):
        self.search = Search(terminos, self.driver)
    
    def link_set(self, link):
        self.search = Search(None, self.driver, link)

    # metodo para establecer la fecha y hora como un string 
    # y usarlo como nombres de las capturas de pantalla    
    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')
