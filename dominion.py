import random
import time

# Set a seed for random based on time
random.seed(time.process_time())

# Basic card definitions
class Card:
    def __init__(self, name, cost, card_type):
        self.name = name
        self.cost = cost
        self.card_type = card_type

    def __repr__(self):
        return self.name

class TreasureCard(Card):
    def __init__(self, name, cost, value):
        super().__init__(name, cost, 'Treasure')
        self.value = value

class VictoryCard(Card):
    def __init__(self, name, cost, points):
        super().__init__(name, cost, 'Victory')
        self.points = points

class Player:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.discard_pile = []

    def draw_card(self):
        if not self.deck:
            self.deck, self.discard_pile = self.discard_pile, self.deck
            random.shuffle(self.deck)
        if self.deck:
            self.hand.append(self.deck.pop())

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

    def calculate_score(self):
        total_points = 0
        for card in self.deck + self.hand + self.discard_pile:
            if isinstance(card, VictoryCard):
                total_points += card.points
        return total_points

# Initialize cards
copper = TreasureCard("Copper", 0, 1)
silver = TreasureCard("Silver", 3, 2)
gold = TreasureCard("Gold", 6, 3)
estate = VictoryCard("Estate", 2, 1)
duchy = VictoryCard("Duchy", 5, 3)
province = VictoryCard("Province", 8, 6)

# Randomly choose number of players (2 to 4)
num_players = random.randint(2, 4)
players = [Player() for _ in range(num_players)]

# Randomly assign initial decks
for player in players:
    player.deck = random.sample([copper] * 7 + [silver] * 3 + [gold] * 2 + [estate] * 2 + [duchy] * 1, 10)
    random.shuffle(player.deck)
    for _ in range(5):
        player.draw_card()

# Game loop - very basic with a buying phase
for turn in range(1, 10):  # Example: 10 turns
    for player_num, player in enumerate(players, start=1):
        print(f"Player {player_num}'s turn: {turn}")
        print(f"Player {player_num}'s hand: {player.show_hand()}")

        # Random action: Player might draw an extra card
        if random.choice([True, False]):
            player.draw_card()
            print(f"Player {player_num} drew an extra card: {player.hand[-1]}")

        # Simulate a basic buying phase
        if random.choice([True, False]):
            purchased_card = random.choice([estate, duchy, province])
            player.discard_pile.append(purchased_card)
            print(f"Player {player_num} bought a {purchased_card}")

        # Cleanup and prepare for next turn
        player.discard_pile.extend(player.hand)
        player.hand = []
        for _ in range(5):
            player.draw_card()

# Determine the winner
scores = [player.calculate_score() for player in players]
for player_num, score in enumerate(scores, start=1):
    print(f"Player {player_num} Score: {score}")
winner = scores.index(max(scores)) + 1
print(f"Player {winner} wins!")