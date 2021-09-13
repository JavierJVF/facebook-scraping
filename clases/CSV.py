import pandas as pd
from datetime import datetime

class CSV:
    
    def __init__(self, list_dict = [], name_user_file = 'Default'):
        self.list_dict = list_dict
        self.name_user_file = name_user_file.replace(' ','_')

    def register(self):
        dataframe_posts = pd.DataFrame.from_dict(self.list_dict)
        name_csv = self.name_user_file +'_'+self.str_datetime()+'.csv'
        dataframe_posts.to_csv('files/'+name_csv, index = False, header=True, encoding='utf-8')
    
    def str_datetime(self):
        return str(datetime.now()).replace(':','_').replace(' ','_')