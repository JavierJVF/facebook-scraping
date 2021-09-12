from selenium import webdriver

class Web_driver:

    def __init__(self, driver = None):
        self.driver = driver

    def init_webdriver(self):
        REMOTO = False
        if REMOTO == True:
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


            driver_path = 'C:\\Users\\javier\\Downloads\\chromedriver_win32\\chromedriver.exe'

            self.driver = webdriver.Chrome(driver_path, chrome_options=options)

    def close_webdriver(self):
        if self.driver != None:
            self.driver.quit()

    def set_webdriver(self):
        self.driver = 'Valor de prueba'
        