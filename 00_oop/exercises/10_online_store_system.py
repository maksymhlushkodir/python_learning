class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product: {self.name}, Price: ${self.price}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


class Cart:
    def __init__(self, __items : list=None):
        self.__items = __items
        if __items == None:
            self.__items = []

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return f'Cart has {len(self)} items, total price: ${self.total_price()}'

    def add_item(self, product):
        self.__items.append(product)
        print(f'{product} added to your cart')

    def total_price(self):
        total_price = 0
        for item in self.__items:
            total_price += item.price
        return total_price


# Create products
p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 25)

# Create cart
my_cart = Cart()
my_cart.add_item(p1)
my_cart.add_item(p2)

# This will now look beautiful because of __str__
print(p1)
print(my_cart)
print(p1.__eq__(p2))
print(my_cart.total_price())

# This works because of __len__
print(f"Items in cart: {len(my_cart)}")