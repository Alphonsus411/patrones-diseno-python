from dataclasses import dataclass


@dataclass
class GameState:
    level: int
    health: int
    weapon: str


class GameMemento:
    def __init__(self, game_state):
        self.game_state = game_state


class Game:
    def __init__(self):
        self.current_state = None

    def save_game(self):
        return GameMemento(self.current_state)

    def load_game(self, memento):
        self.current_state = memento.game_state


class GameSaveManager:
    def __init__(self):
        self.saves = []

    def save_game(self, game):
        self.saves.append(game.save_game())

    def load_game(self, game, save_slot):
        game.load_game(self.saves[save_slot])


game = Game()
save_manager = GameSaveManager()

game.current_state = GameState(3, 100, "BroadSword")
print(f"Player reached level: {game.current_state.level}")

save_manager.save_game(game)
print("Game saved.")

game.current_state = GameState(5, 80, "BroadSword")
print(f"Player reached level: {game.current_state.level}")

save_manager.load_game(game, 0)
print(f"Game loaded. Player is back at level: {game.current_state.level}")




