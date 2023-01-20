# TO DO

class Wallet:
    """This one probably should not be the core part.
        Might be treated as an extension and calculated based on actual transactions."""
    def __init__(self, address, amount=0):
        self.address = address
        self.amount = amount
