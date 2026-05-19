import time
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#**************************************************************************************************
# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

#******************************************************************************************
class UrbanRoutesPage:
    #Localizadores
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_button = (By.XPATH, './/button[@class="button round"]')
    comfort_fare = (By.XPATH, './/div[@class="tcard"]//div[@class="tcard-icon"]//img[@alt="Comfort"]')
    phone_num_field = (By.CLASS_NAME, "np-button")
    phone_input = (By.ID, "phone")
    next_button = (By.XPATH, './/div[@class="modal"]//div[@class="section active"]//form//div[@class="buttons"]')
    confirmation_button = (By.XPATH, './/div[@class="modal"]//div[@class="section active"]//form//div[@class="buttons"]//button[@type="submit"]')
    closePaymentButton = (By.XPATH, '//div[@class="payment-picker open"]//div[@class="modal"]//div[@class="section active"]//button[@class="close-button section-close"]')
    code_input_field = (By.XPATH, './/input[@id="code"][@class="input"]')
    credit_card_button = (By.CLASS_NAME, "pp-value")
    credit_card_row = (By.XPATH, './/div[@class="pp-row disabled"]//div[@class="pp-title"]')
    card_input_number = (By.XPATH, './/div[@class="card-number-input"]//input[@type="text"][@id="number"]')
    card_input_code = (By.XPATH, './/div[@class="card-code-input"]//input[@type="text"][@id="code"]')
    card_wrapper = (By.CLASS_NAME, "card-wrapper")
    message_field = (By.ID, "comment")
    reqs_arrow = (By.CLASS_NAME, "reqs" )
    blanket_button = (By.XPATH, '//div[text()="Manta y pañuelos"]/following-sibling::div//span')
    icecream_counter_plus_button = (By.XPATH, '//div[text()="Helado"]/following-sibling::div//div[@class="counter-plus"]')
    smart_button = (By.XPATH, './/button[@class="smart-button"]')
    smart_button_title = (By.XPATH, './/button[@class="smart-button"]//span[@class="smart-button-main"][text()="Pedir un taxi"]')
    order_window = (By.XPATH,'.//div[@class="order shown"]//div[@class="order-body"]')
    orderHeaderTitle = (By.XPATH, './/div[@class="order-header-title"]')
    orderNumber = (By.XPATH, './/div[@class="number"]')
    orderDriverRating = (By.XPATH, './/div[contains(@class, "order-btn-rating")]')
    orderDriverName = (By.XPATH, '//div[contains(text(), "driver.name")]')

    #***************************************************************************************************************************
    #Métodos
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address): #Metodo para escribir en campo Desde
        from_space = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.from_field))
        from_space.send_keys(from_address)

    def set_to(self, to_address): #Metodo para escribir en campo Hasta
        to_space = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.to_field))
        to_space.send_keys(to_address)

    def get_from(self): #Metodo para obtener el valor del campo Desde
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self): #Metodo para obtener el valor del campo Hasta
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.set_from(address_from)
        self.set_to(address_to)

    def click_on_taxi_request_button(self):
        button = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.request_button))
        button.click()

    def select_comfort_tare(self):
        comfort_button = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.comfort_fare))
        comfort_button.click()

    def get_selected_tare(self):
        return self.driver.find_element(By.XPATH, './/div[@class="tcard active"]//div[@class="tcard-icon"]//img[@alt="Comfort"]').is_displayed()

    def fill_phone_number_field(self):
        phoneNumField = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.phone_num_field))
        phoneNumField.click()
        phoneInput = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.phone_input))
        phoneInput.send_keys(data.phone_number)
        return phoneInput

    def click_on_confirmation_button(self):
        confirmButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.confirmation_button))
        confirmButton.click()

    def write_code_number(self, code_num):
        codeInput= WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.code_input_field))
        codeInput.send_keys(code_num)
        return codeInput

    def fill_credit_card_form(self):
        creditCardForm = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.credit_card_button))
        creditCardForm.click()
        creditCardRow = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.credit_card_row))
        creditCardRow.click()
        cardNumberField = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.card_input_number))
        cardNumberField.send_keys(data.card_number)
        cardCodeField = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.card_input_code))
        cardCodeField.send_keys(data.card_code)
        self.driver.find_element(*self.card_wrapper).click()
        return cardNumberField, cardCodeField

    def writting_message_for_driver(self):
        messageField = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.message_field))
        messageField.send_keys(data.message_for_driver)
        time.sleep(2)
        return messageField

    def order_reqs(self):
        reqsArrow = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.reqs_arrow))
        reqsArrow.click()
        blanketButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.blanket_button))
        blanketButton.click()

    def select_ice_cream(self):
        iceCreamCounterButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.icecream_counter_plus_button))
        iceCreamCounterButton.click()
        time.sleep(1)
        iceCreamCounterButton.click()




class TestUrbanRoutes:

    driver = None

    #closePickNumberButton = (By.XPATH, '//div[contains(@class, "number-picker open")]//div[contains(@class, "section active")]//button[contains(@class, "section-close")]')

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
        cls.routes_page = UrbanRoutesPage(cls.driver)
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
        assert phoneInputField.get_attribute('value') == '+1 123 123 12 12'
        #Click en siguiente
        nextButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.routes_page.next_button))
        nextButton.click()
        #Obtenemos, ingresamos el código de confirmación y validamos antes de confirmar
        time.sleep(2)
        codeNumber = retrieve_phone_code(self.routes_page.driver)
        codeNumberField = self.routes_page.write_code_number(codeNumber)
        assert codeNumberField.get_attribute('value') == codeNumber
        #Confirmamos la solicitud
        self.routes_page.click_on_confirmation_button()

       # time.sleep(2)
       # self.driver.find_element(*self.closePickNumberButton).click()

    def test4_add_credit_card(self):
        #Rellenamos los datos de la tarjeta y validamos
        cardFormList = self.routes_page.fill_credit_card_form()
        assert cardFormList[0].get_attribute('value') == '1234 5678 9100'
        assert cardFormList[1].get_attribute('value') == '111'
        #click en boton Agregar
        self.driver.find_element(By.XPATH, './/div[@class="pp-buttons"]//button[@type="submit"]').click()
        time.sleep(2)
        #Click en cerrar
        self.driver.find_element(*self.routes_page.closePaymentButton).click()

    def test5_write_driver_message(self):
        #Escribimos el mensaje para el conductor y validamos el texto que ingresamos
        message = self.routes_page.writting_message_for_driver()
        assert message.get_attribute('value') == 'Muéstrame el camino al museo'

    def test6_ask_for_blanket_scarves(self):
        #Ordenamos Manta y pañuelos
        self.routes_page.order_reqs()
        time.sleep(2)
        #validamos que esta seleccionado el switch
        blanketSwitch = self.driver.find_element(By.XPATH, '//div[text()="Manta y pañuelos"]/following-sibling::div//input')
        assert blanketSwitch.is_selected() == True

    def test7_select_2_ice_creams(self):
        #Seleccionamos 2 helados
        self.routes_page.select_ice_cream()
        #Validamos que realmente se seleccionaron 2
        qtyIceCreamValue = self.driver.find_element(By.XPATH, '//div[text()="Helado"]/following-sibling::div//div[@class="counter-value"]')
        assert qtyIceCreamValue.text == '2'

    def test8_check_modal_taxi(self):
        #Validamos que el botón despliegue el texto correcto
        modalTaxiButton = self.driver.find_element(*self.routes_page.smart_button)
        buttonTitle = self.driver.find_element(*self.routes_page.smart_button_title)
        assert buttonTitle.text == "Pedir un taxi"
        #Hacemos click
        modalTaxiButton.click()
        time.sleep(2)
        #Verificamos si aparece la orden despues de hacer click
        modalTaxiWindow  = self.driver.find_element(*self.routes_page.order_window)
        assert modalTaxiWindow.is_enabled() == True

    def test9_check_driver_info(self):
        #Esperamos a que se complete el timer de búsqueda de taxi
        time.sleep(40)
        #Buscamos la información del conductor
        modalHeader = self.driver.find_element(*self.routes_page.orderHeaderTitle)
        modalOrderNumber = self.driver.find_element(*self.routes_page.orderNumber)
        modalOrderDrvRating = self.driver.find_element(*self.routes_page.orderDriverRating)
        modalOrderDrvName = self.driver.find_element(*self.routes_page.orderDriverName)
        time.sleep(2)
        #Validamos que se despliegue la información
        assert modalHeader.is_displayed() == True
        assert modalOrderNumber.is_displayed() == True
        assert modalOrderDrvRating.is_displayed() == True
        assert modalOrderDrvName.is_displayed() == True



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



