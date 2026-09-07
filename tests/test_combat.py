from unittest.mock import patch

from dndgame.character import Character
from dndgame.combat import Combat
from dndgame.enemy import Enemy


def create_character() -> Character:
    """Create a character with predictable stats for testing."""
    character = Character("Hero", "Human", 10)
    character.stats = {
        "STR": 12,
        "DEX": 14,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }
    character.hp = 10
    character.max_hp = 10
    return character


def create_enemy() -> Enemy:
    """Create an enemy with predictable stats for testing."""
    enemy = Enemy("Goblin", 5, 10)
    enemy.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
    }
    enemy.hp = 5
    enemy.max_hp = 5
    return enemy


def test_combat_creation() -> None:
    """Test that Combat stores its participants."""
    player = create_character()
    enemy = create_enemy()

    combat = Combat(player, enemy)

    assert combat.player is player
    assert combat.enemy is enemy
    assert combat.round == 0
    assert combat.initiative_order == []


def test_roll_initiative_player_goes_first() -> None:
    """Test initiative when the player rolls higher."""
    player = create_character()
    enemy = create_enemy()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[15, 5]):
        order = combat.roll_initiative()

    assert order == [player, enemy]


def test_roll_initiative_enemy_goes_first() -> None:
    """Test initiative when the enemy rolls higher."""
    player = create_character()
    enemy = create_enemy()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[5, 15]):
        order = combat.roll_initiative()

    assert order == [enemy, player]


def test_attack_hits() -> None:
    """Test that a successful attack deals damage."""
    player = create_character()
    enemy = create_enemy()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[15, 4]):
        damage = combat.attack(player, enemy)

    assert damage == 4
    assert enemy.hp == 1


def test_attack_misses() -> None:
    """Test that a missed attack deals no damage."""
    player = create_character()
    enemy = create_enemy()
    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", return_value=2):
        damage = combat.attack(player, enemy)

    assert damage == 0
    assert enemy.hp == 5

def test_attack_does_not_reduce_hp_below_zero() -> None:
    """Test that an attack cannot reduce HP below zero."""
    player = Character("Hero", "Human", 10)
    enemy = Enemy("Goblin", 5, 10)

    player.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
    }

    enemy.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
    }

    player.hp = player.max_hp = 10
    enemy.hp = 1
    enemy.max_hp = 5

    combat = Combat(player, enemy)

    with patch("dndgame.combat.roll", side_effect=[20, 6]):
        combat.attack(player, enemy)

    assert enemy.hp == 0