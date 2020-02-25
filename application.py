from customer import customer
from merchant import merchant
from bank import bank

def main():
    num_orders = 100
    amount = 5

    # set up bank
    b = bank()
    b.addAccount("Alice", 50)
    b.addAccount("Bob", 0)
    
    # set up customer
    alice = customer("Alice", "1234 Street Address", "999-999-9999")
    alice.generateOrders(num_orders, amount)

    # set up merchant
    bob = merchant()

    # show starting balances
    print("Alice's total before transaction: " + b.printBalance("Alice"))
    print("Bob's total before transaction: " + b.printBalance("Bob"))
    
    if b.validateCustomerOrders(alice.sendOrdersToBank(), alice.cash_ids):
        b.modifyBalance("Alice", amount * -1)
        order = alice.unblind(b.order_to_sign, alice.b_fac[alice.secret])

        if bob.verifyOrder(order, b.signOrder(order), b.pu):
            revealed = alice.revealStrings(bob.genRevealString(len(alice.cid)))
            b.validateMerchantOrder(order, revealed, bob.reveal_string)

    # show final balances
    print("Alice's total after transaction: " + b.printBalance("Alice"))
    print("Bob's total after transaction: " + b.printBalance("Bob"))

if __name__ == "__main__":
    main()
