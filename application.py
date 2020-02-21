from customer import customer

def main():
    num_orders = 100
    amount = 5

    # set up customer
    alice = customer("Alice", "1234 Street Address", "999-999-9999")
    alice.generateOrders(num_orders, amount)

    # blind money orders
    for i in range(0, num_orders):


if __name__ == "__main__":
    main()
