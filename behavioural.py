# Strategy Pattern demo: Payment methods
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class Checkout:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)

if __name__ == "__main__":
    Checkout(CreditCardPayment()).process(100)
    Checkout(PayPalPayment()).process(200)
