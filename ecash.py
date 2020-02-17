class ecash:
    id_pairs = []

    """
    @param amount The value of the transaction
    @param uid The uniqueness string number
    @param cid The customer ID
    @param sig The bank signature
    """
    def __init__(self, amount, uid, cid, sig):
        self.amount = amount
        self.cid = cid
        self.sig = sig
