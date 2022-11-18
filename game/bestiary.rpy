default persistent.monsters = []
default monsters = persistent.monsters

init -1 python:
    class Monster(python_object):
        def __init__ (self, portrait, name, ability, description):
            python_object.__init__(self)
            self.portrait = portrait
            self.name = name
            self.ability = ability
            self.description = description

        def __eq__(self, obj):
            return self.name == obj.name and self.ability == obj.ability and self.description == obj.description
