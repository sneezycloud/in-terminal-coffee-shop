"""
Module usage:
    
    from customer_data import CustomerData

    cust_data = CustomerData()

Then call methods on that same cust_data wherever a purchase happens or when code wants to look
up customer information.
"""

class CustomerData():
    """
    Creates an object to update customer data based on purchases, and retrieve customer lists or
    information about each customer.

    Summary of methods:
    - next_customer increases the current customer number
    - add_purchase creates or updates purchase records for the current customer
    - get_customers retrieves a list of all customer numbers that made purchases
    - get_customer_total_spend retrieves a customer's total spend by customer number
    - get_customer_purchases retrieves a customer's purchases by customer number, and optionally
      filters that list by purchase type
    """

    def __init__(self):
        """
        Create a new customer data store with no information.
        """
        self.customer_info = {}
        self.current_customer = 1

    def next_customer(self):
        self.current_customer += 1

    def add_purchase(self, purchased_item, purchase_type, price):
        """
        Record a purchase for the current customer.
        Takes 3 arguments:
        - The name of the item they purchased
        - The type of the item they purchased (expected: "tea" or "coffee" or "smoothie" or "book")
        - The price of the item they purchased
        """
        if self.current_customer not in self.customer_info:
            # If we don't have a record for this customer, create initial record with no purchases.
            self.customer_info[self.current_customer] = {
                "purchases": [],
                "total_spend": 0.00
            }

        # Now, we record this purchase and increase the customer's total spend.
        self.customer_info[self.current_customer]["purchases"].append({
            "name": purchased_item,
            "type": purchase_type,
            "price": price
        })
        self.customer_info[self.current_customer]["total_spend"] += price

    def get_customers(self):
        """
        Returns a list of all customer numbers that have recorded purchases.
        """
        return list(self.customer_info.keys())

    def get_customer_total_spend(self, customer_number):
        """
        Given a customer number, returns customer's total spend, or None if customer is not in
        the records.
        """
        if customer_number in self.customer_info:
            return self.customer_info[customer_number]["total_spend"]
        else:
            return None

    def get_customer_purchases(self, customer_number, purchase_type=None):
        """
        Given a customer number, returns a list of customer's purchases, or None if customer
        is not in the records.
        Optionally, a purchase type may also be supplied, in which case the returned list
        will contain only purchases of that type.
        """
        if customer_number in self.customer_info:
            if purchase_type is None:
                return self.customer_info[customer_number]["purchases"]
            else:
                filtered_purchases = []
                for purchase in self.customer_info[customer_number]["purchases"]:
                    if purchase["type"] == purchase_type:
                        filtered_purchases.append(purchase)
                return filtered_purchases
        else:
            return None