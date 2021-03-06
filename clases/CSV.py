#import pandas as pd
from datetime import datetime
import csv

# Clase quue realiza toda la creacion y gestion de un CSV
class CSV:
    
    #se inicializa con la lista de diccionarios y
    # el nombre del uusuario para facilitar su identificacion en el directorio
    def __init__(self, list_dict = [], name_user_file = 'Default'):
        self.list_dict = list_dict
        self.name_user_file = name_user_file.replace(' ','_')

    def register_comments(self):
        name_csv = 'files/' + self.name_user_file +'_'+self.str_datetime()+'.csv'
        self.create_csv_only_for_comments(name_csv)
        for x in self.list_dict:
            self.save_facebook_comment_to_csv(x,name_csv)


    #Metodo que registra una lista de diccionarios en un CSV en formato uft-8
    def register(self):
        name_csv = 'files/' + self.name_user_file +'_'+self.str_datetime()+'.csv'
        self.create_csv_only(name_csv)
        for x in self.list_dict:
            self.save_facebook_data_to_csv(x,name_csv)
    
    def create_csv_only_for_comments(self, filepath, mode='w'):
        header = ['id','name_user','url_user','comment_text','comment_main']

        with open(filepath, mode=mode, newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    
    '''def register_dict(self):
        dataframe_posts = pd.DataFrame.from_dict(self.list_dict)
        name_csv = 'files/' + self.name_user_file +'_'+self.str_datetime()+'.csv'
        dataframe_posts.to_csv('files/'+name_csv, index = False, header=True, encoding='utf-8')'''
    
    def save_facebook_data_to_csv(self,records, filepath, mode='a+'):
        header = ['autor_post','url_autor','date_post','descripcion_post','autor_post_shared','url_autor_shared','date_post_shared','descripcion_post_shared','enlace_shared','url_image','url_video','cant_reacciones','cant_shared','cant_comments','tagged_someone','someone_tagged_me','shared','has_enlace','has_image','has_video']

        with open(filepath, mode=mode, newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if mode == 'w':
                writer.writerow(header)
            if records:
                writer.writerow(records)
    
    def save_facebook_comment_to_csv(self,records, filepath, mode='a+'):
        header = ['id','name_user','url_user','comment_text','comment_main']

        with open(filepath, mode=mode, newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if mode == 'w':
                writer.writerow(header)
            if records:
                writer.writerow(records)
    
    def create_csv_only(self, filepath, mode='w'):
        header = ['autor_post','url_autor','date_post','descripcion_post','autor_post_shared','url_autor_shared','date_post_shared','descripcion_post_shared','enlace_shared','url_image','url_video','cant_reacciones','cant_shared','cant_comments','tagged_someone','someone_tagged_me','shared','has_enlace','has_image','has_video']

        with open(filepath, mode=mode, newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    
    # metodo para establecer la fecha y hora como un string 
    # y usarlo como nombres de los CSV junto con el nombre del usuario
    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')