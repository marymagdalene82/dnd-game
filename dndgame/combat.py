from dndgame.dice import roll
from dndgame.character import Character

class Combat:
    def __init__(self, player: Character, enemy: Character) -> None:
        """Initialize a combat encounter.

            Args:
                player: The character controlled by the player.
                enemy: The character the player will fight.
        """
        self.player = player
        self.enemy = enemy
        self.round = 0
        self.initiative_order: list[Character] = []

    def roll_initiative(self) -> list[Character]:
        """Determine the combat order using each character's DEX modifier.

            Returns:
                The characters arranged from first to last in the initiative order.
        """
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker: Character, defender: Character) -> int:
        """Perform an attack against a defending character.

            Args:
                attacker: The character making the attack.
                defender: The character being attacked.

            Returns:
                The damage dealt, or 0 if the attack misses.
        """
        attack_roll = roll(20, 1) + attacker.get_modifier("STR")
        weapon_max_damage = 6
        if attack_roll >= defender.armor_class:
            damage = roll(weapon_max_damage, 1)
            defender.hp -= damage
            return damage
        return 0
