from dndgame.dice import roll

RACIAL_BONUSES: dict[str, dict[str, int]] = {
    "Human": {
        "STR": 1,
        "DEX": 1,
        "CON": 1,
        "INT": 1,
        "WIS": 1,
        "CHA": 1,
    },
    "Elf": {
        "DEX": 2,
    },
    "Dwarf": {
        "CON": 2,
    },
    "Halfling": {
        "DEX": 2,
    },
}
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
        """Apply the ability score bonuses associated with the character's race."""
        bonuses = RACIAL_BONUSES.get(self.race, {})

        for stat, bonus in bonuses.items():
            self.stats[stat] += bonus
