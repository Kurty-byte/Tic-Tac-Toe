import random

class Ai:
    """This is the opponent of the player represented as object
    """
    def pick_choice(self, ava_choice: list[int]) -> int:
        """a method that chooses a random slot on the table

        Args:
            ava_choice (list[int]): a list of slot identities that is not occupied yet

        Returns:
            int: a random integer representing a slot identity
        """
        return random.choice(ava_choice) if len(ava_choice) != 0 else None