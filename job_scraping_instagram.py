import time
from clases_instagram.CSV import CSV
from clases_instagram.Account_scraper import Account_scraper

#se debe ingresar las credenciales para iniciar session en facebook
#parametro 1: email o numero de telefono
#parametro 2: passwword
account = Account_scraper('', '') ########## MODIFICAR

term = '#casico'
if True:
    #se inicializa el Webdriver, en este caso mediante chromedriver
    account.init_webdriver()

    #Nos logueamos en el sitio
    account.login()

    account.search_set(term)
    account.search.buscar_terminos()

    account.search.find_posts()
    #Inicializamos el objeto quue gestiona el csv a crear

    csv = CSV(account.search.data_posts, term)
    #Creamos el csv con toda la informacion de los posts
    csv.register()

#cerramos el webdriver
account.close_webdriver()
print('Fin proceso')
