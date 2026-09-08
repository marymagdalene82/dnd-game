class Entity:
    """Represent a generic entity in the game."""

    def __init__(self, name: str, base_hp: int) -> None:
        """Initialize an entity.

        Args:
            name: The entity's name.
            base_hp: The entity's base hit points.
        """
        self.name: str = name
        self.stats: dict[str, int] = {}
        self.base_hp: int = base_hp
        self.hp: int = 0
        self.max_hp: int = 0
        self.armor_class: int = 10

    def get_modifier(self, stat: str) -> int:
        """Calculate the ability modifier for a given stat.

        Args:
            stat: The ability score whose modifier should be calculated.

        Returns:
            The ability modifier calculated from the stat score.
        """
        return (self.stats[stat] - 10) // 2

    def is_alive(self) -> bool:
        """Return whether the entity still has hit points.

        Returns:
            True if the entity has more than zero hit points.
        """
        return self.hp > 0
