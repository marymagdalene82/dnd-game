from dndgame.entity import Entity


class Enemy(Entity):
    """Represent an enemy that can participate in combat."""

    def __init__(
        self,
        name: str,
        base_hp: int,
        armor_class: int = 10,
    ) -> None:
        """Initialize an enemy.

        Args:
            name: The enemy's name.
            base_hp: The enemy's base hit points.
            armor_class: The enemy's armor class.
        """
        super().__init__(name, base_hp)
        self.armor_class = armor_class