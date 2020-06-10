

class Auction:
    """
    Class to store state of current highest bid
    """
    def __init__(self, auction_id):
        self.auction_id = auction_id
        self.highest_bid = 0
        self.highest_bidder = None
        self.bid_time = 0

    def set_highest(self, bid):
        """Set highest_bid attr to input bid vals"""

        if bid.ammount > self.highest_bid:
            self.highest_bid = bid.amount
            self.highest_bidder = bid.account_id
            self.bid_time = bid.time_unit
        else:
            pass


