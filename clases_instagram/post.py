from clases.Fecha import Fecha 
import time

#CLASE para Extraer y gestionar los datos de los posts de los usuarios objetivos
class Post:

    #el parametro para inicializar es un elemento obtenido del webdriver
    # en este caso seria el elemento padre de cada post
    def __init__(self,driver_post):
        self.driver_post = driver_post
        self.img_src = 'NOT ASSIGNED'
        self.img = 'NOT ASSIGNED'
        self.fav_cant = 'NOT ASSIGNED'
        self.comment_cant = 'NOT ASSIGNED'
        self.date_time = 'NOT ASSIGNED'
        self.username = 'NOT ASSIGNED'
        self.username_url = 'NOT ASSIGNED'
        self.descripcion_text = 'NOT ASSIGNED'
        self.ubicacion = 'NOT ASSIGNED'

        self.driver_global = None
    
    def find_images(self):
        try:
            self.img = self.driver_post.find_element_by_css_selector('img.FFVAD')
            self.img_src = self.img.get_attribute('src')
        except:
            print('error image')
    
    def find_comments(self):
        comments = self.driver_global.find_elements_by_css_selector('ul.Mr508 li.gElp9.rUo9f')

        list_comment = []
        for item in comments:
            try:
                element = self.get_info_comment(item)

                list_comment.append(element)
            except:
                pass
        return list_comment
    
    def get_info_comment(self,item):
        

        container_comment = item.find_element_by_css_selector('div.C4VMK')
        a_username = container_comment.find_element_by_css_selector('a.sqdOP.yWX7d._8A5w5.ZIAjV')
        username = a_username.text
        username_url = a_username.get_attribute('href')
        comment_text = container_comment.find_element_by_xpath('span').text
        return [username,
            username_url,
            comment_text]
    
    def click_ver_respuestas(self):
        time.sleep(4)
        mas_respuestas = self.driver_global.find_elements_by_css_selector('button.sqdOP.yWX7d.y3zKF span.EizgU')
        list_mas_respuestas = []
        for element in mas_respuestas:
            print(element.text.upper())
            if 'Ver'.upper() in element.text.upper():
                list_mas_respuestas.append(element)

        if len(list_mas_respuestas) > 0:
            for element in list_mas_respuestas:
                self.driver_global.execute_script("arguments[0].click();", element)
            self.click_ver_respuestas()
    
    def click_plus(self):
        
        try:
            comments = self.driver_global.find_elements_by_css_selector('ul.Mr508 li.gElp9.rUo9f')
            plus_button = self.driver_global.find_element_by_css_selector('div.qF0y9.Igw0E.IwRSH.YBx95._4EzTm.NUiEW  button.wpO6b div.QBdPU')
            self.driver_global.execute_script("arguments[0].click();", plus_button)
            time.sleep(5)
            comments_update = self.driver_global.find_elements_by_css_selector('ul.Mr508 li.gElp9.rUo9f')
            if comments[len(comments)-1] != comments_update[len(comments_update)-1]:
            
                self.click_plus()
        except:
            print('no tiene mas comentarios')

        
    
    def find_likes_cant(self):
        try:

            fav_tag = self.driver_post.find_element_by_css_selector('span.coreSpriteHeartSmall')
            self.fav_cant = fav_tag.find_element_by_xpath('../span[1]').text
            #print(fav_cant)
        except:
            self.fav_cant = '0'
        
        if self.fav_cant == '':
            self.fav_cant = '0'
    
    def find_comments_cant(self):
        try:
            comment_tag = self.driver_post.find_element_by_css_selector('span.coreSpriteSpeechBubbleSmall')
            self.comment_cant = comment_tag.find_element_by_xpath('../span[1]').text
            #print(comment_cant)
        except:
            self.comment_cant = '0'
        
        if self.comment_cant == '':
            self.comment_cant = '0'
    
    def find_datetime(self):
        try:

            date = self.driver_post.find_element_by_css_selector('time._1o9PC.Nzb55')
            self.date_time = date.get_attribute('datetime')
        except:
            print('erro date_time')
            self.date_time = 'None'
    
    def find_username(self):
        try:
            a_username = self.driver_post.find_element_by_css_selector('div.e1e1d a.sqdOP.yWX7d._8A5w5.ZIAjV')
            self.username = a_username.text
            self.username_url = a_username.get_attribute('href')
        except:
            print('erro username')
            self.username_url = 'None'
            self.username = 'None'

    def find_descripcion(self):
        try:

            ul_descripcion = self.driver_post.find_element_by_css_selector('ul.XQXOT')
            descripcion_element_all = ul_descripcion.find_element_by_xpath('div')
            descripcion_element = descripcion_element_all.find_element_by_css_selector('div.C4VMK')
            self.descripcion_text = descripcion_element.find_element_by_xpath('span').text
        except:
            print('descripcion error')
            self.descripcion_text = 'None'
    
    def find_descripcion(self):
        try:

            ul_descripcion = self.driver_post.find_element_by_css_selector('ul.XQXOT')
            descripcion_element_all = ul_descripcion.find_element_by_xpath('div')
            descripcion_element = descripcion_element_all.find_element_by_css_selector('div.C4VMK')
            self.descripcion_text = descripcion_element.find_element_by_xpath('span').text
        except:
            print('descripcion error')
            self.descripcion_text = 'None'
    
    def find_ubicacion(self):
        try:

            self.ubicacion = self.driver_post.find_element_by_css_selector('a.O4GlU').text
        except:
            self.ubicacion = 'NO ASIGNADO'
            print('error ubicacion')
    
    def to_row(self):
        return [
            self.img_src,
            self.fav_cant,
            self.comment_cant,
            self.date_time,
            self.username,
            self.username_url,
            self.descripcion_text,
            self.ubicacion]
    
    def set_driver_global(self, driver):
        self.driver_global = driver

    def setdriver(self,driver):
        self.driver_post = driver