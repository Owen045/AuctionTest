

class Auction:
    """
    Class to store state of current highest bid
    """
    def __init__(self, auction_id):
        self.auction_id = auction_id
        self.highest_bid = {}

    def set_highest(self, bid):
        """Set highest_bid attr to input bid vals"""


