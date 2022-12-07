# class ProductPriceError(Exception):
#     pass
# class product:
#     def __init__(self, name, sku, price):
#         self.name = name
#         self.sku = sku
#         self.__price = price

#     @property    
#     def price(self):
#         return self.__price 
 
#     @price.setter
#     def price(self, price):
#         if price <= 0:
#             raise ProductPriceError("Price can not be smaller than zero")
#             return
#         self.__price = price  

# tshirt = product("T-shirt", "123", 500)
# print(tshirt.__dict__)
# try:
#     tshirt.price = -1
# except ProductPriceError as err:
#     print(err)    
#     print(tshirt.__dict__)

class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

    def difference(self):
        return self.num1 - self.num2

    def product(self):
        return self.num1 * self.num2 

    @staticmethod
    def sqrt(num):
        return num**0.5  

c = calculator( 20, 10)
print(c.add())
print(c.difference())
print(c.product())
print(calculator.sqrt(25))                  

        