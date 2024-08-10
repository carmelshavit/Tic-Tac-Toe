"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

# class Dog:
#
#     species = "Canis Lupus"
#
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#
# print(Dog.species)

class BouncyBall:

        def __init__(self, price, size, brand):
            self._price = price
            self._size = size
            self._brand = brand


        @property
        def price(self):
            return self._price

        @property
        def size(self):
            return self._size

        @property
        def brand(self):
            return self._brand

        @price.setter
        def price(self, new_price):
            self._price = new_price

        @brand.setter
        def brand(self, new_brand):
            self._brand = new_brand

        @size.setter
        def size(self, new_size):
            self._size = new_size

            # getting the values

        def get_brand(self):
            print('Getting brand')
            return self._brand

            # setting the values

        def set_brand(self, brand):
            print('Setting brand to ' + size)
            self._size = size

            # deleting the values



        brand = property(getBrand, setBrand, )