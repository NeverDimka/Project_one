class Coin:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Candy:
    def __int__(self, flavor):
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor


class Vending_mashine:
    def __int__(self, name):
        self.name = name

    def get_candy(self, candy: Candy):
        pass

    def insert_coin(self, value: Coin):
        pass
