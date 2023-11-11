from DOMs.productCard import ProductCard
from cookie_notify.cookies import Cookie
from DOMs.cartPage import Cart
from time import sleep

def test_addToCart(page)->None:
    #inicjalizacja obiektów
    pc_obj = ProductCard(page)
    cookie_obj = Cookie(page)
    cart_obj = Cart(page)

    #kliknięcie akceptacji w btn cookie
    pc_obj.goToProductCartpage()
    cookie_obj.acceptCookie()
    #asercja czy znajdujemy sie na poprawnej stronie
    pc_obj.productCart_assertions()

    pc_obj.addToCart()
    #przejście do sposobu dostawy

    cart_obj.responseCheckout()


