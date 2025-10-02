from bdd.Helpers.price_hotel_afiliado import obtained_price_passenger, obtained_price_passenger_extra, \
    obtained_price_passenger_bus, obtained_hotel_fare_room_type_rates, vat_percentage_for_affiliate_discount
from bdd.Helpers.afiliate_bd import get_discount_fixed_amount_category, get_discount_percentage_amount_category
from bdd.pages.catmandu.PassengerPage import PassengerPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from loguru import logger
import datetime
import math
import re


class AfiliatePassengerPage(PassengerPage):
    MESSAGE_CAUTION = (By.XPATH, "//div[@id='Notify']//span")
    PRICE_TAXES = "//div[@id='divSummary']//div[@class='small-6 column text-right']"
    IMAGEN_HOTEL = "//div[@class='side-hotel-image-div']/img"
    EXTRA_TRAVELER_TITLE = "ExtraReservationItems_0__Travelers_{index}__Title"
    EXTRA_TRAVELER_DOCUMENT = "ExtraReservationItems_0__Travelers_{index}__DucumentNumber"
    EXTRA_TRAVELER_NAME = "ExtraReservationItems_0__Travelers_{index}__FirstName"
    EXTRA_TRAVELER_DOCUMENT_TYPE = "ExtraReservationItems_0__Travelers_{index}__DocumentType"
    PRICE_FORM_PASSENGER_AFILIATE = "//span[@class='nts-totalizer nts-big-total']//span[@class='currencyText']"
    AFFILIATE_DISCOUNT_VALUE = "//div[@class='small-6 column text-right']/span[@class='nts-negative']/span[@class='currencyText']"

    def __init__(self, context):
        PassengerPage.__init__(self, context)

    def MakeOccupancy(self, rooms, adults_room_one, children_room_one, adults_room_two, children_room_two,adults_room_three, children_room_three):
        if rooms == 1:
            if adults_room_one == 1 and children_room_one == 0:
                if self.context.actual_occupancy == '1r1a_cc':
                    self.context.ocupation = '1r1a_cc'
                elif self.context.actual_occupancy == '1r1a_ca':
                    self.context.ocupation = '1r1a_ca'
                elif self.context.actual_occupancy == '1r1a_cb':
                    self.context.ocupation = '1r1a_cb'
                return self.context.ocupation
            elif adults_room_one == 2 and children_room_one == 0:
                if self.context.actual_occupancy == '1r2a_cac':
                    self.context.ocupation = '1r2a_cac'
                elif self.context.actual_occupancy == '1r2a_ca':
                    self.context.ocupation = '1r2a_ca'
                return self.context.ocupation
            elif adults_room_one == 3 and children_room_one == 0:
                if self.context.actual_occupancy == '1r3acabc':
                    self.context.ocupation = '1r3acabc'
                return self.context.ocupation
            elif adults_room_one == 2 and children_room_one == 2:
                if self.context.actual_occupancy == '1r2a_1c1n':
                    self.context.ocupation = '1r2a_1c1n'
                elif self.context.actual_occupancy == '1r2a_1n1c':
                    self.context.ocupation = '1r2a_1n1c'
                return self.context.ocupation
        if rooms == 2:
            if adults_room_one == 1 and children_room_one == 0 and adults_room_two == 1 and children_room_two == 0:
                if self.context.actual_occupancy == '1r1aca_2r1acb':
                    self.context.ocupation = '1r1aca_2r1acb'
            elif adults_room_one == 2 and children_room_one == 0 and adults_room_two == 1 and children_room_two == 0:
                if self.context.actual_occupancy == '1r2ad_2r1aca':
                    self.context.ocupation = '1r2ad_2r1aca'
            elif adults_room_one == 1 and children_room_one == 0 and adults_room_two == 1 and children_room_two == 2:
                if self.context.actual_occupancy == '1r1a_2r1a1c1n':
                    self.context.ocupation = '1r1a_2r1a1c1n'
            return self.context.ocupation

    def FillPassengerInformation(self, composedNames=False):
        """Registra los pasajeros en el formulario dependiendo del occupancy.
        :return:
        """
        occupancy = self.GetOccupancyFromModel()
        data = self.mockaroo.GetNetNFFPassengersData()

        if occupancy == '1r1a_cc':
            self.FillPassenger1r1a_cc(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r1a_ca':
            self.FillPassenger1r1a_ca(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r2a_cac':
            self.FillPassenger1r2a_cac(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r1a_cb':
            self.FillPassenger1r1a_cb(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r1aca_2r1acb':
            self.FillPassenger1r1aca_2r1acb(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r3acabc':
            self.FillPassenger1r3acabc(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r2a_1n1c':
            self.FillPassenger1r2a_1n1c(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1re':
            self.FillPassenger1re(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1e_cb':
            self.FillPassenger1e_cb(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1e_cc':
            self.FillPassenger1e_cc(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '3acabc':
            self.FillPassenger3acabc(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r2ad_2r1aca':
            self.FillPassenger1r2ad_2r1aca(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r2a_ca':
            self.FillPassenger1r2a_ca(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '2adt_cca':
            self.FillPassenger2adt_cca(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '3adt_cabc':
            self.FillPassenger3adt_cabc(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '1r2a_1c1n' or\
                occupancy == '1r1a_2r1a1c1n' or\
                occupancy == '2adt_1c1n':
            self.FillPassenger1r2a_1c1n(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()
        elif occupancy == '2ad_1c1n':
            self.FillPassenger2ad_1c1n(composedNames)
            self.identity_message()
            self.FillEmail(data['Email'])
            self.FillPhone(data['Phone'])
            self.ClickCheckBox()

    def FillPassenger1r1a_cc(self, composedNames=False):
        self.FillFormPerPassenger('passenger_cc', 0, composedNames)

    def FillPassenger1r1a_ca(self, composedNames=False):
        self.FillFormPerPassenger('passenger_ca', 0, composedNames)

    def FillPassenger1r2a_cac(self, composedNames=False):
        self.FillFormPerPassenger('passenger_ca', 0, composedNames)
        self.FillFormPerPassenger('passenger_cc', 1, composedNames)

    def FillPassenger1r1a_cb(self, composedNames=False):
        self.FillFormPerPassenger('passenger_cb', 0, composedNames)

    def FillPassenger1r1aca_2r1acb(self, composedNames=False):
        self.FillFormPerPassenger('passenger_ca', 0, composedNames)
        self.FillFormPerPassenger('passenger_cb', 1, composedNames)

    def FillPassenger1r3acabc(self, composedNames=False):
        self.FillFormPerPassenger('passenger_ca', 0, composedNames)
        self.FillFormPerPassenger('passenger_cb', 1, composedNames)
        self.FillFormPerPassenger('passenger_cc', 2, composedNames)

    def FillPassenger1re(self, composedNames=False):
        self.FillFormPerPassenger('traveler', 0, composedNames)

    def FillPassenger1e_cb(self, composedNames=False):
        self.FillFormPerPassenger('traveler_cb', 0, composedNames)

    def FillPassenger1e_cc(self, composedNames=False):
        self.FillFormPerPassenger('traveler_cc', 0, composedNames)

    def FillPassenger3acabc(self, composedNames=False):
        self.FillFormPerPassenger('traveler', 0, composedNames)
        self.FillFormPerPassenger('traveler_cb', 1, composedNames)
        self.FillFormPerPassenger('traveler_cc', 2, composedNames)

    def FillPassenger1r2ad_2r1aca(self, composedNames=False):
        self.FillFormPerPassenger('passenger', 0, composedNames)
        self.FillFormPerPassenger('passenger', 1, composedNames)
        self.FillFormPerPassenger('passenger_ca', 2, composedNames)

    def FillPassenger1r2a_ca(self, composedNames=False):
        self.FillFormPerPassenger('passenger_cb', 0, composedNames)
        self.FillFormPerPassenger('passenger', 1, composedNames)

    def FillPassenger2adt_cca(self, composedNames=False):
        self.FillFormPerPassenger('passenger_cc', 0, composedNames)
        self.FillFormPerPassenger('passenger_ca', 1, composedNames)

    def FillPassenger3adt_cabc(self, composedNames=False):
        self.FillFormPerPassenger('passenger_ca', 0, composedNames)
        self.FillFormPerPassenger('passenger_cb', 1, composedNames)
        self.FillFormPerPassenger('passenger_cc', 2, composedNames)

    def FillPassenger1r2a_1c1n(self, composedNames=False):
        self.FillFormPerPassenger('passenger_cb', 0, composedNames)
        self.FillFormPerPassenger('passenger_cc', 1, composedNames)
        self.FillFormPerPassenger('children_ca', 2, composedNames)
        self.FillFormPerPassenger('infant_ca', 3, composedNames)

    def FillPassenger1r2a_1n1c(self, composedNames=False):
        self.FillFormPerPassenger('passenger_cb', 0, composedNames)
        self.FillFormPerPassenger('passenger_cc', 1, composedNames)
        self.FillFormPerPassenger('infant_cd', 2, composedNames)
        self.FillFormPerPassenger('infant_ca', 3, composedNames)

    def FillPassenger2ad_1c1n(self, composedNames=False):
        self.FillFormPerPassenger('traveler_cb', 0, composedNames)
        self.FillFormPerPassenger('traveler_cc', 1, composedNames)
        self.FillFormPerPassenger('traveler_children', 2, composedNames)
        self.FillFormPerPassenger('traveler_infant', 3, composedNames)

    def FillFormPerPassenger(self, type_passenger, passenger_number, composedNames=False):

        data = self.mockaroo.GetNetNFFPassengersData()
        date_time_format = '%Y-%m-%d %H:%M:%S'

        if type_passenger == 'passenger_cc':
            self.fill_title(data['Title'], passenger_number)
            self.fill_document_number(passenger_number, 'adult_c')
            self.fill_name_new(passenger_number)
        if type_passenger == 'passenger_ca':
            self.fill_title(data['Title'], passenger_number)
            self.fill_document_number(passenger_number, 'adult_a')
            self.fill_name_new(passenger_number)
        if type_passenger == 'passenger_cb':
            self.fill_title(data['Title'], passenger_number)
            self.fill_document_number(passenger_number, 'adult_b')
            self.fill_name_new(passenger_number)
        if type_passenger == 'passenger_cd':
            self.fill_title(data['Title'], passenger_number)
            self.fill_document_number(passenger_number, 'adult_d')
            self.fill_name_new(passenger_number)
        if type_passenger == 'children_ca':
            self.fill_title(data['Title'], passenger_number)
            self.fill_document_type(passenger_number)
            self.fill_document_number(passenger_number, 'children_a')
            self.fill_name_new(passenger_number)
        if type_passenger == 'infant_ca':
            self.fill_title(data['Title'], passenger_number)
            self.fill_document_type_infant(passenger_number)
            self.fill_document_number(passenger_number, 'infant_a')
            self.fill_name_new(passenger_number)
        if type_passenger == 'infant_cd':
            self.fill_title(data['Title'], passenger_number)
            self.fill_document_type_infant(passenger_number)
            self.fill_document_number(passenger_number, 'infant_d')
            self.fill_name_new(passenger_number)

        # Todo: extras
        if type_passenger == 'traveler':
            self.fill_extra_afilliate(data['Title'], passenger_number)
            self.fill_document_number(passenger_number, 'adult_a')
            self.fill_name_extra(passenger_number)
        if type_passenger == 'traveler_cb':
            self.fill_extra_afilliate(data['Title'], passenger_number)
            self.fill_document_number(passenger_number, 'adult_b')
            self.fill_name_extra(passenger_number)
        if type_passenger == 'traveler_cc':
            self.fill_extra_afilliate(data['Title'], passenger_number)
            self.fill_document_number(passenger_number, 'adult_c')
            self.fill_name_extra(passenger_number)
        if type_passenger == 'traveler_children':
            self.fill_extra_afilliate(data['Title'], passenger_number)
            self.fill_extra_traveler_document_type_afilliate(passenger_number)
            self.fill_document_number(passenger_number, 'child_extra')
            self.fill_name_extra(passenger_number)
        if type_passenger == 'traveler_infant':
            self.fill_extra_afilliate(data['Title'], passenger_number)
            self.fill_extra_document_type_afilliate_infant(passenger_number)
            self.fill_document_number(passenger_number, 'infant_a')
            self.fill_name_extra(passenger_number)
        if type_passenger == 'passenger':
            self.fill_title(data['Title'], passenger_number)
            self.FillName(data['ComposedFirstNameMale'] if composedNames else data['FirstName'], passenger_number)
            self.FillLastName(data['LastName'], passenger_number)
            self.FillDocumentType(data['BillingDocumentTypeNamePlaceToPay'], passenger_number)
            self.FillIDocumentNumber(self.mockaroo.GetDocumentPassenger(), passenger_number)
            date_object = datetime.datetime.strptime(data['AdultAge'], date_time_format)
            self.FillBirthDay(date_object.day, passenger_number)
            self.FillBirthDayMonth(date_object.month, passenger_number)
            self.FillBirthDayYear(date_object.year, passenger_number)

# Todo: llenar campos de afiliados

    def fill_document_number(self, index, passenger_type):
        try:
            if self.context.product.lower() == 'product.extra':
                id_input_document = (By.ID, self.EXTRA_TRAVELER_DOCUMENT.replace("{index}", str(index)))
            else:
                id_input_document = (By.ID, self.PASSENGER_DOCUMENT.replace("{index}", str(index)))
            document_mapping = self.type_document_mapping()
            document_number = document_mapping.get(passenger_type)
            WebDriverWait(self.context.browser, 40).until(
                EC.element_to_be_clickable(id_input_document)).send_keys(document_number)
            WebDriverWait(self.context.browser, 40).until(
                EC.element_to_be_clickable(id_input_document)).send_keys(Keys.TAB)

            WebDriverWait(self.context.browser, 40).until(
                EC.element_to_be_clickable(self.PASSENGER_SUBMIT))

        except Exception as e:
            raise Exception(f"¡Error when filling out affiliate documents! details: {str(e)}")

    def type_document_mapping(self):
        try:
            if self.context.catmandu_userservice == 'compensar':
                document_mapping = {
                    'adult_a': '1024522247',
                    'adult_b': '1024524451',
                    'adult_c': '1032389700',
                    'adult_d': '1069726456',
                    'infant_a': '1018202021',
                    'infant_d': '1023087256'
                }
            else:
                document_mapping = {
                    'adult_a': '39163304',
                    'adult_b': '1216719188',
                    'adult_c': '1017156553',
                    'children_a': '1195213974',
                    'infant_a': '1035988965',
                    'child_extra': '1025667727'
                }
            return document_mapping

        except Exception as e:
            raise Exception(f"¡Error obtaining mapped documents!: {e}")

    # def fill_document_number_cc(self, index):
    #     by = (By.ID, self.PASSENGER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys('1017156553')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))
    #
    # def fill_document_number_ca(self, index):
    #     by = (By.ID, self.PASSENGER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys('39163304')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))
    #
    # def fill_document_number_cb(self, index):
    #     by = (By.ID, self.PASSENGER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys('1216719188')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))

# Todo: Extras afiliados
    def fill_extra_afilliate(self, title, index):
        by = (By.ID, self.EXTRA_TRAVELER_TITLE.replace("{index}", str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[@id='ExtraReservationItems_0__Travelers_{index}__Title']/option[text()='{title}']"))).click()

    # def fill_extra_document_number_afilliate(self, index):
    #     by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 60).until(
    #         EC.visibility_of_element_located(by)).send_keys('39163304')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 30).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))
    #
    # def fill_extra_document_number_afilliate_cb(self, index):
    #     by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 60).until(
    #         EC.visibility_of_element_located(by)).send_keys('1216719188')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 30).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))
    #
    # def fill_extra_document_number_afilliate_cc(self, index):
    #     by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 60).until(
    #         EC.visibility_of_element_located(by)).send_keys('98668245')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 30).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))

    # Todo: metodo validacion campo nombre no vacio

    def fill_name_new(self, index):
        text_field = True

        while text_field:
            by = (By.ID, self.PASSENGER_NAME.replace("{index}", str(index)))
            WebDriverWait(self.context.browser, 60).until(
                EC.presence_of_element_located(by))
            value_text = self.context.browser.execute_script(
                f"return document.getElementById('Travelers_{index}__FirstName').value")
            if value_text and value_text != '':
                text_field = False

    def fill_name_extra(self, index):
        text_field_extra = True

        while text_field_extra:
            by = (By.ID, self.EXTRA_TRAVELER_NAME.replace("{index}", str(index)))
            WebDriverWait(self.context.browser, 60).until(
                EC.presence_of_element_located(by))
            value_text_extra = self.context.browser.execute_script(
                f"return document.getElementById('ExtraReservationItems_0__Travelers_{index}__FirstName').value")
            if value_text_extra and value_text_extra != '':
                text_field_extra = False

    # Todo: metodo cambio de tipo de document
    def fill_document_type(self, index):
        by = (By.ID, self.PASSENGER_DOCUMENT_TYPE.replace("{index}", str(index)))
        WebDriverWait(self.context.browser, 40).until(EC.presence_of_element_located(by))
        id_text = by[1]
        Select(self.context.browser.find_element(By.ID, id_text)).select_by_visible_text("Tarjeta de identidad")

    def fill_document_type_infant(self, index):
        by = (By.ID, self.PASSENGER_DOCUMENT_TYPE.replace("{index}", str(index)))
        WebDriverWait(self.context.browser, 40).until(EC.presence_of_element_located(by))
        id_text = by[1]
        Select(self.context.browser.find_element(By.ID, id_text)).select_by_visible_text("Registro civil")

    # Todo: ingreso documento children
    # def fill_document_number_children(self, index):
    #     by = (By.ID, self.PASSENGER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys('1195213974')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))

    # Todo: ingreso documento infant
    # def fill_document_number_infant(self, index):
    #     by = (By.ID, self.PASSENGER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys('1035988965')
    #         # EC.element_to_be_clickable(by)).send_keys('1025774312')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))

    # Todo: Document type extras
    def fill_extra_traveler_document_type_afilliate(self, index):
        by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT_TYPE.replace("{index}", str(index)))
        WebDriverWait(self.context.browser, 30).until(EC.visibility_of_element_located(by))
        id_text = by[1]
        Select(self.context.browser.find_element(By.ID, id_text)).select_by_visible_text("Tarjeta de identidad")

    # Todo: Numeros Documentos extras children
    # def fill_extra_document_number_afilliate_children(self, index):
    #     by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 60).until(
    #         EC.visibility_of_element_located(by)).send_keys('1025667727')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 30).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))

    # Todo: Document type extras
    def fill_extra_document_type_afilliate_infant(self, index):
        by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT_TYPE.replace("{index}", str(index)))
        WebDriverWait(self.context.browser, 30).until(EC.visibility_of_element_located(by))
        id_text = by[1]
        Select(self.context.browser.find_element(By.ID, id_text)).select_by_visible_text("Registro civil")

    # Todo: Numeros Documentos extras infant
    # def fill_extra_document_number_afilliate_infant(self, index):
    #     by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT.replace("{index}", str(index)))
    #     WebDriverWait(self.context.browser, 60).until(
    #         EC.visibility_of_element_located(by)).send_keys('1035988965')
    #     WebDriverWait(self.context.browser, 40).until(
    #         EC.element_to_be_clickable(by)).send_keys(Keys.TAB)
    #
    #     WebDriverWait(self.context.browser, 30).until(
    #         EC.element_to_be_clickable(self.PASSENGER_SUBMIT))
# Todo: Tomar precio pagina de pasajeros

    def get_price_form_passenger_afiliate(self):
        view_price_in_passenger = self.context.browser.find_elements(
            By.XPATH, self.PRICE_FORM_PASSENGER_AFILIATE)

        convert_price = view_price_in_passenger[0].text  # TODO: get_price_text_in_passenger_page
        convert_price = convert_price.replace('.', '').replace('$ ', '')
        convert_price = (float(convert_price))
        self.context.price_obtained_in_passenger_page = convert_price
        return self.context.price_obtained_in_passenger_page

    def get_affiliate_discount(self):
        discount_value = WebDriverWait(self.context.browser, 60)\
            .until(EC.visibility_of_element_located((By.XPATH, self.AFFILIATE_DISCOUNT_VALUE))).text
        discount_value = discount_value.replace('.', '').replace('$ ', '')
        discount_value = (float(discount_value))
        self.context.affiliate_discount_value = discount_value
        return self.context.affiliate_discount_value

    def get_price_taxes_afilliate(self):
        WebDriverWait(self.context.browser, 60).until(
            EC.presence_of_element_located((By.XPATH, self.PRICE_TAXES)))
        taxes = self.context.browser.find_elements(By.XPATH, self.PRICE_TAXES)
        price_taxes = taxes[1].text
        price_taxes = price_taxes.replace('.', '').replace('COP', '').replace('$', '').replace(' ', '')
        price_taxes = float(price_taxes)
        self.context.value_total_taxes = price_taxes
        return self.context.value_total_taxes

    def identity_message(self):
        try:
            message = self.visibility_identity_message()
            if message:
                product_discount_method = {
                    'product.hotel': self.identity_message_hotel,
                    'product.extra': self.identity_message_extras,
                    'product.bus': self.identity_message_bus
                }
                product_discount_method[self.context.product.lower()]()
            return self.context.discount_total

        except Exception as e:
            raise Exception(f"¡Error occurred verifying the discount!: {e}")

    def visibility_identity_message(self):
        try:
            WebDriverWait(self.context.browser, 60).until(
                EC.visibility_of_element_located(self.MESSAGE_CAUTION))
            elements = self.context.browser.find_elements(*self.MESSAGE_CAUTION)
            message = elements[0].text
            message = message is not None
            return message

        except Exception as e:
            raise Exception(f"¡Error the discount message is not visible!: {e}")

    # calculate discount hotel
    def identity_message_hotel(self):
        try:
            occupancy_discount_method_hotel = {
                '1r1a_cc': self.hotel_discount_occupation_1r1a_cc,
                '1r1a_ca': self.hotel_discount_occupation_1r1a_ca,
                '1r1a_cb': self.hotel_discount_occupation_1r1a_cb,
                '1r2a_ca': self.hotel_discount_occupation_1r2a_ca,
                '1r2a_cac': self.hotel_discount_occupation_1r2a_cac,
                '1r3acabc': self.hotel_discount_occupation_1r3acabc,
                '1r2a_1n1c': self.hotel_discount_occupation_1r2a_1n1c,
                '1r2a_1c1n': self.hotel_discount_occupation_1r2a_1c1n,
                '1r1aca_2r1acb': self.hotel_discount_occupation_1r1aca_2r1acb,
                '1r2ad_2r1aca': self.hotel_discount_occupation_1r2ad_2r1aca,
                '1r1a_2r1a1c1n': self.hotel_discount_occupation_1r1a_2r1a1c1n,
            }
            occupancy_discount_method_hotel[self.context.ocupation]()

        except Exception as e:
            raise Exception(f"Error processing discount hotel: {self.context.ocupation}: ", e)

    def hotel_discount_occupation_1r1a_cc(self):
        try:
            if self.context.catmandu_sucursal == 'af_h_mf_cc':
                price_tax_free = self.context.price_obtained_in_passenger_page
                data_value_discount = self.mapping_discount_fixed_amount()['hotel_category_c_mf']
                discount_fixed_amount = get_discount_fixed_amount_category(data_value_discount)
                print(discount_fixed_amount)
                price_tax_free = price_tax_free - discount_fixed_amount
                self.context.discount_total = price_tax_free
            else:
                price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
                discount_total = (price_tax_free * 20) / 100
                discount = price_tax_free - discount_total
                self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r1a_ca(self):
        try:
            if self.context.catmandu_sucursal == 'afh_dmf':
                price_tax_free = self.context.price_obtained_in_passenger_page
                data_value_discount = self.mapping_discount_fixed_amount()['hotel_category_a_mf']
                discount_fixed_amount = get_discount_fixed_amount_category(data_value_discount)
                price_tax_free = price_tax_free - discount_fixed_amount
                self.context.discount_total = price_tax_free
            else:
                price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
                discount_total = (price_tax_free * 40) / 100
                discount = price_tax_free - discount_total
                self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r1a_cb(self):
        try:
            if self.context.catmandu_sucursal == 'afilia_cb':
                price_tax_free = self.context.price_obtained_in_passenger_page
                data_value_discount = self.mapping_discount_fixed_amount()['hotel_category_b_mf']
                discount_fixed_amount = get_discount_fixed_amount_category(data_value_discount)
                print(discount_fixed_amount)
                price_tax_free = price_tax_free - discount_fixed_amount
                self.context.discount_total = price_tax_free
            else:
                price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
                discount_total = (price_tax_free * 30) / 100
                discount = price_tax_free - discount_total
                self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r2a_ca(self):
        try:
            price = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            divide_passenger = price / 2
            discount_total_ca = (divide_passenger * 30) / 100
            discount = price - discount_total_ca
            self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r2a_cac(self):
        try:
            price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            if self.context.catmandu_userservice == 'compensar':
                result_dict = obtained_hotel_fare_room_type_rates(33290, 42206)
                categories = ['PLTU24_Cat_A_Lagomar_ADULTO', 'PLTU24_Cat_C_Lagomar_ADULTO']
                self.calculate_compensar_discount(price_tax_free, result_dict, categories)
            else:
                divide = price_tax_free / 2
                discount_ca = (divide * 40) / 100
                discount_cc = (divide * 20) / 100
                discount_passenger_total = discount_cc + discount_ca
                discount = price_tax_free - discount_passenger_total
                self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r3acabc(self):
        try:
            price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            if self.context.catmandu_userservice == 'compensar':
                result_dict = obtained_hotel_fare_room_type_rates(33274, 42195)
                categories = ['PLTU24_Cat_A_Lagomar_ADULTO', 'PLTU24_Cat_B_Lagomar_ADULTO',
                              'PLTU24_Cat_C_Lagomar_ADULTO']
                self.calculate_compensar_discount(price_tax_free, result_dict, categories)
            else:
                divide_result = price_tax_free / 3
                discount_a = int((divide_result * 40) / 100)
                discount_b = int((divide_result * 30) / 100)
                discount_c = int((divide_result * 20) / 100)
                discount_passenger_total = discount_a + discount_b + discount_c
                discount = price_tax_free - discount_passenger_total
                self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r2a_1n1c(self):
        try:
            price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            if self.context.catmandu_userservice == 'compensar':
                result_adult = obtained_hotel_fare_room_type_rates(33273, 41384)
                result_child = obtained_hotel_fare_room_type_rates(33273, 41385)
                list_fare_room_person = [result_adult, result_adult, result_child]
                categories = ['PLTU24_Cat_B_Lagomar_ADULTO', 'PLTU24_Cat_C_Lagomar_ADULTO', 'PLTU24_Cat_A_Lagomar_NINO']
                self.calculate_compensar_discount(price_tax_free, list_fare_room_person, categories)

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r2a_1c1n(self):
        try:
            price_one_rooms = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            passenger = int(obtained_price_passenger(33160, 36444)) + (int(obtained_price_passenger_extra(24880)) * 4)
            p_one = passenger * 30 / 100
            p_two = passenger * 20 / 100
            p_c = int(obtained_price_passenger(33159, 36441)) + (int(obtained_price_passenger_extra(24881)) * 4)
            p_i = int(obtained_price_passenger(33159, 36442)) + (int(obtained_price_passenger_extra(24881)) * 4)
            p_c = p_c * 40 / 100
            p_i = p_i * 40 / 100
            discount_hotel_pre = p_one + p_two + p_c + p_i
            discount = price_one_rooms - discount_hotel_pre
            self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r1aca_2r1acb(self):
        try:
            price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            divide = price_tax_free / 2
            discount_ca = (divide * 40) / 100
            discount_cb = (divide * 30) / 100
            discount_passenger_total = discount_cb + discount_ca
            discount = price_tax_free - discount_passenger_total
            self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r2ad_2r1aca(self):
        try:
            price = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            divide_passenger = price / 3
            discount_total_ca = (divide_passenger * 40) / 100
            discount = price - discount_total_ca
            self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def hotel_discount_occupation_1r1a_2r1a1c1n(self):
        try:
            price_two_rooms = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            one_adult_room = (int(obtained_price_passenger(33160, 36443)) * 30) / 100
            two_adult_room = (int(obtained_price_passenger(33159, 36440)) * 20) / 100
            children = (int(obtained_price_passenger(33159, 36441)) * 40) / 100
            infant = (int(obtained_price_passenger(33159, 36442)) * 40) / 100
            self.context.discount_hotel = one_adult_room + two_adult_room + children + infant
            discount = price_two_rooms - self.context.discount_hotel
            self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount hotel: {self.context.ocupation}: ", str(e))

    def calculate_compensar_discount(self, price_tax_free, result_dict, categories):
        try:
            discount_total = 0
            new_taxes = 0
            percentage_taxes = vat_percentage_for_affiliate_discount()
            if isinstance(result_dict, list):
                for i, result in enumerate(result_dict):
                    c = categories[i]
                    discount_person = self.get_category_percentage(c)
                    discount = (result['Cost'] * discount_person) / 100
                    discount_total += discount
                    recalculate_cost = result['Cost'] - discount
                    recalculate_taxes = ((recalculate_cost * percentage_taxes) / 100) + result['BoardTaxes']
                    new_taxes += recalculate_taxes
            else:
                discounts = self.get_category_percentage(categories)
                for category_discount in discounts:
                    discount = (result_dict['Cost'] * category_discount) / 100
                    discount_total += discount
                    recalculate_cost = result_dict['Cost'] - discount
                    recalculate_taxes = ((recalculate_cost * percentage_taxes) / 100) + result_dict['BoardTaxes']
                    new_taxes += recalculate_taxes
            self.context.discount_total = round((price_tax_free + new_taxes) - discount_total)

        except Exception as e:
            raise Exception(f"Failed to process discount 'compensar': {str(e)}",)

    # calculate discount extras
    def identity_message_extras(self):
        try:
            occupancy_discount_method_extra = {
                '1re': self.extra_discount_occupation_1re,
                '1e_cb': self.extra_discount_occupation_1e_cb,
                '1e_cc': self.extra_discount_occupation_1e_cc,
                '3acabc': self.extra_discount_occupation_3acabc,
                '2ad_1c1n': self.extra_discount_occupation_2ad_1c1n,
            }
            occupancy_discount_method_extra[self.context.ocupation]()

        except Exception as e:
            raise Exception(f"Error processing discount extras: {self.context.ocupation}", e)

    def extra_discount_occupation_1re(self):
        try:
            if self.context.catmandu_sucursal == 'ext_mf':
                price_tax_free = self.context.price_obtained_in_passenger_page
                data_value_discount = self.mapping_discount_fixed_amount()['extra_category_a_mf']
                discount_fixed_amount = get_discount_fixed_amount_category(data_value_discount)
                price_tax_free = price_tax_free - discount_fixed_amount
                self.context.discount_total = price_tax_free
            else:
                price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
                discount_extra = (price_tax_free * 40) / 100
                discount = price_tax_free - discount_extra
                self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount extra: {self.context.ocupation}: ", str(e))

    def extra_discount_occupation_1e_cb(self):
        try:
            if self.context.catmandu_sucursal == 'ext_mf_cB':
                price_tax_free = self.context.price_obtained_in_passenger_page
                data_value_discount = self.mapping_discount_fixed_amount()['extra_category_b_mf']
                discount_fixed_amount = get_discount_fixed_amount_category(data_value_discount)
                price_tax_free = price_tax_free - discount_fixed_amount
                self.context.discount_total = price_tax_free

        except Exception as e:
            raise Exception(f"error calculating discount extra: {self.context.ocupation}: ", str(e))

    def extra_discount_occupation_1e_cc(self):
        try:
            if self.context.catmandu_sucursal == 'ext_mf_cc':
                price_tax_free = self.context.price_obtained_in_passenger_page
                data_value_discount = self.mapping_discount_fixed_amount()['extra_category_c_mf']
                discount_fixed_amount = get_discount_fixed_amount_category(data_value_discount)
                price_tax_free = price_tax_free - discount_fixed_amount
                self.context.discount_total = price_tax_free

        except Exception as e:
            raise Exception(f"error calculating discount extra: {self.context.ocupation}: ", str(e))

    def extra_discount_occupation_3acabc(self):
        try:
            price_tax_free = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            divide_result_extra = price_tax_free / 3
            discount_a = (divide_result_extra * 40) / 100
            discount_b = (divide_result_extra * 30) / 100
            discount_c = (divide_result_extra * 20) / 100
            discount_passenger_total_extra = discount_a + discount_b + discount_c
            discount = price_tax_free - discount_passenger_total_extra
            self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount extra: {self.context.ocupation}: ", str(e))

    def extra_discount_occupation_2ad_1c1n(self):
        try:
            extra_price = self.context.price_obtained_in_passenger_page
            p_extra = int(obtained_price_passenger_extra(24895))
            px_one = p_extra * 30 / 100
            px_two = p_extra * 20 / 100
            pc_extra = (int(obtained_price_passenger_extra(24896)) * 40) / 100
            pi_extra = (int(obtained_price_passenger_extra(24897)) * 40) / 100
            discount_ext = px_one + px_two + pc_extra + pi_extra
            discount = extra_price - discount_ext
            self.context.discount_total = discount

        except Exception as e:
            raise Exception(f"error calculating discount extra: {self.context.ocupation}: ", str(e))

    # calculate discount bus
    def identity_message_bus(self):
        try:
            occupancy_discount_method_bus = {
                '2adt_cca': self.bus_discount_occupation_2adt_cca,
                '3adt_cabc': self.bus_discount_occupation_3adt_cabc,
                '2adt_1c1n': self.bus_discount_occupation_2adt_1c1n,
            }
            occupancy_discount_method_bus[self.context.ocupation]()

        except Exception as e:
            raise Exception(f"Error processing discount bus: {self.context.ocupation}", e)

    def bus_discount_occupation_2adt_cca(self):
        try:
            price_bus = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            passenger_divide = price_bus / 2
            discount_total_cc = (passenger_divide * 20) / 100
            discount_total_ca = (passenger_divide * 40) / 100
            discount_cca = discount_total_cc + discount_total_ca
            discount = price_bus - discount_cca
            self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount extra: {self.context.ocupation}: ", str(e))

    def bus_discount_occupation_3adt_cabc(self):
        try:
            price_bus = self.context.price_obtained_in_passenger_page - self.context.value_total_taxes
            passenger_divide = price_bus / 3
            discount_bus_a = (passenger_divide * 40) / 100
            discount_bus_b = (passenger_divide * 30) / 100
            discount_bus_c = (passenger_divide * 20) / 100
            discount_bus_total = discount_bus_a + discount_bus_b + discount_bus_c
            discount = price_bus - discount_bus_total
            self.context.discount_total = discount + self.context.value_total_taxes

        except Exception as e:
            raise Exception(f"error calculating discount extra: {self.context.ocupation}: ", str(e))

    def bus_discount_occupation_2adt_1c1n(self):
        try:
            bus_price = self.context.price_obtained_in_passenger_page
            p_bus = (int(obtained_price_passenger_bus(10534)) * 2) + (int(obtained_price_passenger_extra(24892)) * 4)
            pb_one = p_bus * 30 / 100
            pb_two = p_bus * 20 / 100
            p_bus_c = (int(obtained_price_passenger_bus(10535)) * 2) + (int(obtained_price_passenger_extra(24893)) * 4)
            p_bus_i = (int(obtained_price_passenger_bus(10536)) * 2) + (int(obtained_price_passenger_extra(24894)) * 4)
            pb_c = p_bus_c * 40 / 100
            pb_i = p_bus_i * 40 / 100
            discount_bus_pre = pb_one + pb_two + pb_c + pb_i
            discount = bus_price - discount_bus_pre
            self.context.discount_total = discount

        except Exception as e:
            raise Exception(f"error calculating discount extra: {self.context.ocupation}: ", str(e))

    def get_price_page_passenger_after_discount_affiliate(self):
        WebDriverWait(self.context.browser, 60).until(
            EC.presence_of_all_elements_located(self.MESSAGE_CAUTION))

        price_passenger_total = self.context.browser.find_elements(*self.MESSAGE_CAUTION)
        convert_price = price_passenger_total[2].text  # TODO: get_price_text_in_passenger_page
        convert_price = convert_price.replace('.', '').replace('$ ', '')
        convert_price = (float(convert_price))
        self.context.get_price_passenger_total_discount = convert_price

    def get_category_percentage(self, categories):
        try:
            if isinstance(categories, list):
                discounts = []
                for category in categories:
                    data_value_discount = self.mapping_discount_fixed_amount().get(category)
                    if data_value_discount is not None:
                        discount = get_discount_percentage_amount_category(data_value_discount)
                        discounts.append(float(discount))
                return discounts
            else:
                data_value_discount = self.mapping_discount_fixed_amount().get(categories)
                if data_value_discount is not None:
                    discount = float(get_discount_percentage_amount_category(data_value_discount))
                    return discount

        except Exception as e:
            raise Exception(f"Error when obtaining discount percentages: ", e)

    def go_to_previous_page_affiliates(self):
        try:
            repeat = 2
            for i in range(repeat):
                self.context.browser.back()
            WebDriverWait(self.context.browser, 30)\
                .until(EC.element_to_be_clickable((By.XPATH, self.PRICE_FORM_PASSENGER_AFILIATE))).send_keys(Keys.TAB)
        except Exception as e:
            print(f"Error al navegar hacia atrás: {e}")

    def validate_discount_not_duplicated(self):
        # validate the discount
        assert self.context.discount_hotel == self.context.affiliate_discount_value, \
            f"{self.context.affiliate_discount_value} but this discount was expected {self.context.discount_hotel}"
        # validate the total
        assert self.context.discount_total == self.context.price_obtained_in_passenger_page, \
            f"{self.context.price_obtained_in_passenger_page} but this total was expected {self.context.discount_total}"

    def mapping_discount_fixed_amount(self):
        try:
            mapping_discount = {
                'hotel_category_a_mf': 25238,
                'extra_category_a_mf': 25240,
                'hotel_category_b_mf': 25242,
                'extra_category_b_mf': 25244,
                'hotel_category_c_mf': 25246,
                'extra_category_c_mf': 25248,
                'PLTU24_Cat_A_Lagomar_ADULTO': 25933,
                'PLTU24_Cat_B_Lagomar_ADULTO': 25934,
                'PLTU24_Cat_C_Lagomar_ADULTO': 25855,
                'PLTU24_Cat_A_Lagomar_NINO': 25856,
            }
            return mapping_discount
        except KeyError:
            raise KeyError("La clave no está presente en el diccionario de mapeo.")


