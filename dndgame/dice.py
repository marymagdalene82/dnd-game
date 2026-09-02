import random


def roll(dice_type: int, number_of_dice: int) -> int:
    """Roll one or more dice and return their total.

    Args:
        dice_type: The number of sides on each die.
        number_of_dice: The number of dice to roll.

    Returns:
        The sum of all dice rolls.
    """
    rolls = []
    total = 0
    for _ in range(number_of_dice):
        roll_result = random.randint(1, dice_type)
        rolls.append(roll_result)
        total += roll_result
    print(f"Rolling {number_of_dice}d{dice_type}: {rolls} = {total}")
    return total


def roll_with_advantage(dice_type: int) -> int:
    """Roll a die twice and return the higher result.

    Args:
        dice_type: The number of sides on the die.

    Returns:
        The higher of the two dice rolls.
    """
    roll1 = roll(dice_type, 1)
    roll2 = roll(dice_type, 1)
    return max(roll1, roll2)


def roll_with_disadvantage(dice_type: int) -> int:
    """Roll a die twice and return the lower result.

    Args:
        dice_type: The number of sides on the die.

    Returns:
        The lower of the two dice rolls.
    """
    roll1 = roll(dice_type, 1)
    roll2 = roll(dice_type, 1)
    return min(roll1, roll2)
