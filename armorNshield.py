class armor_shield:
    def masterwork(self, en=0):
        if en < 1:
            self.name = "MW " + self.name
        self.mw = True
        self.pen -= 1

    def __init__(self, wht, name, gp, armor, dex, pen, sp, enh=0):
        self.weight = wht
        self.name = name

        self.cost = gp
        self.armor_bonus = armor
        self.bonus_type = ('armor', 'shield')[self.weight == 'Shield']
        self.max_dex = dex
        self.penalty = pen
        self.enhancement = enh
        self.spell_fail = sp
        self.speedred = (0, 10)[self.weight == "Medium"
                                or self.weight == "Heavy"]
        self.mw = False
        self.equipped_by = "None"

        if enh > 0:
            self.masterwork(enh)

    def __repr__(self):
        return repr(self.name + ' -- ' + self.bonus_type + ' -- ' +
                    str(self.armor_bonus))

    def equipped(self, owner):
        self.equipped_by = owner.name
        print(self.name, 'has been equipped by', owner.name + '!')
        owner.speed -= self.speedred
        owner.spell_fail += self.spell_fail
        owner.ac += self.armor_bonus

    def unequipped(self, owner):
        self.equipped_by = 'None'
        owner.speed += self.speedred
        owner.spell_fail -= self.spell_fail
        owner.ac -= self.armor_bonus
        print(self.name, 'has been unequipped by', owner.name + '!')

