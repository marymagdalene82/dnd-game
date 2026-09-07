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
        """Let the player choose a path through the forest."""
        self.current_scene = "forest"

        print("\nYou enter the dark forest.")
        print("The path splits into two directions.")
        print("1. Take the left path")
        print("2. Take the right path")

        while True:
            choice = input("Which path do you take? ")

            if choice == "1":
                self.current_scene = "left_path"
                print("\nYou take the left path.")
                break

            if choice == "2":
                self.current_scene = "right_path"
                print("\nYou take the right path.")
                break

            print("Invalid choice. Please choose 1 or 2.")

    def explore_left_path(self) -> None:
        """Explore the left path through the forest."""
        self.current_scene = "left_path"

        print("\nYou follow the left path deeper into the forest.")
        print("You discover an old wooden chest beneath a tree.")
        print("The chest contains a small healing potion.")

    def explore_right_path(self) -> None:
        """Explore the right path through the forest."""
        self.current_scene = "right_path"

        print("\nYou follow the right path through the forest.")
        print("You hear something moving in the bushes.")
        print("A goblin jumps out!")