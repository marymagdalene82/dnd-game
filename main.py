from dndgame.character import Character
from dndgame.dice import roll
from dndgame.combat import Combat
from dndgame.enemy import Enemy

def create_character():
    """Create a character from user input."""
    print("Welcome to D&D Adventure!")
    name = input("Enter your character's name: ")

    print("\nChoose your race:")
    print("1. Human (+1 to all stats)")
    print("2. Elf (+2 DEX)")
    print("3. Dwarf (+2 CON)")
    race_choices: dict[str, str] = {
        "1": "Human",
        "2": "Elf",
        "3": "Dwarf",
        "4": "Halfling",
    }
    while True:
        race_choice = input("Enter choice (1-4): ")

        if race_choice in race_choices:
            race = race_choices[race_choice]
            break

        print("Invalid choice. Please enter a number from 1 to 4.")

    character = Character(name, race, 10)
    character.roll_stats()
    character.apply_racial_bonuses()
    return character


def display_character(character):
    print(f"\n{character.name} the {character.race}")
    print("\nStats:")
    for stat, value in character.stats.items():
        modifier = character.get_modifier(stat)
        print(f"{stat}: {value} ({'+' if modifier >= 0 else ''}{modifier})")
    print(f"\nHP: {character.hp}")


def combat_with_goblin(player: Character) -> bool:
    """Run a combat encounter between the player and a goblin.

    Args:
        player: The character controlled by the player.

    Returns:
        True if the player defeats the goblin, otherwise False.
    """
    print("\nA goblin appears!")

    goblin = Enemy("Goblin", 5, 10)
    goblin.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
    }
    goblin.hp = goblin.base_hp
    goblin.max_hp = goblin.base_hp

    combat = Combat(player, goblin)
    combat.roll_initiative()

    while player.is_alive() and goblin.is_alive():
        print(f"\n{goblin.name} HP: {goblin.hp}")
        print(f"{player.name} HP: {player.hp}")

        print("\nYour turn!")
        print("1. Attack")
        print("2. Run away")
        print()

        choice = input("What do you do? ")

        if choice == "1":
            damage = combat.attack(player, goblin)

            if damage > 0:
                print(f"You hit for {damage} damage!")
            else:
                print("You missed!")

            if not goblin.is_alive():
                break

            print("\nThe goblin attacks!")

            damage = combat.attack(goblin, player)

            if damage > 0:
                print(f"The goblin hits you for {damage} damage!")
            else:
                print("The goblin missed!")

        elif choice == "2":
            return False

        else:
            print("Invalid choice.")

    return player.is_alive()


def main():
    player = create_character()

    while True:
        print("\nWhat would you like to do?")
        print("1. Fight a goblin")
        print("2. View character")
        print("3. Quit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            victory = combat_with_goblin(player)
            if victory:
                print("You defeated the goblin!")
            else:
                print("You ran away!")
        elif choice == "2":
            display_character(player)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
