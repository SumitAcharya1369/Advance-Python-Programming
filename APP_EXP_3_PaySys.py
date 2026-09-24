# implement a configurable payment processing system
# using strategy pattern

class CreditCardPayment:   # made the 3 payment strategies
    def pay(self, amount):
        self.amount = amount
        print(f"paid rupees {self.amount} using credit card")

class UpiPayment:
    def pay(self, amount):
        self.amount = amount
        print(f"paid rupees {self.amount} using upi")

class PayPalPayment:
    def pay(self, amount):
        self.amount = amount
        print(f"paid rupees {self.amount} using paypal")

class PaymentProcessor: # created the context class
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def set_strategy(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)

c = PaymentProcessor(UpiPayment())
amount = 100000000
c.process_payment(amount) # make obj in contxt class not strat class

d = PaymentProcessor(CreditCardPayment())
amount = 4000000
d.process_payment(amount)

e = PaymentProcessor(PayPalPayment())
amount = 6000000
e.process_payment(amount)



