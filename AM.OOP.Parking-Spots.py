# AM OOP Design
# Playing Card
# https://algo.monster/problems/oop_parking_spots
from enum import Enum
from typing import Dict, List, Optional


class CarSize(Enum):
    """Enum class representing the car sizes"""

    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Car:
    """Class representing a Car"""

    CAR_SIZES: Dict[str, CarSize] = {
        "Small": CarSize.SMALL,
        "Medium": CarSize.MEDIUM,
        "Large": CarSize.LARGE,
    }
    CAR_SIZES_NAMES: Dict[CarSize, str] = {e: s for s, e in CAR_SIZES.items()}

    def __init__(self, size: str, color: str, brand: str) -> None:
        self.__size: CarSize = self.CAR_SIZES[size]
        self.__color: str = color
        self.__brand: str = brand

    def __str__(self) -> str:
        return f"{self.CAR_SIZES_NAMES[self.__size]} {self.__color} {self.__brand}"


class ParkingSpot:
    """Class representing a Parking Spot inside a Parking Lot"""

    def __init__(self, parked_car: Optional[Car] = None) -> None:
        self.__parked_car: Optional[Car] = parked_car

    @property
    def is_free(self) -> bool:
        """Property to check if the ParkingSpot is free"""
        return self.__parked_car is None

    def __str__(self) -> str:
        if self.__parked_car is None:
            return "Empty"
        else:
            return str(self.__parked_car)

    def park(self, car: Car) -> None:
        """Method to park a Car in the Parking Spot"""
        self.__parked_car = car

    def leave(self) -> None:
        """Method to remove the car from the Parking Spot"""
        self.__parked_car = None


class ParkingLot:
    """Class representing a Parking Lot"""

    def __init__(self, nb_spots: int) -> None:
        """Init method

        Args:
            n: the number of ParkingSpot inside the ParkingLot
        """
        self.__spots_list: List[ParkingSpot] = [
            ParkingSpot() for _ in range(nb_spots)
        ]
        self.__nb_free_spots: int = nb_spots

    @property
    def nb_free_spots(self) -> int:
        """Return the number of free ParkingSpot in the ParkingLot"""
        return self.__nb_free_spots

    def __len__(self) -> int:
        return len(self.__spots_list)

    def __getitem__(self, key) -> None:
        return self.__spots_list[key]

    def debug_msg(self) -> str:
        """Return a debug message for the ParkingLot"""
        msg = f"ParkingLot has {self.nb_free_spots} free spots out of {len(self)}"
        for i, spot in enumerate(self.__spots_list):
            msg += f"\nSpot {i}: {spot}"
        return msg

    def park(self, spot_index: int, car: Car) -> None:
        """Method to attempt to park a car at the given spot

        If the given spot is unavailable (because a car cannot park there, or there is already a car),
        the car will try to park in the next available spot in order until it finds an available slot,
        or there are no more slots left (in which case the car leaves the parking lot)

        Args:
            sport_index: the index of the spot to park the car in
            car: the car to park
        """
        # print(f"Parking {car} at spot {spot_index}")
        for i in range(len(self)):
            parking_spot: ParkingSpot = self.__spots_list[
                (spot_index + i) % len(self)
            ]
            if parking_spot.is_free:
                # print(f"ParkingSpot {i} is free")
                parking_spot.park(car)
                self.__nb_free_spots -= 1
                break

    def remove(self, spot_index: int) -> None:
        """Remove the car parked at that spot. Do nothing if there is no car there."""
        if not self.__spots_list[spot_index].is_free:
            self.__nb_free_spots -= 1

        self.__spots_list[spot_index].leave()


def parking_system(n: int, instructions: List[List[str]]) -> List[str]:
    """Entry point function for the parking system"""
    parking_lot = ParkingLot(nb_spots=n)
    output: List[str] = []
    for instruction in instructions:
        # print(parking_lot.degug_msg())
        if instruction[0] == "park":
            parking_spot_index: int = int(instruction[1])
            car_size: str = instruction[2]
            car_color: str = instruction[3]
            car_brand: str = instruction[4]
            car = Car(size=car_size, color=car_color, brand=car_brand)
            parking_lot.park(spot_index=parking_spot_index, car=car)
        elif instruction[0] == "remove":
            parking_spot_index: int = int(instruction[1])
            parking_lot.remove(spot_index=parking_spot_index)
        elif instruction[0] == "print":
            parking_spot_index: int = int(instruction[1])
            # print(f"Printing content of ParkingSpot {parking_spot_index}")
            output.append(str(parking_lot[parking_spot_index]))
        elif instruction[0] == "print_free_spots":
            # print("Printing number of free spots")
            output.append(f"{parking_lot.nb_free_spots}")
        else:
            raise ValueError(f"{instruction[0]} is not supported.")
    return output


if __name__ == "__main__":
    n = int(input())
    instructions = [input().split() for _ in range(int(input()))]
    res = parking_system(n, instructions)
    for line in res:
        print(line)
