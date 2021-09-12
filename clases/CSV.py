from os import replace
import pandas as pd
from datetime import datetime

class CSV:
    headers = ['Url_user', 'autor', 'autor_shared', 'description','description_shared', 'url_media', 'date_post', 'date_post_shared']

    def __init__(self, rows = []):
        self.rows = rows

    def register(self, name_user):
        dataframe_posts = pd.DataFrame(self.rows, columns = self.headers)
        name_csv = name_user+'_'+self.str_datetime()+'.csv'
        dataframe_posts.to_csv('files/'+name_csv)
    
    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')