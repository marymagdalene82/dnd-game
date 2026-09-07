from dndgame.adventure import Adventure
from dndgame.character import Character
from unittest.mock import patch

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

def test_enter_forest() -> None:
    """Test that entering the forest changes the current scene."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", return_value="1"):
        adventure.enter_forest()

    assert adventure.current_scene == "left_path"

def test_enter_forest_left_path() -> None:
    """Test that choosing 1 enters the left path."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", return_value="1"):
        adventure.enter_forest()

    assert adventure.current_scene == "left_path"


def test_enter_forest_right_path() -> None:
    """Test that choosing 2 enters the right path."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", return_value="2"):
        adventure.enter_forest()

    assert adventure.current_scene == "right_path"

def test_enter_forest_rejects_invalid_choice() -> None:
    """Test that invalid choices are rejected."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", side_effect=["7", "1"]):
        adventure.enter_forest()

    assert adventure.current_scene == "left_path"


# git add dndgame/adventure.py tests/test_adventure.py
# git commit -m "feat: add interactive forest paths"