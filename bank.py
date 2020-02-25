import random
from Crypto.PublicKey import RSA

class bank:
    def __init__(self):
        self.past_ids = [] # past ecash uids
        self.accounts = [] # contains the user accounts
        self.pr = RSA.generate(2048)
        self.pu = self.pr.publickey()
        self.order_to_sign = None
        self.id_strings = None
        self.order_index = None

    def addAccount(self, name, amount):
        self.accounts.append({name : amount})

    def modifyBalance(self, name, amount):
        for i in self.accounts:
            if name in i:
                if i.get(name) + amount < 0:
                    print("Not enough funds")
                else:
                    i[name] = i.get(name) + amount
    
    def printBalance(self, name):
        for i in self.accounts:
            if name in i:
                return str(i.get(name))

    def validateCustomerOrders(self, orders, id_strings):
        # remove secret order from the n-1 to validate
        secret_index = orders[1]
        self.id_strings = id_strings[secret_index]
        self.order_to_sign = orders[0][secret_index] 
        self.order_index = secret_index
        validate = []
        j = 0
        value = 0

        for i in range(0, len(orders[0])):
            if (i != secret_index):
                validate.append(orders[0][i])

        for val in validate:
            tmp = []
            tmp = val.decode('utf-8').split(", ")
            
            if j == 0:
                value = tmp[0]

            # check ecash uid
            if tmp[1] in self.past_ids:
                return False
            else:
                self.past_ids.append(tmp[1])

            # check amount
            if value != tmp[0]:
                return False

            j += 1

        return True

    def validateMerchantOrder(self, order, merch_id_string, bit_rev_string):
        # validate signature
        if self.pu.verify(order, (self.signOrder(order), )):
            uid = order.decode('utf-8').split(", ")[1]
            if uid in self.past_ids:
                # reject if uid already in past database
                print("Double spending alert!")
                order_id_string = self.id_strings[self.order_index]
                i = 0

                for c in bit_rev_string:
                    if c == "1":
                        if order_id_string[0][1][i] != merch_id_string[i]:
                            print("Customer cheated!")
                            customer_id = order_id_string[0][1] ^ order_id_string[0][0]
                            print("Customer: " + str(customer_id))
                            break
                    elif c == "0":
                        if order_id_string[0][0][i] != merch_id_string[i]:
                            print("Customer cheated!")
                            customer_id = order_id_string[0][1] ^ order_id_string[0][0]
                            print("Customer: " + str(customer_id))
                            break

                    i += 1

                print("Merchant cheated!")

            else:
                self.modifyBalance("Bob", int(order.decode('utf-8').split(", ")[0]))
                self.past_ids.append(uid)
                
    def signOrder(self, order):
        return self.pr.sign(order, self.pr.n)[0]
