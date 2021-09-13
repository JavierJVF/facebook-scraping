import time
from typing import Container
from clases.User import User 
from clases.Web_driver import Web_driver
from datetime import datetime,date,timedelta


class User_objetive(User,Web_driver):
    def __init__(self, url, name = None, driver = None):
        User.__init__(self,name)
        Web_driver.__init__(self,driver)

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
        data_post = []
        for item in posts_items:
            if item.text != '':
                autor_post = 'NOT ASSIGNED'
                date_post = 'NOT ASSIGNED'
                autor_post_shared = 'NOT ASSIGNED'
                date_post_shared = 'NOT ASSIGNED'
                descripcion_post = 'NOT ASSIGNED'
                descripcion_post_shared = 'NOT ASSIGNED'
                url_autor = 'NOT ASSIGNED'
                url_autor_shared = 'NOT ASSIGNED'
                #print(item.text)

                #imagen del post
                #img.i09qtzwb.n7fi1qx3.datstx6m.pmk7jnqg.j9ispegn.kr520xx4.k4urcfbm.bixrwtb6
                url_images = []
                try:
                    images = item.find_elements_by_css_selector('img.i09qtzwb.n7fi1qx3.datstx6m.pmk7jnqg.j9ispegn.kr520xx4.k4urcfbm')
                    for image in images:
                        url_images.append(image.get_attribute('src'))
                except:
                    url_images = []
                
                
                try:
                    video = item.find_element_by_css_selector('video.k4urcfbm.datstx6m.a8c37x1j')
                    url_video = video.get_attribute('src').replace('blob:','')
                except:
                    url_video = 'NOT ASSIGNED'


                #Cantidad de reacciones
                #span.gpro0wi8.pcp91wgn
                try:
                    cant_reacciones = item.find_element_by_css_selector('span.gpro0wi8.pcp91wgn').text
                except Exception as e:
                    cant_reacciones = 0
                    #print(e)
                
                try:
                    container_shared_comments = item.find_element_by_css_selector('div.gtad4xkn')
                    try:
                        cant_shared_text = container_shared_comments.find_element_by_xpath('span/div/span').text
                        cant_shared = int(cant_shared_text.split(' ')[0])
                    except:
                        cant_shared = 0

                    try:
                        cant_comments_text = container_shared_comments.find_element_by_xpath('div/span').text
                        cant_shared = int(cant_comments_text.split(' ')[0])
                    except:
                        cant_comments = 0
                except Exception as e:
                    cant_shared = 0
                    cant_comments = 0
                    #print(e)

                #compartidas cantidad
                #div.gtad4xkn xpath span div span
                #split ' ' y tomar el priemer elemento

                #comentarios cantidad
                #div.gtad4xkn xpath div span
                #split ' ' y tomar el priemer elemento

                #enlace
                #a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.datstx6m.k4urcfbm
                try:
                    element_a = item.find_element_by_css_selector('a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.datstx6m.k4urcfbm')
                    enlace_shared = element_a.get_attribute('href')

                    container_description_enlace = item.find_element_by_css_selector('div.b3i9ofy5.s1tcr66n.l9j0dhe7.p8dawk7l')
                    descripcion_post_shared = item.find_element_by_css_selector('div.qzhwtbm6.knvmm38d').text
                except:
                    enlace_shared = 'NOT ASSIGNED'
                    descripcion_post_shared = 'NOT ASSIGNED'

                try:

                    elements_text = item.find_elements_by_css_selector('div.j83agx80.cbu4d94t.ew0dbk1b.irj2b8pg')
                    for element in elements_text:
                        segmentos_texto = element.find_elements_by_css_selector('div.qzhwtbm6.knvmm38d')
                        cant_segmento = len(segmentos_texto)
                        
                        if cant_segmento == 2:
                            if autor_post == 'NOT ASSIGNED':
                                h2 =  segmentos_texto[0].find_elements_by_css_selector('h2')
                                if(len(h2) == 1):
                                    url_autor = h2[0].find_element_by_css_selector('a').get_attribute('href')
                                    autor_post = h2[0].text
                                    
                                    date_post = self.get_date(segmentos_texto[1])
                                        
                                else:
                                    h3 =  segmentos_texto[0].find_elements_by_css_selector('h3')
                                    if(len(h3) == 1):
                                        url_autor_shared = h3[0].find_element_by_css_selector('a').get_attribute('href')
                                        autor_post_shared = h3[0].text
                                        date_post_shared = self.get_date(segmentos_texto[1])
                            else:
                                h3 =  segmentos_texto[0].find_elements_by_css_selector('h3')
                                if(len(h3) == 1):
                                    url_autor_shared = h3[0].find_element_by_css_selector('a').get_attribute('href')
                                    autor_post_shared = h3[0].text
                                    date_post_shared = self.get_date(segmentos_texto[1])

                        elif cant_segmento == 1:
                            if descripcion_post_shared != segmentos_texto[0].text:
                                if autor_post_shared == 'NOT ASSIGNED':
                                    descripcion_post = segmentos_texto[0].text
                                else:
                                    descripcion_post_shared = segmentos_texto[0].text
                        

                except Exception as e:
                        print(e)
                
                if autor_post_shared != 'NOT ASSIGNED':
                    FLAG_shared = True
                else:
                    FLAG_shared = False
                
                if autor_post != self.name:
                    FLAG_etiquetado = True
                else:
                    FLAG_etiquetado = False
                
                if enlace_shared != 'NOT ASSIGNED':
                    FLAG_enlace = True
                else:
                    FLAG_enlace = False

                row_post = {
                    'autor_post': autor_post,
                    'url_autor': url_autor,
                    'date_post': date_post,
                    'descripcion_post': descripcion_post,
                    'autor_post_shared': autor_post_shared,
                    'url_autor_shared': url_autor_shared,
                    'date_post_shared': date_post_shared,
                    'descripcion_post_shared':descripcion_post_shared,
                    'enlace_shared': enlace_shared,
                    'url_image': str(url_images),
                    'url_video': url_video,
                    'cant_reacciones': cant_reacciones,
                    'cant_shared': cant_shared,
                    'cant_comments': cant_comments,
                    'etiquetado': FLAG_etiquetado,
                    'shared': FLAG_shared,
                    'enlace': FLAG_enlace,
                }
                print(row_post)
                data_post.append(row_post)

                #container info tex
                #div.j83agx80.cbu4d94t.ew0dbk1b.irj2b8pg
                #separaciones
                #div.qzhwtbm6.knvmm38d      si son dos es nombre y fecha si es una es desrripcion

                #container de post compartido
                #hqeojc4l
                #texto
                #div.ecm0bbzt.hv4rvrfc.ihqw7lf3.dati1w0a div.j83agx80.cbu4d94t.ew0dbk1b.irj2b8pg div.qzhwtbm6.knvmm38d div.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.c1et5uql.ii04i59q

                #numero de egustas modal
                #span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.fe6kdd0r.mau55g9w.c8b282yb.iv3no6db.jq4qci2q.a3bd9o3v.lrazzd5p.q66pz984
                cont = cont + 1

            if cont == 6:
                break

    def get_date(self, element):
        spam_date = element.find_element_by_css_selector('span.j1lvzwm4.stjgntxs.ni8dbmo4.q9uorilb.gpro0wi8')
        all_spans = spam_date.find_elements_by_xpath('span/span')
        all_spans_date = []
        for span in all_spans:
                                    
            if '' == span.get_attribute('style'):
                all_spans_date.append(span.text)
                                        
        date_post = "".join(all_spans_date)

        date_post = self.validate_yesterday_or_today(date_post)
        return date_post
    
    def getDateMonthDict(self):
        return{
            1:'Enero',
            2:'Febrero',
            3:'Marzo',
            4:'Abril',
            5:'Mayo',
            6:'Junio',
            7:'Julio',
            8:'Agosto',
            9:'Septiembre',
            10:'Octubre',
            11:'Noviembre',
            12:'Diciembre',
        }
    
    def getDateNow(self):
        now = datetime.now()
        mes = self.getDateMonthDict().get(now.month)
        day = now.day
        date_format = str(day)+' de '+mes
        return date_format
    
    def getDateYesterday(self):
        date_ = date.today() - timedelta(days=1)
        mes = self.getDateMonthDict().get(date_.month)
        day = date_.day
        date_format = str(day)+' de '+mes
        return date_format

    def validate_yesterday_or_today(self, date_):
        if 'horas' in date_ or 'minutos' in date_ or 'segundos_date' in date_:
            return self.getDateNow()

        if 'ayer' in date_:
            return self.getDateYesterday()
        return date_

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

        print('Tamano de publicaciones: '+str(len(posts_items)))
        num_post = 0
        for post_activated in posts_items:
            if post_activated.text != '':
                num_post = num_post + 1
        if num_post < 6:
            posts = self.view_post()
            if posts == False:
                return posts_items
        else:
            return posts_items
        return posts