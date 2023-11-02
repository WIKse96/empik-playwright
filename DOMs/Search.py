import re
from playwright.sync_api import expect
from sc_video_shots.get_screenshot import screenshot
from time import sleep
class Search:
    def __init__(self, page)->None:
        self.page = page
        self.url = "https://empik.com"
        self.search_input = page.get_by_placeholder("Wpisz czego szukasz")
        self.search_btn = page.locator("xpath=//button[@class='css-clgzww-root-m']")
        self.productTitle_h2 = page.locator("xpath=//h2/a/strong[@class='ta-product-title']")
        self.response = page.request.get(self.url)

    # Otwórz stronę główną
    def goToHomepage(self)->None:
        self.page.goto(self.url)
        # sprawdź czy strona zwraca kod 200
        expect(self.response).to_be_ok()


    def searchProduct(self, searchText:str)->None:
        self.search_input.fill(searchText)
        self.search_btn.click()
        #czy na stronie wyników wyszukiwania w pierwszym elemencie znajduje się szukany tekst, jeśli nie zrób screenshota
        if not searchText in self.productTitle_h2.first.text_content():
            sleep(2)
            screenshot(self.page, __name__)


