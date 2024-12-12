import random


class Coin:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def flip(self):
        """Simulate flipping a coin, returning a value within its range."""
        return random.randint(self.min_value, self.max_value)


class Card:
    def __init__(self, name, card_type, coins):
        self.name = name
        self.card_type = card_type  # 'attack' or 'defense'
        self.coins = coins  # List of Coin objects

    def play(self):
        """Flip all coins on the card and return their values."""
        return [coin.flip() for coin in self.coins]


class Combatant:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck  # List of Card objects
        self.hp = 100

    def choose_card(self):
        """Let the player select a card or auto-pick for AI."""
        if not self.deck:
            print(f"{self.name} has no cards left!")
            return None

        if self.name.lower() == "player":
            print("\nYour cards:")
            for i, card in enumerate(self.deck):
                print(f"{i + 1}: {card.name} ({card.card_type})")
            choice = int(input(f"Choose a card to play (1-{len(self.deck)}): ")) - 1
            return self.deck.pop(choice)
        else:
            return self.deck.pop(0)


def clash(coins1, coins2):
    """Simulate a clash between two players' coin rolls."""
    while coins1 and coins2:
        roll1 = sum(coins1)
        roll2 = sum(coins2)
        print(f"Clash rolls: Player: {roll1} vs Enemy: {roll2}")

        if roll1 > roll2:
            print("Player wins the clash round!")
            coins2.pop()  # Enemy loses one coin
        elif roll2 > roll1:
            print("Enemy wins the clash round!")
            coins1.pop()  # Player loses one coin
        else:
            print("It's a tie! No coins lost.")

        print(f"Remaining coins: Player: {len(coins1)}, Enemy: {len(coins2)}")

    # Determine the winner
    return "player" if coins2 == [] else "enemy"


def combat_round(combatant1, combatant2):
    """Simulate a single combat round with user-selected cards and clashing."""
    card1 = combatant1.choose_card()
    card2 = combatant2.choose_card()

    if not card1 or not card2:
        return

    print(f"\n{combatant1.name} plays {card1.name}")
    print(f"{combatant2.name} plays {card2.name}")

    coins1 = card1.play()
    coins2 = card2.play()

    print(f"Initial rolls: Player: {sum(coins1)} | Enemy: {sum(coins2)}")
    winner = clash(coins1, coins2)

    # Damage is calculated based on final remaining coins
    damage = abs(sum(coins1) - sum(coins2))
    if winner == "player":
        combatant2.hp -= damage
        print(f"Enemy loses {damage} HP!")
    else:
        combatant1.hp -= damage
        print(f"Player loses {damage} HP!")

    print(f"\nPlayer HP: {combatant1.hp}")
    print(f"Enemy HP: {combatant2.hp}")


# Example Usage
def main():
    # Define some example coins and cards
    coin1 = Coin(1, 6)
    coin2 = Coin(2, 5)
    coin3 = Coin(3, 8)

    card1 = Card("Slash", "attack", [coin1, coin2])
    card2 = Card("Shield Bash", "defense", [coin2, coin3])
    card3 = Card("Piercing Strike", "attack", [coin3, coin1])
    card4 = Card("Defensive Stance", "defense", [coin2])

    # Create combatants
    player = Combatant("Player", [card1, card2])
    enemy = Combatant("Enemy", [card3, card4])

    # Simulate combat rounds
    while player.hp > 0 and enemy.hp > 0:
        combat_round(player, enemy)
        if not player.deck and not enemy.deck:
            break

    # Determine the winner
    if player.hp > enemy.hp:
        print("\nPlayer wins!")
    elif enemy.hp > player.hp:
        print("\nEnemy wins!")
    else:
        print("\nIt's a draw!")


if __name__ == "__main__":
    main()