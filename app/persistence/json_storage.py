import json
import os

class JSONStorage:
    def __init__(self, filename="game_state.json"):
        self.filename = filename

    def save_game(self, game_data):
        try:
            with open(self.filename, "w") as f:
                json.dump(game_data, f, indent=4)
        except Exception as e:
            print(f"Error saving game: {e}")

    def load_game(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error: Save file is corrupted.")
            return {}
        except Exception as e:
            print(f"Error loading game: {e}")
            return {}
