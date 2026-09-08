from dndgame.enemy import Enemy


def test_enemy_creation() -> None:
    """Test that an enemy is created with the correct attributes."""
    enemy = Enemy("Goblin", 5, 12)

    assert enemy.name == "Goblin"
    assert enemy.base_hp == 5
    assert enemy.armor_class == 12
    assert enemy.hp == 0
    assert enemy.max_hp == 0


def test_enemy_inherits_get_modifier() -> None:
    """Test that an enemy can calculate ability modifiers."""
    enemy = Enemy("Goblin", 5)

    enemy.stats = {
        "STR": 12,
        "DEX": 14,
        "CON": 10,
    }

    assert enemy.get_modifier("STR") == 1
    assert enemy.get_modifier("DEX") == 2
    assert enemy.get_modifier("CON") == 0
