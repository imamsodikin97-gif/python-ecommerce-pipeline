from Order import Orders

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self, tax_rate):
        total_revenue = 0
        for order in self.orders:
            total_revenue += order.total_amount
        return total_revenue
        
    def display_orders(self):
        print("===== Detail Orders =====")
        for order in self.orders:
            order.display_order()
            print("-------------------------")

pesanan1 = Orders(1, "Budi", "2022-01-01", 100000)
pesanan2 = Orders(2, "Andi", "2022-01-01", 100000)
pesanan3 = Orders(3, "Siti", "2022-01-01", 100000)

order_processor = OrderProcessor()
order_processor.add_order(pesanan1)
order_processor.add_order(pesanan2)
order_processor.add_order(pesanan3)
order_processor.display_orders()

print("List Orders : ", order_processor.orders)
print("Total Revenue: ", order_processor.calculate_total_revenue(0.1))
