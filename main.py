from dndgame.character import Character
from dndgame.adventure import Adventure

def create_character():
    """Create a character from user input."""
    print("Welcome to D&D Adventure!")
    while True:
        name = input("Enter your character's name: ").strip()

        if name:
            break

        print("Name cannot be empty.")

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

def main() -> None:
    """Run the D&D game."""
    player = create_character()

    adventure = Adventure(player)
    adventure.play()


if __name__ == "__main__":
    main()