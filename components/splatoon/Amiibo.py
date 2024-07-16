class Amiibo:
    def __init__(self, name, kit_1, kit_2, kit_3, kit_4, kit_5) -> None:
        self.name = name
        self.kit_1 = kit_1
        self.kit_2 = kit_2
        self.kit_3 = kit_3
        self.kit_4 = kit_4
        self.kit_5 = kit_5

    def __str__(self) -> str:
        return self.name + ',' + self.kit_1 + ',' + self.kit_2 + ',' + self.kit_3 + ',' + self.kit_4 + ',' + self.kit_5