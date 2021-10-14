from clases.CSV import CSV
from clases.Account_scraper import Account_scraper
from getpass import getpass


usr        = input("Twitter User:")
pwd        = getpass()
term       = input("Search Term:")
#account = Account_scraper('', '') ########## MODIFICAR
account = Account_scraper(usr, pwd) ########## MODIFICAR


try:
    #se inicializa el Webdriver, en este caso mediante chromedriver
    account.init_webdriver()

    #Nos logueamos en el sitio
    account.login()

    account.search_set(term)

    account.search.buscar_terminos()

    #buscamos la informacion de sus posts
    account.search.find_posts()

    #Inicializamos el objeto quue gestiona el csv a crear
    csv = CSV(account.search.data_posts, term)
    #Creamos el csv con toda la informacion de los posts
    csv.register()

except Exception as e:
    print(e)

#cerramos el webdriver
account.close_webdriver()
print('Fin proceso')
