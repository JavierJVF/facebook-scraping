import time
from typing import Container
from clases.User import User 
from clases.Post import Post 
from clases.Web_driver import Web_driver
from datetime import datetime,date,timedelta


class User_objetive(User,Web_driver):
    limit_post = 10
    def __init__(self, url, name = None, driver = None):
        User.__init__(self,name)
        Web_driver.__init__(self,driver)
        self.data_posts = []
        self.url = url
    
    def __str__(self) -> str:
        return User.__str__(self) + '\nURL: ' + self.url
    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')

    def find_posts(self):
        self.driver.get(self.url)
        time.sleep(30)

        '''name_png = 'login_'+self.str_datetime()
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')'''

        posts_items = self.view_post()

        cont = 0
        
        for item in posts_items:
            if item.text != '':
                post = Post(item)
                post.find_images()
                post.find_video()
                post.find_cant_reacciones()
                post.find_cant_comments_and_shared()
                post.find_link_shared()
                post.find_autores_and_description_info()
                post.valitade_flags(self.url, self.name)

                row_post = post.to_row()
                #print(row_post)
                self.data_posts.append(row_post)

                cont = cont + 1

            if cont == self.limit_post:
                break

    

    def make_scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(10)
    
    def view_post(self):
        try:
            self.make_scroll()
        except:
            return False

        all_section = self.driver.find_element_by_css_selector('div.gile2uim')
        posts_items = all_section.find_elements_by_xpath('div[3]/div')

        #print('Numero de publicaciones: '+str(len(posts_items)))
        num_post = 0
        for post_activated in posts_items:
            if post_activated.text != '':
                num_post = num_post + 1
        if num_post < self.limit_post:
            posts = self.view_post()
            if posts == False:
                return posts_items
        else:
            return posts_items
        return posts