from ..Logger import logger
from ..auction_house.auction import Auction


class Auctioneer:
    """
    This class is responsible for the core methods which keep track of and determine who is winning the auction

    """
    def __init__(self, data):
        self.data = data # must be AuctionData object
        self.auctions = {}

    def process_bid(self):
        """Check bid against corresponding auction, log evaluation and trigger state change if necessary"""
        for bid in self.data:
            try:
                auction = self.auctions[bid.auction_id]
            except KeyError:
                auction = Auction(bid.auction_id)

            auction.set_highest(bid)

            self.auctions[auction.auction_id] = auction
