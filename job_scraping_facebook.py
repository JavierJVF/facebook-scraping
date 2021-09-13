from clases.CSV import CSV
from clases.Account import Account

account = Account('', '')
account.init_webdriver()
account.login()
account.find_friends()
#account.set_list()
account.select_user_objetive()
account.user_obetive.find_posts()

print(account.user_obetive.data_posts)
csv = CSV(account.user_obetive.data_posts, account.user_obetive.name)
csv.register()

print(account.user_obetive)

account.close_webdriver()

print('Fin proceso')
