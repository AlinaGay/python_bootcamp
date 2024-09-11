class Customer:
    def __init__(self, name):
        self.name = name
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, price):
        price_with_dicscount = round((price * (100 - self.__discount)/100), 2)
        return price_with_dicscount

    def set_discount(self, new_discont):
        if new_discont > 80:
            self.__discount = 80
        else:    
            self.__discount = new_discont


customer = Customer("Иван Иванович")
customer.get_price(100)
customer.set_discount(20)
customer.get_price(100)