import time
import data
import pages
import utilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#**************************************************************************************************

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        #Configurando el driver del navegador
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        #Centralizamos y abrimos la página para todas las pruebas
        cls.routes_page = pages.UrbanRoutesPage(cls.driver)
        #Seteamos la ruta del viaje
        cls.routes_page.set_route()



    def test1_set_route(self):
        #Solamente validamos que las direcciones sean correctas
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test2_select_comfort_taxi_fare(self):
        self.routes_page.click_on_taxi_request_button()
        self.routes_page.select_comfort_tare()
        tare_selected = self.routes_page.get_selected_tare()
        #Validamos que selecciono la tarifa correcta
        assert tare_selected == True

    def test3_fill_the_phone_number_field(self):
        #Rellenamos el campo del numero telefónico y validamos
        phoneInputField = self.routes_page.fill_phone_number_field()
        assert phoneInputField.get_attribute('value') == data.phone_number
        self.routes_page.click_on_next_button()
        #Obtenemos, ingresamos el código de confirmación y validamos antes de confirmar
        codeNumber = utilities.retrieve_phone_code(self.routes_page.driver)
        codeNumberField = self.routes_page.write_code_number(codeNumber)
        assert codeNumberField.get_attribute('value') == codeNumber
        #Confirmamos la solicitud
        self.routes_page.click_on_confirmation_button()

    def test4_add_credit_card(self):
        #Rellenamos los datos de la tarjeta y validamos
        cardFormList = self.routes_page.fill_credit_card_form()
        assert cardFormList[0].get_attribute('value') == data.card_number
        assert cardFormList[1].get_attribute('value') == data.card_code
        #Click en agregar
        self.routes_page.click_on_add_button()
        #Click en cerrar
        self.routes_page.click_on_close_payment_button()

    def test5_write_driver_message(self):
        #Escribimos el mensaje para el conductor y validamos el texto que ingresamos
        message = self.routes_page.writting_message_for_driver()
        assert message.get_attribute('value') == data.message_for_driver

    def test6_ask_for_blanket_scarves(self):
        #Ordenamos Manta y pañuelos
        self.routes_page.order_reqs()
        #validamos que esta seleccionado el switch
        blanketSwitch = self.routes_page.search_blankets_switch()
        assert blanketSwitch == True

    def test7_select_2_ice_creams(self):
        #Seleccionamos 2 helados
        self.routes_page.select_ice_cream()
        #Validamos que realmente se seleccionaron 2
        qtyIceCreamValue = self.routes_page.search_ice_cream_counter()
        assert qtyIceCreamValue.text == data.ice_cream_counter_value

    def test8_check_modal_taxi(self):
        #Validamos que el botón despliegue el texto correcto
        orderList = self.routes_page.check_order_button()
        modalButton = orderList[0]
        buttonText = orderList[1]
        assert buttonText.text == data.smart_button_text
        #Hacemos click
        modalButton.click()
        #Verificamos si aparece la orden despues de hacer click
        modalTaxiWindow  = self.routes_page.search_order_popup()
        assert modalTaxiWindow.is_enabled() == True

    def test9_check_driver_info(self):
        #Buscamos la información del conductor
        driverInfoList = self.routes_page.search_driver_information()
        #Validamos que se despliegue la información
        #Texto del header
        assert driverInfoList[0].is_displayed() == True
        #Numero de placa
        assert driverInfoList[1].is_displayed() == True
        #Calificacion del conductor
        assert driverInfoList[2].is_displayed() == True
        #Nombre del conductor
        assert driverInfoList[3].is_displayed() == True



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



