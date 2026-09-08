from dndgame.character import Character
from unittest.mock import patch

def test_halfling_racial_bonus() -> None:
    """Test that a Halfling receives +2 DEX."""
    character = Character("Bilbo", "Halfling", 10)

    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert character.stats["DEX"] == 12


def test_entity_is_alive() -> None:
    """Test that an entity is alive when it has HP above zero."""
    character = Character("Hero", "Human", 10)

    character.hp = 5

    assert character.is_alive() is True


def test_entity_is_not_alive() -> None:
    """Test that an entity is not alive at zero HP."""
    character = Character("Hero", "Human", 10)

    character.hp = 0


def test_apply_racial_bonuses_for_elf() -> None:
    """Test that an Elf receives the correct racial bonus."""
    character = Character("Legolas", "Elf", 10)

    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert character.stats["DEX"] == 12


def test_apply_racial_bonuses_for_dwarf() -> None:
    """Test that a Dwarf receives the correct racial bonus."""
    character = Character("Dwarf", "Dwarf", 10)

    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert character.stats["CON"] == 12


def test_apply_racial_bonuses_for_halfling() -> None:
    """Test that a Halfling receives the correct racial bonus."""
    character = Character("Halfling", "Halfling", 10)

    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert character.stats["DEX"] == 12

def test_roll_stats() -> None:
    character = Character("Hero", "Human", 10)

    with patch("dndgame.character.roll", side_effect=[10, 11, 12, 13, 14, 15]):
        character.roll_stats()

    assert character.stats == {
        "STR": 10,
        "DEX": 11,
        "CON": 12,
        "INT": 13,
        "WIS": 14,
        "CHA": 15,
    }
    assert character.max_hp == 11
    assert character.hp == 11
