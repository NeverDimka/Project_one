from dataclasses import dataclass
from enum import Enum
from typing import List


class Flavor(Enum):
    cherry = "cherry"
    orange = "orange"


@dataclass
class Coin:
    value: int


@dataclass
class Candy:
    flavor: Flavor


class VendingMachine:
    _storage: List[Candy] = []

    def __init__(self) -> None:
        pass

    def insert_coin(self, coin: Coin) -> None:
        pass

    def choose_candy(self, candy_flavor: Flavor) -> None:
        pass



'''
if __name__ == "__main__":
    coins_in_hand: List[Coin] = []  # TODO add and convert input list of ints into List[Coin]

    machine = VendingMachine()  # init machine with X amount of candies

    machine.insert_coin(*coins_in_hand)  # insert all available coins, consider that machine doesn't give change
    machine.choose_candy(Flavor.cherry)  # try to get cherry candy
    machine.choose_candy(Flavor.orange)  # try to get orange candy

    # TODO
    # machine should process coins in storage
    # machine should raise an error if no candies left or not enough coins inserted
    # machine should be configured to match specific candy with it's cost

'''