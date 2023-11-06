import re
from playwright.sync_api import expect
from sc_video_shots.get_screenshot import screenshot
from time import sleep

class ProductCard:
    def __init__(self, page) -> None:
        self.page = page
        self.url = 'https://www.empik.com/reset,p1421190624,ebooki-i-mp3-p'
        self.response = page.request.get(self.url)

        self.addToCart_f_btn = page.get_by_role("button", name="Dodaj do koszyka").first
        self.addToCart_semicheckout_btn = page.get_by_role("button", name="PRZEJDŹ DO KOSZYKA", exact=True)
        #dla asercji
        self.price = page.get_by_text("1,99 zł").first
        self.descr_link = page.get_by_role("link", name="Opis produktu")
        self.details_link = page.get_by_role("link", name="Informacje szczegółowe")
        self.review_link = page.get_by_role("link", name="Recenzje", exact=True)
        self.aboutPrice_link = page.get_by_role("button", name="Informacje o cenie")

    def goToProductCartpage(self)->None:
        self.page.goto(self.url)
        # sprawdź czy strona zwraca kod 200
        expect(self.response).to_be_ok()
    def addToCart(self)->None:
        #dodanie produktu do koszyka
        self.addToCart_f_btn.click()
        #drugi klik do koszyka czyli przejście do checkout
        self.addToCart_semicheckout_btn.click()

    def productCart_assertions(self)->None:

        #wykoannie asercji czy strona jest OK dla usera, jeśli nie to zrób screenshota
        if not expect(self.aboutPrice_link).to_be_visible() or not expect(self.review_link).to_be_visible() or not expect(self.details_link).to_be_visible() or not expect(self.price).to_be_visible() or not expect(self.descr_link).to_be_visible():
            screenshot(self.page, __name__)