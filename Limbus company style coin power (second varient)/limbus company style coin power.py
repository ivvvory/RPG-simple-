import random

class Coin:
    def __init__(self, base_power: int, flip_power: int):
        """
        Initialize a coin with base power and flip power.
        :param base_power: The power before flipping the coin.
        :param flip_power: Additional power if the coin flip succeeds.
        """
        self.base_power = base_power
        self.flip_power = flip_power

    def flip(self) -> int:
        """
        Simulate a coin flip.
        :return: The power value of the coin after the flip.
        """
        flip_result = random.choice([True, False])  # True for heads, False for tails
        return self.base_power + (self.flip_power if flip_result else 0)

class Skill:
    def __init__(self, coins: list[Coin]):
        """
        Initialize a skill with a list of coins.
        :param coins: List of Coin objects.
        """
        self.coins = coins

    def simulate_skill(self) -> int:
        """
        Simulate the coin flips for the skill and calculate total power.
        :return: Total power of the skill after all coin flips.
        """
        total_power = 0
        for coin in self.coins:
            coin_power = coin.flip()
            total_power += coin_power
        return total_power

# Example of how to use the system
if __name__ == "__main__":
    # Define some coins
    coin1 = Coin(base_power=3, flip_power=5)
    coin2 = Coin(base_power=2, flip_power=4)
    coin3 = Coin(base_power=1, flip_power=6)

    # Create a skill with these coins
    skill = Skill(coins=[coin1, coin2, coin3])

    # Simulate the skill
    total_power = skill.simulate_skill()
    print(f"Total Skill Power: {total_power}")