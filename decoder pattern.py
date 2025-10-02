# Decorator Pattern demo: Coffee add-ons
class Coffee:
    def cost(self):
        return 50

class MilkDecorator(Coffee):
    def __init__(self, base): self.base = base
    def cost(self):
        return self.base.cost() + 10

class SugarDecorator(Coffee):
    def __init__(self, base): self.base = base
    def cost(self):
        return self.base.cost() + 5


coffee = Coffee()
print("Plain:", coffee.cost())
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
print("With Milk+Sugar:", coffee.cost())
