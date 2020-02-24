from customer import customer
from bank import bank

def main():
    num_orders = 100
    amount = 5

    # set up bank
    b = bank()
    b.addAccount("Alice", 50)
    
    # set up customer
    alice = customer("Alice", "1234 Street Address", "999-999-9999")
    alice.generateOrders(num_orders, amount)

    if b.validateCustomerOrders(alice.sendOrdersToBank()):
        b.modifyBalance("Alice", amount)

if __name__ == "__main__":
    main()
