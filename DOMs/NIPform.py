import re
from playwright.sync_api import expect
from sc_video_shots.get_screenshot import screenshot
from time import sleep

class NIPform:
    def __init__(self, page)->None:
        self.page = page
        self.url = "https://www.empik.com/empikplace/wniosek"
        self.response = page.request.get(self.url)
        self.header = page.get_by_role("heading", name="Formularz zgłoszeniowy")
        self.h1 = page.get_by_role("heading", name="Uzupełnij dane firmy")
        self.shippingCountry_select = page.locator("select[name=\"shipping_country\"]")
        self.countryOfRegister_select = page.locator("select[name=\"country\"]")
        self.nip_input = page.locator("//input[@name='tax_identification_number']")
        self.downloadData_btn = page.get_by_role("button", name="Pobierz dane firmy")
        self.further_btn = page.get_by_role("button", name="dalej")

        #inputy, które pojawiają się dopiero po wybraniu innegro kraju rejestracji firmy niż Polska
        self.registerName_input = page.locator("input[name=\"corporate_name\"]")
        self.address_input = page.locator("input[name=\"street1\"]")
        self.bankName_input = page.locator("input[name=\"bank_name\"]")
        self.bankAccount_input = page.locator("input[name=\"bank_name\"]")
        self.bankIban_input = page.locator("input[name=\"iban\"]")
        self.bankBic_input = page.locator("input[name=\"bic\"]")

    #Otwórz stronę do testów
    def gotoNIPform(self):
        self.page.goto(self.url)
        expect(self.response).to_be_ok()

    #asercje pól i obiektów
    def asserionNipForm(self)-> None:
        expect(self.header).to_be_visible()
        expect(self.further_btn).to_be_disabled()
        expect(self.downloadData_btn).to_be_disabled()
        expect(self.nip_input).to_be_editable()
        expect(self.countryOfRegister_select).to_be_visible()
        expect(self.shippingCountry_select).to_be_visible()
        expect(self.h1).to_be_visible()
        expect(self.header).to_be_visible()

        #jeśli z któryś elementow się nie wyświetla to zrób screenshota
        if (not self.header and not self.h1 and not self.shippingCountry_select
        and not self.countryOfRegister_select and not self.nip_input):
            screenshot(page, __name__)
    #wpisz nip, wybierz kraj wysylki, kraj rejestracji firmy. Jeśli inny niż polska to czy są dodatkowe pola input
    def nipFormFillout(self, country_of_register, shipping_country, nip_ints) -> None:
        self.countryOfRegister_select.select_option(value=country_of_register)
        self.shippingCountry_select.select_option(value=shipping_country)

        # Wyczyszczenie pola <select>
        self.nip_input.fill(value='')

        # Wybór wartości w polu <select>
        self.nip_input.fill(value=nip_ints)

        if country_of_register != 'POL':
            # Pozostała część kodu bez zmian
            expect(self.bankBic_input).to_be_editable()
            expect(self.bankIban_input).to_be_editable()
            expect(self.bankAccount_input).to_be_editable()
            expect(self.bankName_input).to_be_editable()
            expect(self.registerName_input).to_be_editable()
            expect(self.address_input).to_be_editable()

            if (not self.bankBic_input and not self.bankIban_input and not self.bankAccount_input and
                    not self.bankName_input and not self.registerName_input and not self.address_input):
                screenshot(self.page, __name__)

            self.bankBic_input.fill('13245')
            self.bankIban_input.fill('15645')
            self.bankAccount_input.fill('2255')
            self.bankName_input.fill('456468')
            self.registerName_input.fill("BANK im. prof. Glapińskiego")
            self.address_input.fill("Adress 12/5")
