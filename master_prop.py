class prop:
  def __init__(self,Name="Test",plass = "Weapon",cost = 0):
    self.name = Name
    self.plass = plass
    self.cost = cost
    self.bonus = [('Alchemical','saves',2)]#('Alchemical','saves',2)
    #print(self.name,'has been created and it is a',self.plass)

class equipable(prop):
    #def enhance(self, en):
  pass
class armor_shield(equipable):
  def masterwork(self, en = 0):
    if en < 1:  
      self.name = "MW "+ self.name
    self.mw = True 
    self.pen -= 1
  #def enhance(self, en):
  def __init__(self, name, plass, cost, wht, armor, dex, pen, sp, enh = 0):
    self.weight = wht
    self.armor_bonus = armor
    self.bonus_type = ('armor','shield')[self.weight == 'Shield']
    self.max_dex = dex
    self.penalty = pen
    self.enhancement = enh
    self.spell_fail = sp
    self.speedred = (0,10)[self.weight == "Medium" or self.weight =="Heavy"]
    self.mw =  False
    self.equipped_by = "None"

    if enh > 0:
      self.masterwork(enh)
    prop.__init__(self,name, plass,cost)
  def __repr__(self):
    return repr(self.name+' -- '+self.bonus_type+' -- '+str(self.armor_bonus))


  def equipped(self,owner):
    self.equipped_by = owner.name
    print(self.name,'has been equipped by',owner.name+'!')
    owner.speed -= self.speedred
    owner.spell_fail += self.spell_fail
    owner.ac += self.armor_bonus

  def unequipped(self,owner):
    self.equipped_by = 'None'
    owner.speed += self.speedred
    owner.spell_fail -= self.spell_fail
    owner.ac -= self.armor_bonus
    print(self.name,'has been unequipped by',owner.name+'!')
  pass

class weapon(prop):
  def masterwork(self, en = 0):
    if en < 1:  
      self.name = "MW "+ self.name
    self.mw = True 
    self.pen -= 1
  pass
  
  
