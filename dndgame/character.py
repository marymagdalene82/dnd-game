from dndgame.dice import roll


class Character:
    """Represent a playable D&D character.

    Attributes:
        name: The character's name.
        race: The character's race.
        stats: The character's ability scores.
        base_hp: The character's base hit points before modifiers.
        hp: The character's current hit points.
        max_hp: The character's maximum hit points.
        level: The character's current level.
        armor_class: The character's armor class.
    """
    def __init__(self, name: str, race: str, base_hp: int) -> None:
        """Initialize a character.

            Args:
                name: The character's name.
                race: The character's race.
                base_hp: The character's base hit points before modifiers.
        """
        self.name: str = name
        self.race: str = race
        self.stats: dict[str, int] = {}
        self.base_hp: int = base_hp
        self.hp: int = 0
        self.max_hp: int = 0
        self.level: int = 1
        self.armor_class: int = 10

    def get_modifier(self, stat: str) -> int:
        """Calculate the ability modifier for a given stat.

        Args:
            stat: The ability score whose modifier should be calculated.

        Returns:
            The ability modifier calculated from the stat score.
        """
        return (self.stats[stat] - 10) // 2

    def roll_stats(self) -> None:
        """Roll and assign all six ability scores.

        The character's maximum and current hit points are then
        calculated using the Constitution modifier.
        """
        print("Rolling stats...\n")
        stats: list[str] = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat in stats:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def apply_racial_bonuses(self) -> None:
        """Apply the ability score bonus associated with the character's race.

        Humans receive +1 to every ability score, elves receive +2 DEX,
        and dwarves receive +2 CON.
        """
        if self.race == "Dwarf":
            self.stats["CON"] += 2
        elif self.race == "Elf":
            self.stats["DEX"] += 2
        elif self.race == "Human":
            for stat in self.stats:
                self.stats[stat] += 1
