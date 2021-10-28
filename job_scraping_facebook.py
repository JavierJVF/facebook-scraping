from clases.CSV import CSV
from clases.Account_scraper import Account_scraper

#se debe ingresar las credenciales para iniciar session en facebook
#parametro 1: email o numero de telefono
#parametro 2: passwword
account = Account_scraper('', '') ########## MODIFICAR


try:
    #se inicializa el Webdriver, en este caso mediante chromedriver
    account.init_webdriver()

    #Nos logueamos en el sitio
    account.login()

    #Ubicamos la lista de amigos y obtenemos sus enlaces
    #account.find_friends()
    account.set_list()

    #seleccionammos de forma aleatoria uno de las cuentas listadas
    account.select_user_objetive()

    #buscamos la informacion de sus posts
    account.user_obetive.find_posts()

    #Inicializamos el objeto quue gestiona el csv a crear
    csv = CSV(account.user_obetive.data_posts, account.user_obetive.name)
    #Creamos el csv con toda la informacion de los posts
    csv.register()

    #vemos de quien es la cuenta obetivo por consola
    print(account.user_obetive)

except Exception as e:
    print(e)

#cerramos el webdriver
account.close_webdriver()
print('Fin proceso')
