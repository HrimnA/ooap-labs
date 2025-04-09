from abc import ABC, abstractmethod

class Order:
    def __init__(self, customer_type, size, shipping_method, destination):
        self.customer_type = customer_type
        self.size = size
        self.shipping_method = shipping_method
        self.destination = destination

class OrderHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler
        return next_handler

    @abstractmethod
    def handle(self, order: Order):
        if self.next_handler:
            return self.next_handler.handle(order)
        else:
            print("[System] Замовлення не може бути оброблене.")

class RegularCustomerHandler(OrderHandler):
    def handle(self, order: Order):
        if order.customer_type == "regular":
            print("Обробка замовлення для звичайного клієнта.")
        else:
            super().handle(order)

class LargeOrderHandler(OrderHandler):
    def handle(self, order: Order):
        if order.size == "large":
            print("Обробка великого замовлення.")
        else:
            super().handle(order)

class ExpressShippingHandler(OrderHandler):
    def handle(self, order: Order):
        if order.shipping_method == "express":
            print("Обробка замовлення з експрес-доставкою.")
        else:
            super().handle(order)

class InternationalOrderHandler(OrderHandler):
    def handle(self, order: Order):
        if order.destination == "international":
            print("Обробка міжнародного замовлення.")
        else:
            super().handle(order)

# Формування ланцюжка обробки
handler_chain = RegularCustomerHandler()
handler_chain.set_next(LargeOrderHandler()).set_next(ExpressShippingHandler()).set_next(InternationalOrderHandler())

order1 = Order("regular", "medium", "standard", "local")
order2 = Order("business", "large", "standard", "international")
order3 = Order("vip", "small", "express", "local")
order4 = Order("vip", "small", "standard", "local")

print("\nОбробка першого замовлення:")
handler_chain.handle(order1)
print("\nОбробка другого замовлення:")
handler_chain.handle(order2)
print("\nОбробка третього замовлення:")
handler_chain.handle(order3)
print("\nОбробка четвертого замовлення:")
handler_chain.handle(order4)