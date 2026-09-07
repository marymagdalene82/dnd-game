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

def test_explore_left_path() -> None:
    """Test that exploring the left path updates the scene."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    adventure.explore_left_path()

    assert adventure.current_scene == "left_path"


def test_explore_right_path() -> None:
    """Test that exploring the right path starts a goblin encounter."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", return_value="2"):
        result = adventure.explore_right_path()

    assert adventure.current_scene == "right_path"
    assert result is False
    assert adventure.current_scene == "right_path"

def test_encounter_goblin_player_runs_away() -> None:
    """Test that the player can run away from a goblin."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", return_value="2"):
        result = adventure.encounter_goblin()

    assert result is False

def test_play_left_path() -> None:
    """Test that playing the adventure can follow the left path."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", return_value="1"):
        adventure.play()

    assert adventure.current_scene == "left_path"


def test_play_right_path_and_run_away() -> None:
    """Test that playing the adventure can follow the right path."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", return_value="2"):
        adventure.play()

    assert adventure.current_scene == "right_path"

def test_encounter_goblin_rejects_invalid_choice() -> None:
    """Test that invalid combat choices are rejected."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    with patch("builtins.input", side_effect=["7", "2"]):
        result = adventure.encounter_goblin()

    assert result is False

def test_encounter_goblin_player_wins() -> None:
    """Test that the player can defeat the goblin."""
    player = Character("Hero", "Human", 10)
    adventure = Adventure(player)

    player.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
    }

    player.hp = player.max_hp = 10

    with patch("builtins.input", return_value="1"):
        with patch("dndgame.combat.roll", side_effect=[20, 6]):
            result = adventure.encounter_goblin()

    assert result is True