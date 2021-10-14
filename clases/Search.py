import time
from typing import Container
from clases.User import User 
from clases.Post import Post 
from clases.Web_driver import Web_driver
from datetime import datetime,date,timedelta
from selenium.webdriver.common.keys import Keys

# Clase que indentifica al usuario objetivo de sacar la informacion
# y ademas se enncarga de buscar cada uno de los posts para ser procesados
class Search(Web_driver):
    
    #atributo que marca el limmite de post que procesaremos en la clase
    limit_post = 20
    def __init__(self, text_find = None, driver = None):
        Web_driver.__init__(self,driver)
        self.data_posts = []
        self.text_find = text_find
    
    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')

    def buscar_terminos(self):
        #input.oajrlxb2.rq0escxv
        input_search = self.driver.find_element_by_css_selector('input.oajrlxb2.rq0escxv')
        self.driver.execute_script("arguments[0].click();", input_search)
        time.sleep(1)
        input_search = self.driver.find_element_by_css_selector('input.oajrlxb2.rq0escxv')
        input_search.send_keys(self.text_find, Keys.ARROW_DOWN)
        time.sleep(10)
        #ul#jsc_c_2y a

        ul = self.driver.find_element_by_css_selector('ul.buofh1pr.cbu4d94t.j83agx80')
        a_list = ul.find_elements_by_css_selector('a')
        pos_fin = len(a_list) - 1
        a = a_list[pos_fin]
        self.driver.execute_script("arguments[0].click();", a)
        

    # Metodo que se encarga de buscar los 10 posts del usuario objetivo para
    # sacar la informacion que requerimos
    def find_posts(self):
        #self.driver.get(self.url)
        time.sleep(30)

        #opcionalmmente podemos sacar uuna captura del muro de publicaciones
        #name_png = 'login_'+self.str_datetime()
        #self.driver.save_screenshot('screenshot/'+ name_png + '.png')

        #se uubican los posts
        self.view_post()

    def extraer_datos_view(self,posts_items):
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
                post.valitade_flags_search()

                row_post = post.to_row_search_row()
                #print(row_post)
                self.data_posts.append(row_post)

                cont = cont + 1

            if cont == self.limit_post:
                break
    
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

        #all_section = self.driver.find_element_by_css_selector('div.tr9rh885.k4urcfbm')
        #all_section = self.driver.find_element_by_css_selector('div.gile2uim')
        all_section = self.driver.find_element_by_css_selector('div.d2edcug0.o7dlgrpb')
        #d2edcug0 o7dlgrpb
        posts_items = all_section.find_elements_by_xpath('div/div')

        try:
            if last_element == posts_items[len(posts_items)-1]:
                return False
            else :
                last_element = posts_items[len(posts_items)-1]
        except:
            return False

        for post_activated in posts_items:

            if post_activated.text != '': #si es vacio significa que el post no cargo la informacion
                
                #aria-posinset.33
                
                try:
                    print('####################')
                    titulo = post_activated.find_element_by_css_selector('h3').text
                    print('titulo: '+ titulo)
                    print('####################')
                    #element_whit_id = post_activated.find_element_by_xpath('div/div/div/div/div/div')
                    element_whit_id = post_activated.find_element_by_css_selector('div.lzcic4wl')
                    #lzcic4wl
                    posinset = element_whit_id.get_attribute('aria-labelledby')
                
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