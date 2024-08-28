"""Novanta Vending Machine"""

from typing import Dict, Set


class InsufficientFunds(Exception):
    """VendingMachine Insufficient Fund Exception"""


class VendingMachine:
    """Class to represent a Vending Machine"""

    def __init__(self) -> None:
        self.__valid_coins: Set[float] = {1, 0.5}
        self.__products: Dict[str, float] = {
            "Coffee": 1.5,
            "Hot chocolate": 1,
            "Hot water": 0.5,
        }
        self.__inserted_coins_amount: float = 0.0

    def buy_product(self, product: str) -> float:
        """Method to buy a product from the VendingMachine"""
        # Invalid product
        if product not in self.__products:
            raise ValueError(f"'{product}' is not a valid product.")

        # Insufficient funds
        if self.__inserted_coins_amount < self.__products[product]:
            raise InsufficientFunds(
                f"Inserted coins value {self.__inserted_coins_amount}$ is not enough to buy {product} which cost {self.__products[product]}$"
            )

        coins_value_left: float = (
            self.__inserted_coins_amount - self.__products[product]
        )
        self.__inserted_coins_amount = 0.0
        return coins_value_left

    def insert_coin(self, coin: float) -> None:
        """Method to insert coin in the VendingMachine"""
        if coin not in self.__valid_coins:
            raise ValueError(f"{coin} is not a valid coin.")
        self.__inserted_coins_amount += coin


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.insert_coin(1)
    vending_machine.insert_coin(1)
    
    print(f"Returned coins value = {vending_machine.buy_product("Coffee")}")

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
