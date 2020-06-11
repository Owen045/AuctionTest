from data import AuctionData
from auction_house import Auction, Auctioneer


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



    # todo - add input with numeric validation to specify number of new bids

if __name__ == "__main__":
    main()
