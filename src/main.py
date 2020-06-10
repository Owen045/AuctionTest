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

    print([v.highest_bid for k, v in Gerald.auctions.items()])

if __name__ == "__main__":
    main()
