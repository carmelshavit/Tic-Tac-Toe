"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

# class Backpack:
#
#     max_num_items = 10
#
#     def __init__(self):
#         self.items = []
#
#
# print(Backpack.max_num_items)
#
# my_backpack = Backpack()
# print(my_backpack.max_num_items)
#
# Backpack.max_num_items = 15
#
# print(Backpack.max_num_items)
# print(my_backpack.max_num_items)


class CashRegister:

    def __init__(self, name_cashier):
        self._products = {}
        self.name_cashier = name_cashier

    def has_product(self, product):
        return product in self._products

    def add_product(self, name, price, amount=1):
        if not amount > 0:
            raise ValueError("amount must be at least 1")
        if name in self._products:  # .keys():
            value = self._products[name]
            if value['price'] != price:
                # raise ValueError("price mismatch, ignoring new price")
                print("price mismatch, adding product with the current price")
            value['amount'] += amount
        else:
            self._products[name] = {'price': price, 'amount': amount}

    def update_product_price(self, name, new_price):
        if name in self._products:
            value = self._products[name]
            value['price'] = new_price

    def show_products(self):
        for name, value in self._products.items():
            price = value['price']
            amount = value['amount']
            print(f'{name} x {amount} ({price} each)')

    def remove_product(self, remove_name, amount_product=None):
        if remove_name not in self._products:
            return
        if amount_product is not None and self._products[remove_name]['amount'] - amount_product > 0:
            self._products[remove_name]['amount'] -= amount_product
        else:
            self._products.pop(remove_name)

    def total_taxes(self):
        tax_rate = 0.05
        tax_amount = self.calc_total_price() * tax_rate
        return tax_amount

    def total_after_taxes(self):
        return self.calc_total_price() + self.total_taxes()

    def clear_purchase(self):
        self._products = {}

    def calc_total_price(self):
        sum = 0
        for value in self._products.values():
            sum += value['amount'] * value['price']
        return sum

    # #  @property
    # #     def products(self):
    # #         return self._product

cash_register = CashRegister("Ronit")

cash_register.add_product("popcorn", 10, 3)
cash_register.add_product("choclate", 9.5, 1)
cash_register.add_product("popcorn", 14.5, 2)
cash_register.update_product_price("choclate",12)
cash_register.update_product_price(";lk;",12)
cash_register.show_products()
current_price=cash_register.calc_total_price()
print(current_price)
current_price=cash_register.calc_total_price()

cash_register.remove_product("popcorn")
cash_register.remove_product("popcorn", 6)
cash_register.show_products()


