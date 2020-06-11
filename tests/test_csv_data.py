import unittest
import os
import sys
import pandas as pd

sys.path.append("..")
from src.data import AuctionData
from src.auction_house import Auction, Auctioneer


class TestCSV(unittest.TestCase):

    def setUp(self):
        """
        Run pandas methods on csv to extract key data
        :return:
        """

        FILE_PATH = os.path.dirname(os.path.realpath('..')) + "/auction-test/src/data/data.csv"

        df = pd.read_csv(FILE_PATH)

        self.win_dict = {}
        win_zip = zip(list(df.groupby(['auction id'], sort=False)['amount'].max()),
                      list(df.groupby(['auction id'], sort=False)['amount'].max().index))

        for x in win_zip:
            # filter out negatives
            if x[0] > 0:
                self.win_dict[x[1]] = x[0]
            else:
                self.win_dict[x[1]] = 'invalid bid'


        print(self.win_dict)


    def test_correct_auc_no(self):
        """
        Test the correct number of auctions are instantiated and appended to auctioneer
        :return:
        """
        data_handler = AuctionData()
        self.ac = Auctioneer(data=data_handler.data, test=True)
        self.ac.start()

        self.assertEqual(len(self.ac.auctions), len(self.win_dict))

    def test_max_bids_correct(self):
        """
        Use pandas to sort csv bids into auctions and then find max bid amount
        """
        # test actual code

        data_handler = AuctionData()
        self.ac = Auctioneer(data=data_handler.data, test=True)
        self.ac.start()

        for auc, bid in self.win_dict.items():
            self.assertEqual(bid, self.ac.auctions[auc].highest_bid)

        # implement code to quick calc max values



if __name__ == '__main__':
    unittest.main()