import random
from Crypto.PubKey import RSA

class bank:
    def __init__(self):
        self.past_ids = [] # past ecash uids
        self.accounts = [] # contains the user accounts
        self.pr = RSA.generate(2048)
        self.pu = pr.publickey()

    def addAccount(self, name, amount):
        self.accounts.append({name : amount})

    def modifyBalance(self, name, amount):
        for i in self.accounts:
            if name in i:
                if i.get(name) + amount < 0:
                    print("Not enough funds")
                else:
                    i[name] = i.get(name) + amount

    def validateCustomerOrders(self, orders):
        # remove secret order from the n-1 to validate
        secret_index = orders[1]
        secret_order = orders[0][secret_index] 
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
