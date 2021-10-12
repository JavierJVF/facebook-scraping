from clases.Fecha import Fecha 

#CLASE para Extraer y gestionar los datos de los posts de los usuarios objetivos
class Post:

    #el parametro para inicializar es un elemento obtenido del webdriver
    # en este caso seria el elemento padre de cada post
    def __init__(self,driver_post):
        self.driver_post = driver_post
        self.autor_post = 'NOT ASSIGNED'
        self.date_post = 'NOT ASSIGNED'
        self.autor_post_shared = 'NOT ASSIGNED'
        self.date_post_shared = 'NOT ASSIGNED'
        self.descripcion_post = 'NOT ASSIGNED'
        self.descripcion_post_shared = 'NOT ASSIGNED'
        self.url_autor = 'NOT ASSIGNED'
        self.url_autor_shared = 'NOT ASSIGNED'
        self.url_images = []
        self.url_video = 'NOT ASSIGNED'
        self.cant_reacciones = 0
        self.cant_shared = 0
        self.cant_comments = 0
        self.enlace_shared = 'NOT ASSIGNED'
        self.a_element_in_titulo = []

        # descripcion de los atributos
        '''
        autor_post: el autor de la publicacion
        url_autor: la url del perfil del autor del post
        date_post: fecha de la publicacion
        descripcion_post: la descripcion de la publicacion del autor
        autor_post_shared: el autor de la publicacion original, que ha sido compartida por el autor del post
        url_autor_shared: la url del autor de la publicacion original, que ha sido compartida por el autor del post
        date_post_shared: fecha de la publicacion original
        descripcion_post_shared:  descripcion de la publicacion original
        enlace_shared: url del enlace que ha sido compartido, en caso de tener
        url_image: urls de las imagenes de la publicacion
        url_video: url del video de la publicacion
        cant_reacciones: cantidad de reacciones de la publicacion
        cant_shared: cantidad de veces compartidas de la publicacion
        cant_comments: cantidad de comentarios de la publicacion
        tagged_someone: el autor etiqueto a alguien
        someone_tagged_me: el autor has sido etiquetado
        shared: publicacion compartida
        has_enlace: La puublicacion tiene un enlace
        has_image: la publicacion tiene imagenes
        has_video: la publicacion tiene video
        '''


    # Metodo que busca imagenes en el post
    # si la tiene entonces extrae el/los src
    def find_images(self):
        
        try:
            images = self.driver_post.find_elements_by_css_selector('img.i09qtzwb.n7fi1qx3.datstx6m.pmk7jnqg.j9ispegn.kr520xx4.k4urcfbm')
            for image in images:
                self.url_images.append(image.get_attribute('src'))
        except:
            self.url_images = []

    # Metodo que busca un video en el post
    # si lo tiene entoces extrae el src
    def find_video(self):
        try:
            video = self.driver_post.find_element_by_css_selector('video.k4urcfbm.datstx6m.a8c37x1j')
            self.url_video = video.get_attribute('src').replace('blob:','')
        except:
            self.url_video = 'NOT ASSIGNED'
    
    # Metodo que indentifica la cantidad de reacciones del post
    def find_cant_reacciones(self):
        try:
            self.cant_reacciones = int(self.driver_post.find_element_by_css_selector('span.gpro0wi8.pcp91wgn').text)
        except Exception as e:
            self.cant_reacciones = 0
            #print(e)
    
    # Metodo que indentifica la cantidad de comentarios y veces compartidas del post
    def find_cant_comments_and_shared(self):
        try:
            container_shared_comments = self.driver_post.find_element_by_css_selector('div.gtad4xkn')

            self.find_cant_shared(container_shared_comments)
            self.find_cant_comments(container_shared_comments)
        except Exception as e:
            self.cant_shared = 0
            self.cant_comments = 0
    
    #metodo que identifica la cantidad de comentarios pasando por parametro el elemento padre
    def find_cant_comments(self,container_element):
        try:
            cant_shared_text = container_element.find_element_by_xpath('span/div/span').text
            self.cant_shared = int(cant_shared_text.split(' ')[0])
        except:
            self.cant_shared = 0
    
    #metodo que identifica la cantidad de veces compartidas pasando por parametro el elemento padre
    def find_cant_shared(self,container_element):
        try:
            cant_comments_text = container_element.find_element_by_xpath('div/span').text
            self.cant_comments = int(cant_comments_text.split(' ')[0])
        except:
            self.cant_comments = 0
    
    # Metodo que busca un enlace en el post
    # si lo tiene entoces extrae la url y la descripcion de este en caso de tenerla
    def find_link_shared(self):
        try:
            element_a = self.driver_post.find_element_by_css_selector('a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.datstx6m.k4urcfbm')
            self.enlace_shared = element_a.get_attribute('href')

            container_description_enlace = self.driver_post.find_element_by_css_selector('div.b3i9ofy5.s1tcr66n.l9j0dhe7.p8dawk7l')
            self.descripcion_post_shared = container_description_enlace.find_element_by_css_selector('div.qzhwtbm6.knvmm38d').text
        except:
            self.enlace_shared = 'NOT ASSIGNED'
            self.descripcion_post_shared = 'NOT ASSIGNED'
    
    # Metodo que identifica al autor del post y si es compartido entonces tambien al autor original
    # Metodo que identifica a la fecha de emision del post y si es compartido entonces tambien la fecha de emision del post original
    # Metodo que busca la descripcion del post y si es compartido entonces tambien la descripcion del post original
    def find_autores_and_description_info(self):
        try:
            elements_text = self.driver_post.find_elements_by_css_selector('div.j83agx80.cbu4d94t.ew0dbk1b.irj2b8pg')
            for element in elements_text:
                segmentos_texto = element.find_elements_by_css_selector('div.qzhwtbm6.knvmm38d')
                cant_segmento = len(segmentos_texto)
                
                if cant_segmento == 2: # si es igual a dos significa nombre y fecha
                    if self.autor_post == 'NOT ASSIGNED': # si es nombre y fecha y el autor no esta identificado significa que es el, por orden
                        self.get_data_text_of_post(segmentos_texto)
                    else:
                        self.get_data_shared(segmentos_texto)

                elif cant_segmento == 1: # si es igual a 1 significa texto de descripcion
                    self.set_descriptions(segmentos_texto)
                    
        except Exception as e:
            print(e)
    
    # Metodo que busca la descripcion del post y si es compartido entonces la descripcion del post original
    # por parametro se le pasa el elemento padre
    def set_descriptions(self,segmentos_texto):
        if self.descripcion_post_shared != segmentos_texto[0].text:
            if self.autor_post_shared == 'NOT ASSIGNED':
                self.descripcion_post = segmentos_texto[0].text.replace('\n',' ')
            else:
                self.descripcion_post_shared = segmentos_texto[0].text.replace('\n',' ')
    
    # Metodo que busca la el autor del post y si es compartido entonces el autor del post original
    # tambien etrae la url del autor en cuestion
    # ademas extrae la fecha de publicacion del post y si es compartido entonces extrae la del post compartido
    # por parametro se le pasa el elemento padre
    def get_data_text_of_post(self,segmentos_texto):
        h2 =  segmentos_texto[0].find_elements_by_css_selector('h3')
        #h2 =  segmentos_texto[0].find_elements_by_css_selector('h2')
        
        if(len(h2) == 1): # si es 1 significa que tiene un h2 y es el del autor de la publicacion
            self.a_element_in_titulo = h2[0].find_elements_by_css_selector('a')
            self.url_autor = self.a_element_in_titulo[0].get_attribute('href')
            self.autor_post = self.a_element_in_titulo[0].text      
            self.date_post = self.get_date(segmentos_texto[1])
                                        
        else:
            self.get_data_shared(segmentos_texto)
    
    # metodo quue extrae datos solo del autor, la fecha, la url del autor de un post compartido
    def get_data_shared(self,segmentos_texto):
        h3 =  segmentos_texto[0].find_elements_by_css_selector('h3')
        if(len(h3) == 1): #si es 1 significa que es el autor de la publicacion original yy que es compartido
            a_element = h3[0].find_element_by_css_selector('a')
            self.url_autor_shared = a_element.get_attribute('href')
            self.autor_post_shared = a_element.text
            self.date_post_shared = self.get_date(segmentos_texto[1])
    
    # Verifica si es un post compartido
    def valiate_flag_shared(self):
        if self.autor_post_shared != 'NOT ASSIGNED':
            self.FLAG_shared = True
        else:
            self.FLAG_shared = False
    
    # Verifica si es un post donde te etiquetarion y etiquetaste o no es etiquetado
    def validate_flags_tagged(self, url, name):
        if len(self.a_element_in_titulo) > 1:
            if url in self.url_autor:
                self.FLAG_tagged_someone = True
                self.FLAG_someone_tagged_me = False
            else:
                self.FLAG_tagged_someone = False
                self.FLAG_someone_tagged_me = True
        else:
            self.FLAG_tagged_someone = False
            self.FLAG_someone_tagged_me = False
    
    # Verifica si es un post con un enlace compartido
    def validate_flag_link(self):
        if self.enlace_shared != 'NOT ASSIGNED':
            self.FLAG_enlace = True
        else:
            self.FLAG_enlace = False
    
    # Verifica si es un post con un video
    def validate_flag_video(self):
        if self.url_video != 'NOT ASSIGNED':
            self.FLAG_video = True
        else:
            self.FLAG_video = False

    # Verifica si es un post con imagen
    def validate_flag_image(self):
        if len(self.url_images) == 0:
            self.FLAG_image = False
        else:
            self.FLAG_image = True
    
    # metodo quue llama a los metodos de verificacion de Banderas
    def valitade_flags(self, url, name):
        self.valiate_flag_shared()
        self.validate_flags_tagged(url,name)
        self.validate_flag_link()
        self.validate_flag_video()
        self.validate_flag_image()
    
    def valitade_flags_search(self):
        self.valiate_flag_shared()
        self.validate_flag_link()
        self.validate_flag_video()
        self.validate_flag_image()
    
    # obtiene todos los atributos del objeto y los coloca en un dict, es usado para cargar una lista
    def to_row(self):
        return {
            'autor_post': self.autor_post,
            'url_autor': self.url_autor,
            'date_post': self.date_post,
            'descripcion_post': self.descripcion_post,
            'autor_post_shared': self.autor_post_shared,
            'url_autor_shared': self.url_autor_shared,
            'date_post_shared': self.date_post_shared,
            'descripcion_post_shared': self.descripcion_post_shared,
            'enlace_shared': self.enlace_shared,
            'url_image': str(self.url_images),
            'url_video': self.url_video,
            'cant_reacciones': self.cant_reacciones,
            'cant_shared': self.cant_shared,
            'cant_comments': self.cant_comments,
            'tagged_someone': self.FLAG_tagged_someone,
            'someone_tagged_me': self.FLAG_someone_tagged_me,
            'shared': self.FLAG_shared,
            'has_enlace': self.FLAG_enlace,
            'has_image': self.FLAG_image,
            'has_video': self.FLAG_video,
        }
    
    def to_row_search(self):
        return {
            'autor_post': self.autor_post,
            'url_autor': self.url_autor,
            'date_post': self.date_post,
            'descripcion_post': self.descripcion_post,
            'autor_post_shared': self.autor_post_shared,
            'url_autor_shared': self.url_autor_shared,
            'date_post_shared': self.date_post_shared,
            'descripcion_post_shared': self.descripcion_post_shared,
            'enlace_shared': self.enlace_shared,
            'url_image': str(self.url_images),
            'url_video': self.url_video,
            'cant_reacciones': self.cant_reacciones,
            'cant_shared': self.cant_shared,
            'cant_comments': self.cant_comments,
            'tagged_someone': 'NULL',
            'someone_tagged_me': 'NULL',
            'shared': self.FLAG_shared,
            'has_enlace': self.FLAG_enlace,
            'has_image': self.FLAG_image,
            'has_video': self.FLAG_video,
        }
    
    # metodo que extrae la informacion de la fecha del post que viene encriptada o enmascarada
    def get_date(self, element):
        spam_date = element.find_element_by_css_selector('span.j1lvzwm4.stjgntxs.ni8dbmo4.q9uorilb.gpro0wi8')
        all_spans = spam_date.find_elements_by_xpath('span/span')
        all_spans_date = []
        for span in all_spans:
                                    
            if '' == span.get_attribute('style'):
                all_spans_date.append(span.text)
                                        
        date_post = "".join(all_spans_date)

        date_obj = Fecha(date_post)

        date_obj.validate_yesterday_or_today()
        date_post = date_obj.date_format
        return date_post