from playwright.sync_api import expect
from time import sleep
from sc_video_shots.get_screenshot import screenshot
import re

class Cookie:
    #jeśli chcę testować cookie w pliku conftest.py trzeba przestawić  accept_cookies=False
    def __init__(self, page)->None:
        self.page = page
        self.url = 'https://empik.com'
        self.cookieContainer = page.locator('xpath=//div[@class="css-1u48hnv-title-title-1"]')
        self.acceptCookie_btn = page.get_by_role("button", name="Zaakceptuj zgody")
        self.customize_link = page.get_by_role("button", name="Dostosuj zgody")
        self.cust_analy_switch = page.locator(".css-2amr1r-slider-slider").first
        self.cust_funct_switch = page.locator("div:nth-child(2) > .css-amarrj-consentSwitch > .css-57f0c1-switcher-switcher > .css-2amr1r-slider-slider")
        self.cust_marketing_switch=page.locator(
            "div:nth-child(3) > .css-amarrj-consentSwitch > .css-57f0c1-switcher-switcher > .css-2amr1r-slider-slider")
        self.cust_social_switch=page.locator(
            "div:nth-child(4) > .css-amarrj-consentSwitch > .css-57f0c1-switcher-switcher > .css-2amr1r-slider-slider")
        self.saveoptions_link = page.get_by_role("button", name="Zapisz ustawienia")
        self.acceptAll_btn = page.get_by_role("button", name="Zaakceptuj wszystkie zgody")
        self.identifyCookie_p = page.get_by_text("Prywatność UżytkownikaTak jak w innych serwisach internetowych, w empik.com wyko")
        self.response = page.request.get(self.url)
    def hp_run(self)->None:
        self.page.goto(self.url)
        #sprawdź czy strona zwraca kod 200
        expect(self.response).to_be_ok()

    def acceptCookie(self, accept:bool=True)->None:
        #zaakceptuj jeśli accept True
        if accept:
            self.acceptCookie_btn.click()


            #sprawdź czy powiadomienie cookie jest ukryte a jesli nie to zrób screenshota
            if not expect(self.acceptCookie_btn).to_be_hidden():
                screenshot(self.page, __name__)


    def customizeCookie(self, analys:bool=True,funct:bool=True,marketing:bool=True,social:bool=True)->None:

        self.customize_link.click()
        # Jeśli True to zaznaczam danego switcha.
        if analys:
            self.cust_analy_switch.click()
        if funct:
            self.cust_funct_switch.click()
        if marketing:
            self.cust_marketing_switch.click()
        if social:
            self.cust_social_switch.click()
        #zapisz opcje
        self.saveoptions_link.click()
        # sprawdź czy powiadomienie cookie jest ukryte
        if not expect(self.saveoptions_link).to_be_hidden():
            screenshot(self.page,__name__)

    def customizeAcceptAll(self)->None:
        #Wchodzę w zaawansowane opcje i klikam zaznacz wszyskie cookie
        self.customize_link.click()
        self.acceptAll_btn.click()
        # sprawdź czy powiadomienie cookie jest ukryte, jeśli nie zrób screenshota
        if not self.acceptAll_btn:
            screenshot(self.page,__name__)
        #Wykonanie asercji playwright
        expect(self.acceptAll_btn).to_be_hidden()

