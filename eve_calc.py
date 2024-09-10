from math import tanh

from CharacterClass import CharacterClass


def _calculate_performance(character_class, attack, defense):
    if character_class == CharacterClass.WARRIOR:
        performance = 0.6 * attack + 0.4 * defense
    elif character_class == CharacterClass.ARCHER:
        performance = 0.9 * attack + 0.1 * defense
    elif character_class == CharacterClass.GUARDIAN:
        performance = 0.1 * attack + 0.9 * defense
    elif character_class == CharacterClass.MAGE:
        performance = 0.8 * attack + 0.3 * defense
    else:
        raise ValueError("Invalid character class")

    return performance


def _calculate_modifiers(height):
    if height < 1.3 or height > 2.0:
        raise ValueError("Height must be between 1.3m and 2.0m")

    h = height
    atm = 0.5 - (3 * h - 5) ** 4 + (3 * h - 5) ** 2 + h / 2
    dem = 2 + (3 * h - 5) ** 4 - (3 * h - 5) ** 2 - h / 2

    return atm, dem


def _calculate_total_attributes(strength_points, dexterity_points, intelligence_points, vigor_points,
                                constitution_points):
    total_strength = 100 * tanh(0.01 * strength_points)
    total_dexterity = tanh(0.01 * dexterity_points)
    total_intelligence = 0.6 * tanh(0.01 * intelligence_points)
    total_vigor = tanh(0.01 * vigor_points)
    total_constitution = 100 * tanh(0.01 * constitution_points)

    return total_strength, total_dexterity, total_intelligence, total_vigor, total_constitution


def calculate(character_class, strength_points, dexterity_points, intelligence_points, vigor_points,
              constitution_points,
              height):
    if not isinstance(character_class, CharacterClass):
        raise ValueError("character_class must be an instance of CharacterClass Enum")

    total_strength, total_dexterity, total_intelligence, total_vigor, total_constitution = _calculate_total_attributes(
        strength_points, dexterity_points, intelligence_points, vigor_points, constitution_points
    )

    atm, dem = _calculate_modifiers(height)

    attack = (total_dexterity + total_intelligence) * total_strength * atm
    defense = (total_vigor + total_intelligence) * total_constitution * dem

    return _calculate_performance(character_class, attack, defense)
