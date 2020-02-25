import random

class merchant:
    def __init__(self):
        self.order = None
        self.reveal_string = None

    def verifyOrder(self, order, signature, bank_key):
        self.order = order
        return bank_key.verify(order, (signature, )) 

    def genRevealString(self, n):
        self.reveal_string = ''.join(random.choices(["0", "1"], k = n)) 
        return self.reveal_string
