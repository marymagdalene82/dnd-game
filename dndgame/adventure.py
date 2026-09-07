from dndgame.character import Character
from dndgame.combat import Combat
from dndgame.enemy import Enemy

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

    def explore_right_path(self) -> bool:
        """Explore the right path through the forest."""
        self.current_scene = "right_path"

        print("\nYou follow the right path through the forest.")
        print("You hear something moving in the bushes.")
        print("A goblin jumps out!")
        return self.encounter_goblin()
    def encounter_goblin(self) -> bool:
        """Start a combat encounter with a goblin.

        Returns:
            True if the player survives the encounter, otherwise False.
        """
        print("\nA goblin attacks!")

        goblin = Enemy("Goblin", 5, 10)
        goblin.stats = {
            "STR": 10,
            "DEX": 10,
            "CON": 10,
        }
        goblin.hp = goblin.base_hp
        goblin.max_hp = goblin.base_hp

        combat = Combat(self.player, goblin)

        while self.player.is_alive() and goblin.is_alive():
            print(f"\n{self.player.name} HP: {self.player.hp}")
            print(f"{goblin.name} HP: {goblin.hp}")

            print("\n1. Attack")
            print("2. Run away")

            choice = input("What do you do? ")

            if choice == "1":
                damage = combat.attack(self.player, goblin)

                if damage > 0:
                    print(f"You hit for {damage} damage!")
                else:
                    print("You missed!")

                if not goblin.is_alive():
                    break

                print("\nThe goblin attacks!")

                damage = combat.attack(goblin, self.player)

                if damage > 0:
                    print(f"The goblin hits you for {damage} damage!")
                else:
                    print("The goblin missed!")

            elif choice == "2":
                print("You run away!")
                return False

            else:
                print("Invalid choice.")

        return self.player.is_alive()

    def play(self) -> None:
        """Run the main adventure."""
        self.start()
        self.enter_forest()

        if self.current_scene == "left_path":
            self.explore_left_path()
            print("\nYour adventure continues...")
        elif self.current_scene == "right_path":
            survived = self.explore_right_path()

            if survived:
                print("\nYou survived the goblin encounter!")
                print("Your adventure continues...")
            else:
                print("\nThe adventure ends here.")