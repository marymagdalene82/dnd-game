from dndgame.adventure import Adventure
from dndgame.character import Character


def test_adventure_creation() -> None:
    """Test that an adventure stores the player."""
    player = Character("Hero", "Human", 10)

    adventure = Adventure(player)

    assert adventure.player is player
    assert adventure.current_scene == "start"


def test_adventure_start(capsys) -> None:
    """Test that starting the adventure prints the introduction."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    adventure.start()

    captured = capsys.readouterr()

    assert "Your adventure begins!" in captured.out
    assert "dark forest" in captured.out