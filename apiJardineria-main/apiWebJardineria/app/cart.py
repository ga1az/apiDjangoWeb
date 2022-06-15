from typing_extensions import Self


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                "id": product.id,
                "nombre": product.name,
                "cantidad": 1,
                "precio": product.price,
                "img": product.image.url,
            }
        else:
            for key, value in self.cart.item():
                if key == str(product.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 0:
                    self.remove(product)
                else:
                    self.save()
                break

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True