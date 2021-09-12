from clases.CSV import CSV
from clases.Account import Account
from clases.Account import Account
from clases.User_objetive import User_objetive
from clases.CSV import CSV
from clases.Post import Post

account = Account('', '')
account.init_webdriver()
account.login()
#account.find_friends()
account.set_list()
account.select_user_objetive()
account.user_obetive.find_posts()

'''user_obetive = User_objetive('ssss' , 'saasas')
print(user_obetive)
print(user_obetive.name)
'''
#print(account.list_frends)
print(account.user_obetive)

#User_objetive(friend.url , friend.name, account.driver)
account.close_webdriver()

print('Fin proceso')
