import pandas as pd
from datetime import datetime

# Clase quue realiza toda la creacion y gestion de un CSV
class CSV:
    
    #se inicializa con la lista de diccionarios y
    # el nombre del uusuario para facilitar su identificacion en el directorio
    def __init__(self, list_dict = [], name_user_file = 'Default'):
        self.list_dict = list_dict
        self.name_user_file = name_user_file.replace(' ','_')

    #Metodo que registra una lista de diccionarios en un CSV en formato uft-8
    def register(self):
        dataframe_posts = pd.DataFrame.from_dict(self.list_dict)
        name_csv = self.name_user_file +'_'+self.str_datetime()+'.csv'
        dataframe_posts.to_csv('files/'+name_csv, index = False, header=True, encoding='utf-8')
    
    # metodo para establecer la fecha y hora como un string 
    # y usarlo como nombres de los CSV junto con el nombre del usuario
    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')