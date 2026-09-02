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