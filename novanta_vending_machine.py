"""Novanta Vending Machine"""

from typing import Dict, List


class InsufficientFunds(Exception):
    """VendingMachine Insufficient Fund Exception"""


class VendingMachine:
    """Class to represent a Vending Machine"""

    def __init__(self) -> None:
        self._valid_coins: List[float] = [1, 0.5]
        self._products: Dict[str, float] = {
            "Coffee": 1.5,
            "Hot chocolate": 1,
            "Hot water": 0.5,
        }
        self._inserted_coins_amount: float = 0.0

    def buy_product(self, product: str) -> float:
        """Method to buy a product from the VendingMachine"""
        # Invalid product
        if product not in self._products:
            raise ValueError(f"'{product}' is not a valid product.")

        # Insufficient funds
        if self._inserted_coins_amount < self._products[product]:
            raise InsufficientFunds(
                f"Inserted coins value {self._inserted_coins_amount}$ is not enough to buy {product} which cost {self._products[product]}$"
            )

        coins_value_left: float = (
            self._inserted_coins_amount - self._products[product]
        )
        self._inserted_coins_amount = 0.0
        return coins_value_left

    def insert_coin(self, coin: float) -> None:
        """Method to insert coin in the VendingMachine"""
        if coin not in self._valid_coins:
            raise ValueError(f"{coin} is not a valid coin.")
        self._inserted_coins_amount += coin

    def return_change(self) -> List[float]:
        """Return the accumulated change as a list of coins"""
        coins_list: List[float] = []
        for coin in self._valid_coins:
            while self._inserted_coins_amount >= coin:
                coins_list.append(coin)
                self._inserted_coins_amount -= coin

        return coins_list


class DrinkMachine(VendingMachine):
    """Class that represents a DrinkMachine"""

    def __init__(self) -> None:
        super().__init__()
        self._valid_coins: List[float] = [1, 0.5, 0.2, 0.1, 0.05]
        self._products: Dict[str, float] = {"Coke": 1.2, "Water": 0.75}


class SnackMachine(VendingMachine):
    """Class that represents a DrinkMachine"""

    def __init__(self) -> None:
        super().__init__()
        self._valid_coins: List[float] = [1, 0.5, 0.2, 0.1]
        self._products: Dict[str, float] = {
            "M&Ms": 2.5,
            "Chips": 1.9,
            "Snickers": 1.3,
            "Pantera Rosa": 0.7,
        }


if __name__ == "__main__":
    vending_machine = VendingMachine()

    # Insert 2x1 and buy Coffee
    vending_machine.insert_coin(1)
    vending_machine.insert_coin(1)
    print(f"Returned coins value = {vending_machine.buy_product('Coffee')}")

    try:
        vending_machine.insert_coin(1.5)
    except ValueError as e:
        print(e)

    try:
        vending_machine.buy_product("Chocolate Bar")
    except ValueError as e:
        print(e)

    vending_machine.insert_coin(0.5)
    try:
        vending_machine.buy_product("Coffee")
    except InsufficientFunds as e:
        print(e)

    vending_machine.return_change()

    vending_machine.insert_coin(1)
    vending_machine.insert_coin(0.5)
    vending_machine.insert_coin(1)
    vending_machine.insert_coin(1)
    print(f"Returned change = {vending_machine.return_change()}")
    print(f"Returned change = {vending_machine.return_change()}")

    # Drink machine
    drink_machine = DrinkMachine()
    drink_machine.insert_coin(0.2)
    drink_machine.insert_coin(0.5)
    drink_machine.insert_coin(1)
    print(f"Returned coins value = {drink_machine.buy_product('Coke')}")

    try:
        drink_machine.insert_coin(0.01)
    except ValueError as e:
        print(e)

    # Snack machine
    snack_machine = SnackMachine()
    snack_machine.insert_coin(0.2)
    snack_machine.insert_coin(0.5)
    snack_machine.insert_coin(1)
    print(f"Returned coins value = {snack_machine.buy_product('Snickers')}")

    try:
        snack_machine.insert_coin(0.05)
    except ValueError as e:
        print(e)
