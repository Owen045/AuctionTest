from data import AuctionData
from auction_house import Auction, Auctioneer


def input_bids(auctioneer, bid_no=None):
    """helper function to allow user input of no of bids"""
    print(f'bid no is: {bid_no}')

    while bid_no != 0:
        bids = input("Enter number of bids: ")

        if type(bid_no) != int:
            print('Please enter integer value')

        return input_bids(auctioneer, bids)

    print('auctions ended...')
    return auctioneer.auctioneer_status()



def main() -> None:
    """
    Runs the main program.

    :return: None
    """

    data_handler = AuctionData()
    Gerald = Auctioneer(data=data_handler.data)
    Gerald.start()

    # check status of auctions
    print([(v.highest_bid, k) for k, v in Gerald.auctions.items()])

    for k, v in Gerald.auctions.items():
        print(f'Auction {k} winner is: {v.highest_bidder} with bid: {v.highest_bid}!')

    input_bids(Gerald)

    # todo - add input with numeric validation to specify number of new bids

if __name__ == "__main__":
    main()
