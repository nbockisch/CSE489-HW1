import ecash
import string
import hashlib
from random import randint

class customer:
    cash = []

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.id_length = 32

        # Generate a customer ID
        self.cid = self.name + ", " + self.address + ", " + self.phone

    def generateOrders(n, amount):
        for i in range(0, n):
            cash[i] = ecash(amount, genBits(self.id_length))
            
            for j in range(0, n):
                pair = splitSecret():
                cash[i].addPair(commitBit(pair[0]), commitBit(pair[1]))

    def splitSecret():
        # generate random number
        r = str(''.join(random.choices(string.digits, k = len(self.cid))))
        s = ''

        for i in range(0, len(self.cid)):
            s += str(self.cid.encode('ascii')[i] ^ r.encode('ascii')[i])

        return (r, s)

    def commitBit(r):
        return hashlib.sha256(r.encode('ascii')).hexdigest()

    def genBits(length):
        return str(''.join(random.choices(string.digits, k = length)))
