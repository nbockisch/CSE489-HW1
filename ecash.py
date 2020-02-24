class ecash:
    """
    @param amount The value of the transaction
    @param uid The uniqueness string number
    @param cid The customer ID
    @param sig The bank signature
    """
    def __init__(self, amount, uid):
        self.amount = amount
        self.uid = uid
        self.id_pairs = []

    def addPair(self, left, right):
        self.id_pairs.append((left, right))

    def toString(self):
        return str(self.amount) + ", " + str(self.uid)
