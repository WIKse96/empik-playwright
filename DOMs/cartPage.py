from playwright.sync_api import expect
from sc_video_shots.get_screenshot import screenshot
class Cart:
    def __init__(self, page):
        self.page = page
        self.url = 'https://www.empik.com/cart/'
        self.response = page.request.get(self.url)
        self.goToCheckout_btn = page.get_by_text("Wybierz sposób dostawy")
        self.clickboard_link = page.get_by_text("zapisz na później")
        self.premium_label = page.get_by_text("premium", exact=True)
        self.freeDelivery = page.get_by_text("dostawa 0 zł")

    def responseCheckout(self)->None:
        # sprawdź czy strona zwraca kod 200
        expect(self.response).to_be_ok()
        #przejdz dalej
        self.goToCheckout_btn.click()

    def cart_assertions(self)->None:
        if not expect(self.goToCheckout_btn).to_be_visible() or not expect(self.clickboard_link).to_be_visible() or not expect(self.freeDelivery).to_be_visible() or not expect(self.goToCheckout_btn).to_be_visible():
            screenshot(self.page, __name__)

