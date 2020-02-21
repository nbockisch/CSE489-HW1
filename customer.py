from ecash import ecash
import string
import hashlib
import random
from random import randint
from math import gcd
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

class customer:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.id_length = 32
        self.cash = []

        # Generate a customer ID
        self.cid = self.name + ", " + self.address + ", " + self.phone

    def genBits(self, length):
        return str(''.join(random.choices(string.digits, k = length)))

    def generateOrders(self, n, amount):
        for i in range(0, n):
            self.cash.append(ecash(amount, self.genBits(self.id_length)))
            
            for j in range(0, n):
                pair = self.splitSecret()
                self.cash[i].addPair(self.commitBit(pair[0]), self.commitBit(pair[1]))

    def splitSecret(self):
        # generate random number
        r = str(''.join(random.choices(string.digits, k = len(self.cid))))
        s = ''

        for i in range(0, len(self.cid)):
            s += str(self.cid.encode('ascii')[i] ^ r.encode('ascii')[i])

        return (r, s)

    def commitBit(self, r):
        return hashlib.sha256(r.encode('ascii')).hexdigest()

    def blind(self, m):
        # generate blinding factor
        r = 5
        while (gcd(r, 255) != 1):
            r = randint(1, 254)

        # get private and public keys
        pr = RSA.generate(2048)
        pu = pr.publickey()

        # perform RSA blinding
        m_hash = SHA256.new(m.encode('ascii')).digest()
        blind = pu.blind(m_hash, r)
        #sign = pr.sign(blind, pr.n)[0]
        
        return (blind, r)
