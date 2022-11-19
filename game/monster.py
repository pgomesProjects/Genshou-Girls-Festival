class Monster:
    def __init__ (self, portrait, name, ability, description):
        self.portrait = portrait
        self.name = name
        self.ability = ability
        self.description = description

    def __eq__(self, obj):
        return self.name == obj.name and self.ability == obj.ability and self.description == obj.description
