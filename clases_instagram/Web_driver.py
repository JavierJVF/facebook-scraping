from selenium import webdriver

##########################################
# El obetivo de esta clase es tener un objeto que tenga acceso al driver que se usara
# Siendo heredados o reutilizados en otras clases
##########################################
class Web_driver:

    def __init__(self, driver = None):
        self.driver = driver

    #metodo para inicializar el driver, se esta utilizando Chromedriver para las
    #pruebas del desarrollo de esta evaluacion

    #Este codigo se prueba en un servidor remoto y en uno local
    #por esto existe variable REMOTO
    def init_webdriver(self):
        REMOTO = False #Bandera para saber la configuracion a tomar del webdriver
        if REMOTO == True:
            #rutas en el servidor remoto
            driver_location = "/usr/local/share/chromedriver"
            binary_location = "/usr/bin/google-chrome"

            options = webdriver.ChromeOptions()
            options.binary_location = binary_location
            options.add_argument("--headless")
            options.add_argument('--disable-extensions')
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")

            self.driver = webdriver.Chrome(executable_path=driver_location, options=options)

        else:
            options =  webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--disable-extensions')
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument('--disable-gpu')

            #ruta del chromdriver en local, esta se debe modificar para ejecutarse en otro entorno
            ######## MODIFICAR ########
            ############## MODIFICAR #########
            driver_path = 'C:\\Users\\javier\\Downloads\\chromedriver_win32\\chromedriver.exe'

            self.driver = webdriver.Chrome(driver_path, chrome_options=options)

    # Metodo para cerrar el Chromedriver y evitar que quede ejecutando en seguundo plano
    def close_webdriver(self):
        if self.driver != None:
            self.driver.quit()
        