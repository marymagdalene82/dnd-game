from dndgame.character import Character


class Adventure:
    """Manage the player's adventure."""

    def __init__(self, player: Character) -> None:
        """Initialize an adventure.

        Args:
            player: The character controlled by the player.
        """
        self.player: Character = player
        self.current_scene: str = "start"

    def start(self) -> None:
        """Start the adventure."""
        print("Your adventure begins!")
        print("You find yourself standing at the entrance of a dark forest.")


    def enter_forest(self) -> None:
        """Move the player from the starting area into the forest."""
        self.current_scene = "forest"

        print("\nYou enter the dark forest.")
        print("The trees are tall and the path splits into two directions.")