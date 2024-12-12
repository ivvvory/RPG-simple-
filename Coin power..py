import random  # Ensure that this is at the top

# Function to simulate a biased coin flip based on a given bias (returns "heads" or "tails")
def coin_roll_biased(bias):
    """
    This function simulates a biased coin flip. The coin has a given bias (probability of heads).
    A value of `bias` between 0 and 1 determines the probability of heads.

    Parameters:
    - bias (float): Probability of getting "heads" (0 <= bias <= 1).

    Returns:
    - "heads" or "tails" based on the bias.
    """
    random_number = random.random()  # Generates a random number between 0 and 1
    
    # If the random number is less than the bias, it's heads, otherwise tails
    if random_number < bias:
        return "heads"
    else:
        return "tails"

# Coin class that calculates the coin's power based on its level
class Coin:
    def __init__(self, level):
        """
        Initializes a Coin object with base and heads coin power based on its level.

        Parameters:
        - level (int): The level of the coin (1 to 10).
        """
        self.level = level
        self.base_coin_power = level  # Base coin power is equal to the coin's level (1-10)
        self.heads_coin_power = self.calculate_heads_coin_power(level)  # Heads power varies with level
        self.total_coin_power = self.base_coin_power + self.heads_coin_power  # Total coin power

    def calculate_heads_coin_power(self, level):
        """
        Calculates the heads coin power based on the coin's level.
        The heads power scales from 10 to 34 as level increases from 1 to 10.

        Parameters:
        - level (int): The level of the coin (1 to 10).

        Returns:
        - (int): The heads coin power based on the coin's level.
        """
        return 10 + (level - 1) * 2  # Linear scaling from 10 at level 1 to 34 at level 10

    def get_total_coin_power(self):
        """Returns the total coin power (base + heads)."""
        return self.total_coin_power

# Function to perform an attack based on the selected ability and coin level
def perform_attack(ability, coin_level):
    """
    Calculates the total attack power based on the ability and coin's level.

    Parameters:
    - ability (str): The selected attack ability ("strike", "slash", "rush") example attacks, change later
    - coin_level (int): The level of the coin (1 to 10).

    Returns:
    - (int): The total attack power calculated based on the number of heads.
    """
    # Create a Coin object based on the given level
    coin = Coin(coin_level)

    # Determine how many coins are needed for the selected attack ability
    if ability == "strike":
        coins_needed = 1
    elif ability == "slash":
        coins_needed = 2
    elif ability == "rush":
        coins_needed = 3
    else:
        return "Invalid ability"  # Return an error if the ability is invalid

    # Initialize the total attack power
    attack_power = 0

    # Simulate the coin flips for the attack
    for _ in range(coins_needed):
        flip_result = coin_roll_biased(0.60)  # 60% chance of heads for each flip
        
        # If the flip result is heads, add the coin's total power to the attack
        if flip_result == "heads":
            attack_power += coin.get_total_coin_power()

    return attack_power

# Main function to simulate the attack based on pre-determined coin level and user-selected attack ability
def simulate_attack():
    """
    Simulates an attack based on pre-determined coin level and user-selected attack ability.
    The function will prompt the user for the attack type and use a fixed coin level.
    """
    # Pre-determined coin level (can be changed before calling the function)
    coin_level = 5  # This is the level of the coin (from 1 to 10)

    # Ask the user to choose the attack ability
    print("Choose your attack ability: strike, slash, or rush")
    ability = input().lower()  # Take user input for ability, convert to lowercase

    # Perform the attack and calculate the power
    attack_power = perform_attack(ability, coin_level)

    # Print the result of the attack
    if attack_power == "Invalid ability":
        print("Invalid attack ability. Please choose either 'strike', 'slash', or 'rush'.")
    else:
        print(f"Attack with ability '{ability}' using coin of level {coin_level}: {attack_power}")

# If this script is executed directly, simulate an attack
if __name__ == "__main__":
    simulate_attack()

# If this script is executed directly, simulate an attack
#if __name__ == "__main__":
    #simulate_attack()


    #from coin_game import simulate_attack

# Simulate the attack
#simulate_attack()
