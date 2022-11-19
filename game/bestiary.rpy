define monsterPage = 0

init:
    $ import monster as Mon
    default persistent.monsters = []
    default monsters = persistent.monsters

init 1 python:
    def AddToBestiary(newMon):
        if(MonsterAlreadyAdded(newMon) == False):
            monsters.append(newMon)
            return True
        return False

    def MonsterAlreadyAdded(mon):
        for m in range(0, len(monsters)):
            if(monsters[m] == mon):
                return True
        return False
