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

    def to_list(self):
        return [self.char_class, self.strength_points, self.dexterity_points, self.intelligence_points,
                self.vigor_points, self.constitution_points, self.height]
