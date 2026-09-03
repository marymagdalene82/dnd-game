from dndgame.character import Character


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

    assert character.is_alive() is False