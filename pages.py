import time
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
    add_button = (By.XPATH, './/div[@class="pp-buttons"]//button[@type="submit"]')
    blanket_switch = (By.XPATH, '//div[text()="Manta y pañuelos"]/following-sibling::div//input')
    counter_ice_cream = (By.XPATH, '//div[text()="Helado"]/following-sibling::div//div[@class="counter-value"]')

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

    def click_on_next_button(self):
        # Click en siguiente
        nextButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.next_button))
        nextButton.click()

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

    def click_on_add_button(self):
        # click en boton Agregar
        addButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.add_button))
        addButton.click()

    def click_on_close_payment_button(self):
        closePayButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.closePaymentButton))
        closePayButton.click()

    def writting_message_for_driver(self):
        messageField = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.message_field))
        messageField.send_keys(data.message_for_driver)
        return messageField

    def order_reqs(self):
        reqsArrow = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.reqs_arrow))
        reqsArrow.click()
        blanketButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.blanket_button))
        blanketButton.click()

    def search_blankets_switch(self):
        switchBlanket = WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(self.blanket_switch))
        return switchBlanket.is_selected()

    def select_ice_cream(self):
        iceCreamCounterButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.icecream_counter_plus_button))
        iceCreamCounterButton.click()
        time.sleep(1)
        iceCreamCounterButton.click()

    def search_ice_cream_counter(self):
        iceCreamCounterValue = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.counter_ice_cream))
        return iceCreamCounterValue

    def check_order_button(self):
        modalTaxiButton = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.smart_button))
        buttonTitle = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.smart_button_title))
        return modalTaxiButton, buttonTitle

    def search_order_popup(self):
        orderPopupWindow = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_window))
        return orderPopupWindow

    def search_driver_information(self):
        #Anclamos la espera en el numero de placa, ya que aparece despues de que se completa el timer.
        modalOrderNumber = WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(self.orderNumber))
        modalHeader = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.orderHeaderTitle))
        modalOrderDrvRating = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.orderDriverRating))
        modalOrderDrvName = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.orderDriverName))
        return modalHeader, modalOrderNumber, modalOrderDrvRating, modalOrderDrvName