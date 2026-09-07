from dndgame.dice import roll
from dndgame.entity import Entity


class Combat:
    """Manage combat between two entities."""

    def __init__(self, player: Entity, enemy: Entity) -> None:
        """Initialize combat.

        Args:
            player: The player entity participating in combat.
            enemy: The enemy entity participating in combat.
        """
        self.player: Entity = player
        self.enemy: Entity = enemy
        self.round: int = 0
        self.initiative_order: list[Entity] = []

    def roll_initiative(self) -> list[Entity]:
        """Determine the order in which combatants take their turns.

        Returns:
            A list containing the player and enemy in initiative order.
        """
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker: Entity, defender: Entity) -> int:
        """Perform an attack against another entity.

        Args:
            attacker: The entity making the attack.
            defender: The entity being attacked.

        Returns:
            The amount of damage dealt. Returns 0 if the attack misses.
        """
        attack_roll = roll(20, 1) + attacker.get_modifier("STR")
        weapon_max_damage = 6

        if attack_roll >= defender.armor_class:
            damage = roll(weapon_max_damage, 1)
            defender.hp = max(0, defender.hp - damage)
            return damage

        return 0