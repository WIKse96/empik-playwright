from DOMs.NIPform import NIPform
from cookie_notify.cookies import Cookie
import pytest


# parametry r_country i s_country podać skrót kraju np. POL, DEU, LUX
@pytest.mark.parametrize("r_country",['POL', 'LTU', 'PRT'])
@pytest.mark.parametrize("s_country",['DEU', 'LUX', 'GRC'])
@pytest.mark.parametrize("nip",[132466, 65488, 8978])
# @pytest.mark.parametrize('r_country,s_country,nip',[('POL','POL','64654')])
def test_simpleNipForm(page, r_country, s_country, nip)->None:
    #inicjacja obiektów
    nip_obj = NIPform(page)
    cookie_obj = Cookie(page)

    nip_obj.gotoNIPform()
    cookie_obj.acceptCookie()
    nip_obj.asserionNipForm()

    #r_country i s_country podać skrót kraju np. POL, DEU, LUX
    nip_obj.nipFormFillout(r_country, s_country, nip)