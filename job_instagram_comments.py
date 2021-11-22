import time
from clases_instagram.CSV import CSV
from clases_instagram.Account_scraper import Account_scraper
from getpass import getpass

#se debe ingresar las credenciales para iniciar session en facebook
#parametro 1: email o numero de telefono
#parametro 2: passwword
usr        = input("Instagram User:")
pwd        = getpass()
link       = input("Insert Link:")
account = Account_scraper(usr, pwd) ########## MODIFICAR

#term = '#realmadrid'
#link = 'https://www.instagram.com/p/CWQ8S1Gpzgi/'
#https://www.instagram.com/p/CWORGi8FrjL/
#https://www.instagram.com/p/CWOCTrpLUpO/
#https://www.instagram.com/p/CWQ8S1Gpzgi/

if True:
    #se inicializa el Webdriver, en este caso mediante chromedriver
    account.init_webdriver()

    #Nos logueamos en el sitio
    account.login()

    account.link_set(link)

    account.search.find_post_by_link()

    name_csv = link.split('/')[4]
    csv = CSV(account.search.data_posts, name_csv)
    #Creamos el csv con toda la informacion de los posts
    csv.register_comments()

    #account.search_set(term)
    #account.search.buscar_terminos()

    #account.search.find_posts()
    #Inicializamos el objeto quue gestiona el csv a crear

    #csv = CSV(account.search.data_posts, term)
    #Creamos el csv con toda la informacion de los posts
    #csv.register()

#cerramos el webdriver
account.close_webdriver()
print('Fin proceso')
