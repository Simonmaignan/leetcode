"""
Houses and water tank
"""

from typing import List, Set


def solution(S: str) -> int:
    n = len(S)
    houses_pos: List[int] = [i for i, s in enumerate(S) if s == "H"]

    def is_valid(water_tanks_pos: Set[int]) -> bool:
        """Check if water tanks positions set is valid"""
        # Check if each house has an adjacent water tank
        for house_i in houses_pos:
            if (house_i - 1) not in water_tanks_pos and (
                house_i + 1
            ) not in water_tanks_pos:
                # print(f"houses pos = {houses_pos}")
                # print(f"{water_tanks_pos} invalid")
                return False
        return True

    def dfs(cur_i: int, water_tanks_pos: Set[int]) -> int:
        # print(f"i={cur_i}; wtp={water_tanks_pos}")
        # Skipping houses
        while cur_i < n and S[cur_i] == "H":
            cur_i += 1

        # We're at the end of the street
        if cur_i >= n:
            # Let's check that each house has an adjacent water tank
            if is_valid(water_tanks_pos):
                return len(water_tanks_pos)
            return -1

        # That's the max water tank we could have since N in [1..20]
        min_water_tanks = 21
        # Adding a water tank at this position and going to next position
        water_tanks_pos.add(cur_i)
        nb_water_tanks_with = dfs(cur_i + 1, water_tanks_pos)
        water_tanks_pos.remove(cur_i)
        if nb_water_tanks_with >= 0:
            min_water_tanks = min(min_water_tanks, nb_water_tanks_with)

        # Skipping adding a water tank at this position and going to next position
        nb_water_tanks_without = dfs(cur_i + 1, water_tanks_pos)
        if nb_water_tanks_without >= 0:
            min_water_tanks = min(min_water_tanks, nb_water_tanks_without)

        return min_water_tanks if min_water_tanks < 21 else -1

    return dfs(0, set())


if __name__ == "__main__":
    print("-H-HH--")
    print(solution("-H-HH--"))
    print("\n-H-H-H-H-H")
    print(solution("-H-H-H-H-H"))
    print("\nH")
    print(solution("H"))
    print("\n--------")
    print(solution("--------"))
    print("\nHHHHHHHHHHHHH")
    print(solution("HHHHHHHHHHHHH"))
    print("\n-----HHH")
    print(solution("-----HHH"))
