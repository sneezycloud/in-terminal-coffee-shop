from customer_data import CustomerData
from menus import (tea_list, coffee_list, books_list, smoothies_list)

class CaffeineCloud:
    def __init__(self):
        # set the initial menus from the menus file
        self.tea = tea_list
        self.coffee = coffee_list
        self.books = books_list
        self.smoothies = smoothies_list

        self.order = []
        self.total = 0.0
        self.customer_data = CustomerData()

    def print_menu(self, heading, menu):            
        print(f"\n{heading}:")
        if menu is self.books:  # for books, we print more than just the price
            for book, info in menu.items():
                print(f"{book}: £{info["price"]:.2f}")
                print(f"\tby {info["author"]}")
                print(f"\tGenre: {info["genre"]}")
        else:
            for item, price in menu.items():
                print(f"{item}: £{price:.2f}")

    def purchase_from_menu(self, heading, menu):
        self.print_menu(heading, menu)
        pick = input("\nPlease enter your chosen items below (if multiple, please separate items by ','): ")
        if pick.strip() == "":
            return
        items = [item.strip().title() for item in pick.split(",")]
        for item in items:
            if item in menu:
                if menu is self.books:  # for books, we get the price from each book's dictionary
                    price = menu[item]["price"]
                else:  # for everything else, the price is directly in the menu dictionary
                    price = menu[item]
                self.order.append((item, price))
                self.total += price
                print(f"\nThe following items have been added: {item}")
                print(f"Your current total is: £{self.total:.2f}")
            else:
                print(f"\nItem cannot be found: {item}")

    def checkout(self):
        print("\nYour current order:")
        for item, price in self.order:
            print(f"{item}, £{price:.2f}")
            if item in self.tea:
                item_type = "tea"
            elif item in self.coffee:
                item_type = "coffee"
            elif item in self.smoothies:
                item_type = "smoothie"
            else:  # we don't add items to self.order that aren't in one of the menus, so anything else is a book
                item_type = "book"
            self.customer_data.add_purchase(item, item_type, price)
        print(f"\nTotal: £{self.total:.2f}")
        print("\nThank you for shopping at Caffeine Cloud!")
        self.customer_data.next_customer()

    def start(self):
        print("Welcome to Caffeine Cloud!!")
        while True:
            print("\nWhat can I get you?")
            print("1. Buy teas/coffees")
            print("2. Buy smoothies")
            print("3. Buy books")
            print("4. Checkout")
            print("5. Exit")
            pick = input("Please select an option: ").strip()

            if pick == "1":
                self.purchase_from_menu("Tea & Coffee menu", self.tea | self.coffee)
            elif pick == "2":
                self.purchase_from_menu("Smoothie menu", self.smoothies)
            elif pick == "3":
                self.purchase_from_menu("Our current book selection", self.books)
            elif pick == "4":
                self.checkout()
                print(f"\nNow serving customer #{self.customer_data.current_customer}.")
            elif pick == "5":
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    store = CaffeineCloud()
    store.start()
