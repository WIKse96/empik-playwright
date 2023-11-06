from DOMs.Search import Search
import pytest
from cookie_notify.cookies import Cookie

# stringToSearch - tekst, ktory wpisujemy input
@pytest.mark.parametrize("stringToSearch", ['Python od podstaw'])
def test_search(page,stringToSearch)->None:
    hp_obj = Search(page)
    hp_obj.goToHomepage()
    cookie_obj = Cookie(page)
    cookie_obj.acceptCookie()
    hp_obj.searchProduct(stringToSearch)

