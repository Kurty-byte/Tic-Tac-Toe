import random

class Ai:
    def pick_choice(self, ava_choice: list[int]):
        return random.choice(ava_choice) if len(ava_choice) != 0 else None