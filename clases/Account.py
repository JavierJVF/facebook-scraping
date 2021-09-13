from clases.Web_driver import Web_driver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from clases.User_objetive import User_objetive
import random


class Account(Web_driver):
    def __init__(self, mail_or_phone_number, password, user_obetive = None):
        self.mail_or_phone_number = mail_or_phone_number
        self.password = password
        self.list_frends = []
        self.user_obetive = user_obetive

        super().__init__()
    
    def login(self):
        print('logueando')
        self.driver.get('https://www.facebook.com/')
        time.sleep(25)

        self.set_credentials()
        time.sleep(25)

        name_png = 'login_'+self.str_datetime()
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')

        print('logueado')

    def set_credentials(self):
        self.fill_mail_or_phone_number()
        self.fill_password()
        self.click_login()
    
    def fill_mail_or_phone_number(self):
        input_mail_or_phone_number = self.driver.find_element_by_id('email')
        input_mail_or_phone_number.send_keys(self.mail_or_phone_number, Keys.ARROW_DOWN)
    
    def fill_password(self):
        input_pass = self.driver.find_element_by_id('pass')
        input_pass.send_keys(self.password, Keys.ARROW_DOWN)

    def click_login(self):
        button_send_content = self.driver.find_elements_by_css_selector('div._6ltg')[0]
        button_send = button_send_content.find_element_by_css_selector('button')
        self.driver.execute_script("arguments[0].click();", button_send)
    
    def find_friends(self):
        self.driver.get('https://www.facebook.com/friends/list')
        time.sleep(25)
        name_png = 'friends_'+self.str_datetime()+'.csv'
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')

        my_list_frends = self.driver.find_elements_by_css_selector('div.sxpk6l6v a')
        print(len(my_list_frends))
        for friend in my_list_frends:
            url = friend.get_attribute('href')
            name = friend.find_element_by_css_selector('span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.jq4qci2q.a3bd9o3v')
            self.list_frends.append({'url': url, 'name': name.text})
    
    def select_user_objetive(self):
        size = len(self.list_frends)
        if size ==0:
            self.user_obetive = None
        else:
            friend = self.list_frends[random.randint(0, size-1)]
            #friend = self.list_frends[7]
            self.user_obetive = User_objetive(friend['url'] , friend['name'], self.driver)
    
    def get_friend_random(self):
        return self.list_frends[random.randint(0, len(self.list_frends)-1)]
        
    def set_list(self):
        self.list_frends = [
            {'url': 'https://www.facebook.com/darvinson.santoyo', 'name': 'Darvinson Jose'}, 
            {'url': 'https://www.facebook.com/sergio.leon.3910', 'name': 'Sergio Jesus Leon'}, 
            {'url': 'https://www.facebook.com/hectorramon.carrionmendez', 'name': 'Hector Carrion'}, 
            {'url': 'https://www.facebook.com/celemar', 'name': 'Celenia Febres'}, 
            {'url': 'https://www.facebook.com/yosnel.febres', 'name': 'Yosnel Febres'}, 
            {'url': 'https://www.facebook.com/yurvielys.figuera', 'name': 'Yurvielys Figuera'}, 
            {'url': 'https://www.facebook.com/jennis.febres', 'name': 'Jennis Febres'}, 
            {'url': 'https://www.facebook.com/nerismar.febres', 'name': 'Nerismar Febres'}, 
            {'url': 'https://www.facebook.com/josejavier.figuera', 'name': 'Jose Javier Figuera'}, 
            {'url': 'https://www.facebook.com/maryuli.febres', 'name': 'Maryuli Febres'}, 
            {'url': 'https://www.facebook.com/ronnymixx.vera', 'name': 'Ronny Vera'}, 
            {'url': 'https://www.facebook.com/jairo.vera.509', 'name': 'Jairo Vera'}, 
            {'url': 'https://www.facebook.com/rosdeinys.rodriguez', 'name': 'Rosdeinys Rodriguez'}, 
            {'url': 'https://www.facebook.com/chismeliciosouneg', 'name': 'Uneg Uneg'}, 
            {'url': 'https://www.facebook.com/angelmanuel.verafebres', 'name': 'Angel Manuel Vera Febres'}, 
            {'url': 'https://www.facebook.com/labebakeli.fuentes', 'name': 'Keliannys Gabriela Fuentes'}, 
            {'url': 'https://www.facebook.com/Solangelcamila89', 'name': 'Maurera Sol'}, 
            {'url': 'https://www.facebook.com/eliezer.26', 'name': 'Eliezer Romero'}, 
            {'url': 'https://www.facebook.com/yarii.zuniga', 'name': 'Yáríí Zúñígá'}]
    
    def metodo_fill_posts():
        pass
        
    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')
