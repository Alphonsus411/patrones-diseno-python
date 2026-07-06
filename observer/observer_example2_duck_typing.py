

class Bidder:
    def __init__(self, name):
        self._name = name

    def update(self, auction_item):
        print(
            f"{self._name} notified. "
            f"New highest bid on {auction_item.name} is {auction_item.price}"
        )

    def __str__(self):
        return self._name


class AuctionItem:
    def __init__(self, name, starting_price):
        self._name = name
        self.price = starting_price
        self._bidders = []
        self._highest_bidder = None

    @property
    def name(self):
        return self._name

    def register_bidder(self, bidder):
        if bidder not in self._bidders:
            self._bidders.append(bidder)

    def remove_bidder(self, bidder):
        if bidder in self._bidders:
            self._bidders.remove(bidder)

    def notify_bidders(self):
        for bidder in self._bidders:
            bidder.update(self)

    def new_bid(self, price, bidder):
        if price > self.price:
            self.price = price
            self._highest_bidder = bidder
            print(f"{bidder} placed a new bid: {price}")
            self.notify_bidders()
        else:
            print(f"Bid rejected. {price} is not higher than current price {self.price}")


john = Bidder("John")
jane = Bidder("Jane")

item1 = AuctionItem("Vintage Clock", 10)

item1.register_bidder(john)
item1.register_bidder(jane)

item1.notify_bidders()

item1.new_bid(20, john)
item1.new_bid(30, jane)
item1.new_bid(25, john)