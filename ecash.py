class ecash:
    id_pairs = []

    """
    @param amount The value of the transaction
    @param uid The uniqueness string number
    @param cid The customer ID
    @param sig The bank signature
    """
    def __init__(self, amount, uid):
        self.amount = amount
        self.uid = uid

    def addPair(left, right):
        id_pairs.append((left, right))
