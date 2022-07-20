import unittest
from selenium import webdriver
from pageobjects.pesas_mancuernas import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class PesasMancuernas(unittest.TestCase):

    def setUp(self):
        """
        Prepare and start the browser for test below
        :return: None
        """
        options = Options()
        options.add_argument("start-maximized")
        # self.driver.maximize_window()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.headless = True
        # options.add_argument("--headless")
        options.add_argument("--allow-running-insecure-content")
        print ("Ejemplo Kit de mosculación: https://www.decathlon.es/es/p/kit-de-pesas-y-barras-de-musculacion-de-50-kg/_/R-p-335265?mc=8655649&_adin=11551547647")
        url = input("Escribe la URL del decathlon, la cual quieres saber stock/precio: ")
        print (f"\nYendo a la URL: {url}")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(str(url))

    def test_stock(self):
        """
        Test to check if there are stock in decathlon page for one item given in the URL
        :return: None
        """
        DecathPesasMancuernas(self.driver).accept_cookies()
        price = DecathPesasMancuernas(self.driver).get_price()
        assert price is not None, "No aparece el precio. El elemento que buscas sigue sin estar disponible"
        print(f"El precio del producto es actualmente: {price}")

    def test_add_cart(self):
        """
        Test to check if the elemet add_to_cart is present in the given URL. Therefore we can buy it
        :return: None
        """
        DecathPesasMancuernas(self.driver).accept_cookies()
        verify = DecathPesasMancuernas(self.driver).element_add_to_cart_is_enabled()
        if verify:
            print("Parece que ya hay stock del elemento que buscas, revisalo ¡corre!")
        else:
            assert False, "No es posible añadir el producto a la cesta. El elemento que buscas sigue sin estar disponible"

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
