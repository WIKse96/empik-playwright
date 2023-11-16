from playwright.sync_api import expect
from sc_video_shots.get_screenshot import screenshot
import time

class SignInUp:
    def __init__(self,page)->None:
        self.page = page
        self.url = 'https://www.empik.com/logowanie?continue=%2Fpomoc%2Fkontakt'
        self.h2 = self.page.locator("//h2[contains(text(),'Zaloguj się lub zarejestruj')]")
        self.email_input = self.page.locator("//input[@id='user-email']")
        self.further_btn = self.page.get_by_role("button", name="DALEJ")
        self.error_p = self.page.get_by_text("Niepoprawny adres email")
        self.password_input = self.page.get_by_label("Hasło:")
        self.login_btn = self.page.get_by_role("button", name="ZALOGUJ SIĘ")
        self.changePassword = self.page.get_by_text("Nie pamiętam hasła")
#otwórz stronę pierwszą logowania
    def goToSignInOrUp(self):
        self.page.goto(self.url)
        response = self.page.request.get(self.url)
        # sprawdź czy strona zwraca kod 200
        expect(response).to_be_ok()

    def filloutEmail(self,email):
        self.email_input.fill(email)
    def gotoLogin(self):
        self.further_btn.click()
        expect(self.error_p).to_be_hidden()

#TODO Dodać scenariusz testowy przypomnienia hasła, zalogowania się, zmiany emaila, napisać scenariusz w html dodać test_