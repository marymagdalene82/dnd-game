class Adventure:
    """Manage the player's adventure."""

    def __init__(self) -> None:
        """Initialize an adventure."""
        self.current_scene: str = "start"

    def start(self) -> None:
        """Start the adventure."""
        print("Your adventure begins!")
        print("You find yourself standing at the entrance of a dark forest.")