class Product:
    def __init__(self):
        self.name = input("Hay nhap ten hang hoa: ")
        self.price = int(input("Hay nhap gia cua hang hoa: "))

    def print_infor(self):
        print(f'{self.name} -- {self.price}')

    def update_price(self, new_price):
        self.price = new_price

    def update_name(self, new_name):
        pass

# product_1 = Product()
# product_1.print_infor()


class Product_list:
    def __init__(self):
        self.product_list = []

    def add_product(self):
        new_product = Product()
        self.product_list.append(new_product)

    def print_infor(self):
        for product in self.product_list:
            product.print_infor()

    def del_product(self):
        pass

    def update_product(self):
        self.product_list[0].update_price(30)


class bill():
    def __init__(self):
        self.buying_list = {}
        self.total = 0

    def buy(self, product, quantity):
        self.buying_list[product] = quantity

product_list_1 = Product_list()
product_list_1.add_product()
product_list_1.add_product()
product_list_1.update_product()
product_list_1.print_infor()
