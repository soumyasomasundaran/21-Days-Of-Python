class Customer:
    def __init__(self, customer_id, quantity, price):
        self.customer_id = customer_id
        self.quantity = quantity
        self.price = price
        self.discount = 0

    def generate_bill(self):
        price = self.quantity * self.price
        self.discount_amount = price * self.discount
        return price - self.discount_amount


class SilverCustomer(Customer):
    def __init__(self, id, quantity, price):
        super().__init__(id, quantity, price)
        self.discount = 10 / 100


class GoldCustomer(Customer):
    def __init__(self, id, quantity, price):
        Customer.__init__(self, id, quantity, price)
        self.discount = 20 / 100

customer_zero = Customer('C123',10,100)
print("Your bill amount is ",customer_zero.generate_bill())

customer_one = SilverCustomer('C234',10,100)
print("Your bill amount is ",customer_one.generate_bill())


customer_two = GoldCustomer('C334',10,100)
print("Your bill amount is ",customer_two.generate_bill())

