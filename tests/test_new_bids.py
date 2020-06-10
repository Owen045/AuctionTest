import unittest


class TestBids(unittest.TestCase):

    def setUp(self):
        """Run auction to populate csv values into auction states"""


    def test_new_bid_max(self):
        """
        Test that when new bid comes in to system with a higher bid, the auction state is reset to highest bid
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_new_bid_miss(self):
        """
        Test that when new bid comes in which misses highest bid, auction state is not changed
        :return:
        """


if __name__ == '__main__':
    unittest.main()