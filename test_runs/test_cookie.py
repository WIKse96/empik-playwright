import pytest
from cookie_notify.cookies import Cookie


#Testowanie cookie
@pytest.mark.parametrize("accept",[(True)])
def test_simpleCookie(page, accept)->None:
    cookie_obj = Cookie(page)
    cookie_obj.hp_run()
    cookie_obj.acceptCookie(accept)

#dane wejściowe dla testu checków
@pytest.mark.parametrize("analys",[(False)])
@pytest.mark.parametrize("funct, social",[(True,False,)])
@pytest.mark.parametrize("marketing",[(False)])
def test_customizeCookies(page, analys,funct,marketing,social)->None:
    cookie_obj = Cookie(page)
    cookie_obj.hp_run()
    cookie_obj.customizeCookie(analys,funct,marketing,social)

#przetestuj zaznaczenie wszystkich opcji cookie
def test_customizeAllChecked(page)->None:
    cookie_obj = Cookie(page)
    cookie_obj.hp_run()
    cookie_obj.customizeAcceptAll()