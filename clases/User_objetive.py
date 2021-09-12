import time
from clases.User import User 
from clases.Web_driver import Web_driver
from datetime import datetime


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
        time.sleep(40)

        name_png = 'login_'+self.str_datetime()
        self.driver.save_screenshot('screenshot/'+ name_png + '.png')

        all_section = self.driver.find_element_by_css_selector('div.gile2uim')

        posts_items = all_section.find_elements_by_xpath('div[3]/div')
        
        print('Tamano de publicaciones: '+str(len(posts_items)))

        for item in posts_items:
            #print(item.text)

            #imagen del post
            #img.i09qtzwb.n7fi1qx3.datstx6m.pmk7jnqg.j9ispegn.kr520xx4.k4urcfbm.bixrwtb6

            #me gusta y me encanta sumados
            #span.gpro0wi8.pcp91wgn
            try:
                cant_reacciones = item.find_element_by_css_selector('span.gpro0wi8.pcp91wgn').text
                print('reacciones: ' + cant_reacciones)
            except Exception as e:
                cant_reacciones = 0
                print('reacciones: 0')
                print(e)

            #compartidas cantidad
            #div.gtad4xkn xpath span div span
            #split ' ' y tomar el priemer elemento

            #comentarios cantidad
            #div.gtad4xkn xpath div span
            #split ' ' y tomar el priemer elemento

            data_post = []
            try:
                autor_post = 'NOT ASSIGNED'
                date_post = 'NOT ASSIGNED'
                autor_post_shared = 'NOT ASSIGNED'
                date_post_shared = 'NOT ASSIGNED'
                descripcion_post = 'NOT ASSIGNED'
                descripcion_post_shared = 'NOT ASSIGNED'
                url_autor = 'NOT ASSIGNED'
                url_autor_shared = 'NOT ASSIGNED'

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
                        if autor_post_shared == 'NOT ASSIGNED':
                            descripcion_post = segmentos_texto[0].text
                        else:
                            descripcion_post_shared = segmentos_texto[0].text
                    

            except Exception as e:
                    print(e)
            
            data_texts = {
                'autor_post': autor_post,
                'url_autor': url_autor,
                'date_post': date_post,
                'descripcion_post': descripcion_post,
                'autor_post_shared': autor_post_shared,
                'url_autor_shared': url_autor_shared,
                'date_post_shared': date_post_shared,
                'descripcion_post_shared':descripcion_post_shared,
            }
            print(data_texts)

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
        
    def get_date(self, element):
        spam_date = element.find_element_by_css_selector('span.j1lvzwm4.stjgntxs.ni8dbmo4.q9uorilb.gpro0wi8')
        all_spans = spam_date.find_elements_by_xpath('span/span')
        all_spans_date = []
        for span in all_spans:
                                    
            if '' == span.get_attribute('style'):
                all_spans_date.append(span.text)
                                        
        date_post = "".join(all_spans_date)
        return date_post
