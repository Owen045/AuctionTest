from ..Logger import logger


class Auctioneer:
    """
    This class is responsible for the core methods which keep track of and determine who is winning the auction

    """
    def __init__(self, data):
        self.data = data # must be AuctionData object
        self.auctions = {}

    def process_bid(self):
        """Check bid against corresponding auction, log evaluation and trigger state change if necessary"""
