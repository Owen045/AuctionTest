import unittest
import pandas as pd


class TestBids(unittest.TestCase):

    def setUp(self):
        """Run auction to populate csv values into auction states"""


    def test_new_bid_max(self):
        """
        Test that when new bid comes in to system with a higher bid, the auction state is reset to highest bid
        """


    def test_new_bid_miss(self):
        """
        Test that when new bid comes in which misses highest bid, auction state is not changed
        :return:
        """

    def test_new_auction_create(self):
        """
        Test whether if unrecognised numeric auction id is entered, a new auction will be
        appended to auctioneer.auctions
        :return:
        """

if __name__ == '__main__':
    unittest.main()