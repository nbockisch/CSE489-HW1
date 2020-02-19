import ecash
import string
from random import randint

class customer:
    cash = []

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def generateOrders(n, amount):
        for i in range(0, n):
            cash[i] = ecash(amount, 

    def splitSecret(m):
        # generate random number
        r = int(''.join(random.choices(string.digits, k = len(str(m)))))
        s = m ^ r
        return (r, s)

    def commitBit(r):
        
