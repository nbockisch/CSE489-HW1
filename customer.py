from ecash import ecash
import string
import hashlib
import random as rand
from random import randint
from math import gcd
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Random import random

class customer:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.id_length = 32
        self.cash = []
        self.cash_ids = []
        self.rsa_priv = RSA.generate(2048)
        self.rsa_pub = self.rsa_priv.publickey()
        self.b_fac = [] # blinding factors
        self.blinded = [] # blinded ecash

        # Generate a customer ID
        self.cid = self.name + ", " + self.address + ", " + self.phone
        self.secret = 0

    def genBits(self, length):
        return int(''.join(rand.choices(string.digits, k = length)))

    def generateOrders(self, n, amount):
        for i in range(0, n):
            self.cash.append(ecash(amount, self.genBits(self.id_length)))
            self.cash_ids.append([])
            self.b_fac.append(random.getrandbits(64))
            self.blinded.append(self.blind(self.cash[i].toString(), self.b_fac[i]))
            
            for j in range(0, n):
                pair = self.splitSecret()
                self.cash[i].addPair(self.commitBit(pair[0]), self.commitBit(pair[1]))
                self.cash_ids[i].append(pair)

    def splitSecret(self):
        # generate random number
        r = str(''.join(rand.choices(string.digits, k = len(self.cid))))
        s = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(r, self.cid)) 
        
        return (r, s)

    def commitBit(self, r):
        return hashlib.sha256(r.encode('utf-8')).hexdigest()

    def blind(self, m, r):
        return self.rsa_pub.blind(bytes(m.encode('utf-8')), r)

    def unblind(self, m, r):
        return self.rsa_pub.unblind(m, self.rsa_pub.encrypt(r, self.rsa_priv.n)[0])

    def sendOrdersToBank(self):
        # unblind N - 1 orders
        self.secret = rand.randint(0, len(self.blinded))
        orders = []

        for i in range(0, len(self.blinded)):
            if i != self.secret:
                orders.append(self.unblind(self.blinded[i], self.b_fac[i]))
            else:
                orders.append(self.blinded[i])

        return (orders, self.secret)

    def revealStrings(self, reveal_string):
        tmp = ""
        i = 0
        
        for c in reveal_string:
             if c == "1":
                 tmp += str(self.cash_ids[self.secret][self.secret][1][i])
             elif c == "0":
                 tmp += str(self.cash_ids[self.secret][self.secret][0][i])

             i += 1
                 
        return tmp 
