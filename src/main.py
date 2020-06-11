from data import AuctionData
from auction_house import Auction, Auctioneer


# don't need as bid randomly generates auction id

# def input_auc_id(id=None):
#     """
#     input auction number
#     :param id:
#     :return:
#     """
#     if id is not None:
#         auc_id = int(id)
#     else:
#         pass
#
#     while type(auc_id) is not int:
#         input_id = input('Please enter auction id for bids: ')
#         print('Please enter integer value')
#         return input_auc_id()


# todo - fix so doesn't break on string input
# def input_bids(auctioneer, bid_no=None):
#     """
#     helper function to allow user input of x no of bids, this triggers generation of x new random bids for selected
#     auction id
#     """
#     if bid_no is not None:
#         bid_no = int(bid_no)
#
#     else:
#         pass
#     print(f'bid no is: {bid_no}')
#
#     while bid_no != 0:
#         bids = input("Enter number of bids: ")
#
#         if type(bid_no) != int:
#             print('Please enter integer value')
#             return input_bids(auctioneer, bids)
#         else:
#             # auction_id = input("Enter auction id: ")
#             # todo - process bids through auctioneer
#             auctioneer.accept_bid_input(bids)
#             pass
#         return input_bids(auctioneer, bids)
#
#     print('auctions ended...')
#     return auctioneer.auctioneer_status()


def input_bids(auctioneer):
    """
    helper function to allow user input of x no of bids, this triggers generation of x new random bids for selected
    auction id
    """

    bids = input("Enter number of bids: ")
    try:
        bids = int(bids)
        if bids == 0:
            print('auctions ended...')
            return auctioneer.auctioneer_status()
        else:
            # auction_id = input("Enter auction id: ")
            # todo - process bids through auctioneer
            auctioneer.accept_bid_input(bids)
            pass
            return input_bids(auctioneer)
    except ValueError:
        print('Please enter integer value')
        return input_bids(auctioneer)


def main() -> None:
    """
    Runs the main program.

    :return: None
    """

    data_handler = AuctionData()
    Gerald = Auctioneer(data=data_handler.data)
    Gerald.start()

    # check status of auctions
    # print([(v.highest_bid, k) for k, v in Gerald.auctions.items()])

    Gerald.auctioneer_status()

    input_bids(Gerald)

    # todo - add input with numeric validation to specify number of new bids

if __name__ == "__main__":
    main()
