from clases.CSV import CSV
from clases.Account_scraper import Account_scraper
from getpass import getpass


usr        = input("Facebook User:")
pwd        = getpass()
link       = input("Insert Link:")
#account = Account_scraper('', '') ########## MODIFICAR
account = Account_scraper(usr, pwd) ########## MODIFICAR


try:
    #se inicializa el Webdriver, en este caso mediante chromedriver
    account.init_webdriver()

    #Nos logueamos en el sitio
    account.login()

    account.link_set(link)

    account.search.find_post_by_link()

    #Inicializamos el objeto quue gestiona el csv a crear
    name_csv = link.split('/')[3]
    print(name_csv)
    print('////////////////////////////////////////////////////////')
    print(account.search.data_posts)
    csv = CSV(account.search.data_posts, name_csv)
    #Creamos el csv con toda la informacion de los posts
    csv.register_comments()

except Exception as e:
    print(e)
#https://www.facebook.com/yurvielys.figuera/posts/3671476133077744
#cerramos el webdriver
account.close_webdriver()
print('Fin proceso')
