from DOMs.loginOrRegister import SignInUp
from cookie_notify.cookies import Cookie
import pytest

def init(page) -> fpage_l:
    # Inicjalizacja obiektów
    fpage_l = SignInUp(page)
    cookie = Cookie(page)
    # Otwarcie strony
    fpage_l.goToSignInOrUp()
    # Akceptacja plików cookie
    cookie.acceptCookie()
    return fpage_l

# Test walidacji
@pytest.mark.parametrize('email', [('email@op.pl'), pytest.param('email.email.ps', marks=pytest.mark.xfail),
                                   pytest.param('SELECT * FROM users', marks=pytest.mark.xfail)])
def test_register(page, email):
    fpage_l = init(page)  # Inicjalizacja fpage_l za pomocą funkcji init
    fpage_l.filloutEmail(email)
    fpage_l.gotoLogin()

# w parametrze trzeba podać email, na który już jest zalożone konto
@pytest.mark.parametrize('email'[('vittorio.deejay@gmail.com')])
def test_login(page, email):
    fpage_l = init(page)
    fpage_l.filloutEmail(email)
    fpage_l.gotoLogin()