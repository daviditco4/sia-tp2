from CharacterClass import CharacterClass


class Character:
    attribute_amount = 5

    def __init__(self, char_class, strength_points, dexterity_points, intelligence_points, vigor_points,
                 constitution_points, height):
        self.char_class = char_class
        self.strength_points = strength_points
        self.dexterity_points = dexterity_points
        self.intelligence_points = intelligence_points
        self.vigor_points = vigor_points
        self.constitution_points = constitution_points
        self.height = height

    @classmethod
    def from_list(cls, attr_list):
        if len(attr_list) != Character.attribute_amount + 2:
            raise ValueError('Amount of attributes must be ' + str(Character.attribute_amount + 2))
        return cls(attr_list[0], attr_list[1], attr_list[2], attr_list[3], attr_list[4], attr_list[5], attr_list[6])

    @staticmethod
    def is_valid_from_list(attr_list, total_points_available):
        if len(attr_list) != Character.attribute_amount + 2 or not isinstance(attr_list[0], CharacterClass):
            return False

        addition = 0
        for i in range(1, Character.attribute_amount + 1):
            addition += attr_list[i]
        if addition > total_points_available:
            return False

        if attr_list[Character.attribute_amount + 1] < 1.3 or attr_list[Character.attribute_amount + 1] > 2.0:
            return False
        return True

    @staticmethod
    def unassigned_points_from_list(attr_list, total_points_available):
        addition = 0

        for i in range(1, Character.attribute_amount + 1):
            addition += attr_list[i]

        return total_points_available - addition

    def to_list(self):
        return [self.char_class, self.strength_points, self.dexterity_points, self.intelligence_points,
                self.vigor_points, self.constitution_points, self.height]
