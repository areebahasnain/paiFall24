class Restaurant:
    def __init__(self):
        self.menu_items = {}  # Dictionary to store menu items with their prices
        self.booked_tables = []  # List to store booked table numbers
        self.customer_orders = []  # List to store customer orders

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def reserve_table(self, table_number):
        if table_number in self.booked_tables:
            print(f"Table {table_number} is already booked.")
        else:
            self.booked_tables.append(table_number)
            print(f"Table {table_number} has been reserved.")

    def customer_order(self, order_items):
        self.customer_orders.append(order_items)

    def print_menu(self):
        if not self.menu_items:
            print("No items in the menu.")
        else:
            print("Menu:")
            for item, price in self.menu_items.items():
                print(f"{item}: Rs.{price:.2f}")

    def print_table_reservations(self):
        if not self.booked_tables:
            print("No tables are reserved.")
        else:
            print("Reserved Tables:")
            for table in self.booked_tables:
                print(f"Table {table}")

    def print_customer_orders(self):
        if not self.customer_orders:
            print("No orders have been placed.")
        else:
            print("Customer Orders:")
            for index, orders in enumerate(self.customer_orders, start=1):
                print(f"Order {index}:")
                for item in orders:
                    print(f"  - {item}")

restaurant = Restaurant()

restaurant.add_item_to_menu("Burger", 599.0)
restaurant.add_item_to_menu("Pizza", 899.0)
restaurant.add_item_to_menu("Salad", 499.0)

restaurant.reserve_table(1)
restaurant.reserve_table(2)
restaurant.reserve_table(1)  # Trying to reserve an already reserved table

print("\n")

restaurant.customer_order(["Burger", "Salad"])
restaurant.customer_order(["Pizza"])

restaurant.print_menu()
print("\n")

restaurant.print_table_reservations()
print("\n")

restaurant.print_customer_orders()
