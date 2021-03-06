import collections

import sys
sys.path.append("..")
from src.Logger import Logger
from src.data.bid import Bid


class Auction:
    """
    Class to store state of current highest bid
    """
    def __init__(self, auction_id, test=False):
        self.auction_id = auction_id
        self.highest_bid = 0
        self.highest_bidder = None
        self.bid_time = 0
        self.no_bids = 0
        self.test = test  # suppress logging in tests
        self.log = Logger(id=auction_id, test=self.test)
        self.log.init_logfile()

    def set_invalid(self):
        """
        If after each bid, highest bid is still 0, set as 'invalid bid'
        :return:
        """
        if self.highest_bid == 0:
            self.highest_bid = 'invalid bid'
        else:
            pass

    def set_highest(self, bid):
        """Set highest_bid attr to input bid vals"""

        if self.check_val_pos(bid) is True:
            if bid.amount > self.highest_bid:
                self.highest_bid = bid.amount
                self.highest_bidder = bid.account_id
                self.bid_time = bid.time_unit
                print(f'New highest bid in auction {bid.auction_id}: {self.highest_bid}, bidder: {bid.account_id}')
                self.log.add_log_row(message=f'New highest bid: {self.highest_bid}, bidder: {bid.account_id}')
            else:
                self.log.add_log_row(message=f'Bid missed: {bid.amount}, bidder: {bid.account_id}')
                pass
        else:

            pass

        self.set_invalid()

    def check_val_pos(self, bid):
        """
        Check if bid.amount is positive and log as error if it is
        :return:
        """
        if bid.amount <= 0:
            self.log.add_log_row(message=f'invalid bid amount: {bid.amount} is negative,'
                                         f'bidder: {bid.account_id}', log_level='error')
            self.no_bids += 1
            return False
        else:
            return True


class Auctioneer:
    """
    This class is responsible for the core methods which keep track of and determine who is winning the auction

    """
    def __init__(self, data, test=False):
        self.data = data # must be AuctionData object
        self.auctions = {}
        self.test = test # suppress logging for tests

    def process_bid(self, bid):
        """
        Check bid against corresponding auction, log evaluation and trigger state change if necessary
        """

        try:
            auction = self.auctions[bid.auction_id]
        except KeyError:
            auction = Auction(bid.auction_id, test=self.test)

        auction.set_highest(bid)

        self.auctions[auction.auction_id] = auction

    def start(self):
        """
        Begin iteration through data
        :return:
        """

        for bid in self.data:
            self.process_bid(bid)

    def accept_bid_input(self, no_bids):
        """
        Accept int of number of new bids coming in and generate new bids
        Triggers random bid generation in Bid class which appends to auction
        :return:
        """

        for i in range(no_bids):
            bid = Bid.generate()
            print(f'auction: {bid.auction_id}, bidder: {bid.account_id}, amount: {bid.amount}, time:{bid.time_unit}')
            self.process_bid(bid)



    def auctioneer_status(self):
        """
        Auctioneer prints current status and winner of all auctions
        :return:
        """

        ordered = collections.OrderedDict(sorted(self.auctions.items()))

        for k, v in ordered.items():
            print(f'Auction {k} winner is: {v.highest_bidder} with bid: {v.highest_bid}!')