import re

class Candy:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"{self.name} - Price: {self.price} coin - Amount: {self.quantity} шт.")

    def sell(self):
        if self.quantity > 0:
            self.quantity -= 1
            print(f"U spend {self.price} coins for {self.name} candy.")
            return True
        else:
            print(f"Are u blind? There is no {self.name} candy left.")
            return False


class Coin:
    def __init__(self, value, quantity):
        self.value = value
        self.quantity = quantity

    def total_value(self):
        return self.value * self.quantity


class VendingMachine:
    def __init__(self):
        self.candies = []
        self.coins = []
        self.all_coins = int

    def add_candy(self, candy):
        self.candies.append(candy)

    def add_coin(self, coin):
        self.coins.append(coin)

    def display_candies(self):
        for candy in self.candies:
            candy.display_info()

    def display_coins(self):
        for coin in self.coins:
            print(f"Coin_{coin.value} - In amount of: {coin.quantity} with total value {coin.value * coin.quantity}")






    def sell_candy(self, candy_name, payment):
        for candy in self.candies:
            if candy.name == candy_name:
                if candy.price <= payment:
                    if candy.sell():
                        self.process_payment(payment - candy.price)
                    return
                else:
                    print(f"Uahahaha, u spend every coin u have, now no {candy.name} candy.")
                    return
        print(f"Sems that all {candy_name} are gone, sad but true")

    def process_payment(self, amount):
        if self.all_coins >= amount:
            self.all_coins = amount
            print(f"Tnx, now u have {self.all_coins} coins")
        else:
            print("No money no funy")



    def count_all_coins(self):
        cac = 0
        for coin in self.coins:
            cac += coin.value * coin.quantity
        print(f'We have all of your {cac} coins')
        self.all_coins = cac




def get_number_counts(string):
    numbers = re.findall(r'\d+', string)
    numbers_count = {}

    for number in numbers:
        if number in numbers_count:
            numbers_count[number] += 1
        else:
            numbers_count[number] = 1

    return numbers_count

# Makin` candy load

cherry_candy = Candy("Cherry", 25, 100)
orange_candy = Candy("Orange", 50, 100)

vending_machine = VendingMachine()
vending_machine.add_candy(cherry_candy)
vending_machine.add_candy(orange_candy)

#taking everything from the customer
print("Trow all ur coins in stash by entering its values")
#Taking coins from bum
#input_string = input()
input_string = "25 25 25 50 50 25 30 40 50 1 3 5 4"
result = get_number_counts(input_string)
print(result)

try:
    coin_25 = Coin(25, result['25'])
except KeyError:
    coin_25 = Coin(25, 0)

try:
    coin_50 = Coin(50, result['50'])
except KeyError:
    coin_50 = Coin(50, 0)


#print(f'u inserted {coin_50.total_value() + coin_25.total_value()} coins')


vending_machine.add_coin(coin_50)
vending_machine.add_coin(coin_25)
vending_machine.display_candies()
vending_machine.display_coins()
vending_machine.count_all_coins()
lets_spend_all = vending_machine.all_coins
while vending_machine.all_coins > 0:
    try:
        user_input = int(input("Choose a candy (for cherry enter 1 for orange enter 2:"))
        if user_input == 1:
            vending_machine.sell_candy("Orange", vending_machine.all_coins)
        elif user_input == 2:
            vending_machine.sell_candy("Cherry", vending_machine.all_coins)
        else:
            print('At least its not a symbol, come one, u can do better ')
    except ValueError:
        print("Your ICQ is below melting point? give yourself another try")
        continue

vending_machine.display_candies()

