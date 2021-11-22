import time
from typing import Container
from clases.User import User 
from clases_instagram.post import Post 
from clases_instagram.Web_driver import Web_driver
from datetime import datetime,date,timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Clase que indentifica al usuario objetivo de sacar la informacion
# y ademas se enncarga de buscar cada uno de los posts para ser procesados
class Search(Web_driver):
    
    #atributo que marca el limmite de post que procesaremos en la clase
    limit_post = 20
    def __init__(self, text_find = None, driver = None, link = None):
        Web_driver.__init__(self,driver)
        self.data_posts = []
        self.text_find = text_find
        self.link = link
    
    def find_post_by_link(self):
        
        self.driver.get(self.link)
        time.sleep(15)
        '''name_png = 'view_instagram_'+self.str_datetime()
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')'''

        self.select_post_element()

    def select_post_element(self):
        
        post = Post(None)
        post.set_driver_global(self.driver)
        post.click_plus()
        post.click_ver_respuestas()
        self.data_posts =  post.find_comments()
        #print(self.data_posts)

        '''name_png = 'view_answers_'+self.str_datetime()
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')'''

    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')

    def buscar_terminos(self):
        #input.oajrlxb2.rq0escxv
        time.sleep(15)
        input_search = self.driver.find_element_by_css_selector('input.XTCLo.x3qfX')
        self.driver.execute_script("arguments[0].click();", input_search)
        time.sleep(5)
        input_search = self.driver.find_element_by_css_selector('input.XTCLo.x3qfX')
        input_search.send_keys(self.text_find, Keys.ARROW_DOWN)
        time.sleep(5)
        #error aqui
        a = self.driver.find_elements_by_css_selector('a.-qQT3')[0]
        self.driver.execute_script("arguments[0].click();", a)
        time.sleep(15)
        name_png = 'search_instagram'+self.str_datetime()
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')

    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')
        
    def extraer_datos_view(self, posts_elements):
        count = 0
        for element_post in posts_elements:
            try:
                post = Post(element_post)
                post.find_images()
                ActionChains(self.driver).move_to_element(post.img).perform()
                time.sleep(2)
                post.find_likes_cant()
                post.find_comments_cant()

                #click imagen
                self.driver.execute_script("arguments[0].click();", post.img)
                time.sleep(3)
                post.setdriver(self.driver)

                post.find_datetime()
                post.find_username()
                post.find_descripcion()
                post.find_ubicacion()
                #button x
                #div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG button.wpO6b
                button_x = self.driver.find_element_by_css_selector('div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG button.wpO6b')
                self.driver.execute_script("arguments[0].click();", button_x)
                '''item = {
                    'img_src': img_src,
                    'fav_cant':fav_cant,
                    'comment_cant':comment_cant,
                    'date_time': date_time,
                    'username': username,
                    'username_url': username_url,
                    'descripcion_text': descripcion_text,
                    'ubicacion': ubicacion
                }'''
                self.data_posts.append(post.to_row())
                '''if count==10:
                    break'''
                count = count + 1
                print(count)
            except:
                print('error post')

    # Metodo que se encarga de buscar los 10 posts del usuario objetivo para
    # sacar la informacion que requerimos
    def find_posts(self):
        #v1Nh3 kIKUG  _bz0w
        self.view_post()

      
    # Metodo para hacer scroll hacia abajo en la pagina
    def make_scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #sleep para esperarr a que la informacion nueva que se muestra por el scroll cargue
        time.sleep(10)


    # Metodo para hacer scroll hacia abajo en la pagina y
    # hacer que se muestren mas posts de forma dinamica
    # hasta llegar al numero de posts que necesitamos
    def view_post(self, num_post = 0,posinsetlist=[],last_element = None):
        try:
            self.make_scroll()
        except:
            print('---------------------')
            return False #en caso de que no se pueda hacer mas scroll retornamos false para indicar que es el tope

        list_posts_acum = []

        posts_items = self.driver.find_elements_by_css_selector('div.v1Nh3.kIKUG._bz0w')
        print('dentro de view post')
        print(str(len(posts_items)))

        try:
            if last_element == posts_items[len(posts_items)-1]:
                return False
            else :
                last_element = posts_items[len(posts_items)-1]
        except:
            return False

        for post_activated in posts_items:

            if True: #si es vacio significa que el post no cargo la informacion
                
                #aria-posinset.33
                
                try:
                    print('####################')
                    href = post_activated.find_element_by_css_selector('a').get_attribute('href')
                    print('href: '+ href)
                    print('####################')
                    posinset = href
                
                except Exception as e:
                    #print(e)
                    posinset = None
                
                if posinset!=None:
                    print('id post: '+ str(posinset))
                    if posinset in posinsetlist:
                        pass
                    else:
                        posinsetlist.append(posinset)
                        list_posts_acum.append(post_activated)
                        num_post = num_post + 1
                        print('num_post: ' + str(num_post))

        if num_post < self.limit_post: # sino alcanza el limite de posts vuelve a llamar al mismo metodo hasta llegar
            self.extraer_datos_view(list_posts_acum)
            estatus_post_view = self.view_post(num_post,posinsetlist, last_element)


            if estatus_post_view == False: # si es false quiere decir quue ya no hay mas posts y toma el de la iteacion anterior
                return False

        else:
            self.extraer_datos_view(list_posts_acum)
            return False

        return True