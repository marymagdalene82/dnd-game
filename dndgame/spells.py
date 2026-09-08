# type: ignore
class Spell:
    """Represent a spell that can be used by a character.

    Attributes:
        name: The name of the spell.
        level: The spell level required to use the spell.
        school: The school of magic the spell belongs to.
        spell_power: The amount of power associated with the spell.
    """

    def __init__(self, name: str, level: int, school: str, spell_power: int):
        """Initialize a spell.

        Args:
            name: The name of the spell.
            level: The spell's required level.
            school: The school of magic the spell belongs to.
            spell_power: The spell's power value.
        """
        self.name = name
        self.level = level
        self.school = school
        self.spell_power = spell_power

    def cast(self, caster, target):
        pass


class SpellBook:
    """Store and manage spells available to a character.

    Attributes:
        spells: A list containing the spells in the spellbook.
    """

    def __init__(self) -> None:
        "Initialize a spellbook with an empty list of spells."
        self.spells: list[Spell] = []

    def add_spell(self, spell: Spell) -> None:
        """Add a spell to the spellbook.

        Args:
            spell: The spell to add.
        """
        self.spells.append(spell)

    def get_available_spells(self, spell_level: int) -> list[Spell]:
        """Return spells that can be used at the given spell level.

        Args:
            spell_level: The character's current spell level.

        Returns:
            A list of spells whose level is less than or equal to
            the supplied spell level.
        """
        return [spell for spell in self.spells if spell.level <= spell_level]
