#This page will keep track of all changes and status effects that the character is currently going through
group = {
  'attacks': ['attack.melee','attack.range'],
  'saves' : ['Will', 'Dex', 'Fort'],
  'scores' : ['Str', 'Dex',  'Con',  'Int',  'Wis',  'Cha'],
  'AC':['AC','touch', 'flat'],
  'damage': ['damage.melee','damage.ranged']
}
bonusIndexS = { #source and domains
    'Alchemical': ['scores','saves'],
    'Armor': ['AC'],
    'BAB': ['attacks'],
    'Circumstance': ['attacks', 'checks'],
    'Competence': ['attacks', 'checks','saves'],
    'Deflection': ['AC'],
    'Dodge': ['AC'],
    'Enhancement': ['scores', 'AC', 'attacks', 'damage', 'speed'],
    'Inherent': ['scores'],
    'Insight': ['AC', 'attacks', 'checks', 'saves'],
    'Luck': ['AC', 'attacks', 'checks', 'damage', 'saves'],
    'Morale': [
        'attacks', 'checks', 'damage', 'saves','Str', 'Con',
        'Dex'
    ],
    'Natural': ['AC'],
    'Profane': ['AC', 'checks', 'damage', 'DC', 'saves'],
    'Racial': 'none',
    'Resistance': ['saves'],
    'Sacred': ['AC', 'checks', 'damage', 'DC', 'saves'],
    'Shield': ['AC'],
    'Size': ['scores', 'attacks', 'AC'],
    'Trait':
    'none'
}

bonusIndexA = {#attribute
    'attacks': [
        'BAB', 'Circumstance', 'Competence', 'Enhancement',
        'Insight', 'Luck', 'Morale', 'Size'
    ],
    'AC': [
      'Armor', 'Deflection', 'Dodge', 'Enhancement','Insight','Luck','Natural',  'Profane','Sacred','Shield','Size'
    ],
    'checks' : ['Circumstance','Competence','Insight','Luck','Morale','Profane','Sacred'],
    'damage' : ['Enhancement','Luck','Morale','Profane','Sacred'],
    'DC' : ['Profane','Sacred'],
    'saves' : [
      'Alchemical','Competence','Insight','Luck','Morale','Profane','Resistance','Sacred'
    ],
    'scores' : ['Alchemical','Enhancement','Inherent','Size']
}
#('Elf Robe','Competence','Stealth','4',10)
currentB = {}

currentE = {}

class bonus:
        def __gt__(self, other):#bonus is greater if the bonus_source is same and value is greater
            return (self.bonus_source == other.bonus_source and self.bonus_attribute == other.bonus_attribute and self.value > other.value)

        def __lt__(self, other):
            return not self.__gt__(other)
        
        def __eq__(self,other): #equal is not the same as stackable
            #print(f'{self.item_source} vs {other.item_source}')
            #print((self.item_source == other.item_source and self.bonus_attribute == other.bonus_attribute))
            return (self.item_source == other.item_source and self.bonus_attribute == other.bonus_attribute and self.bonus_source == other.bonus_source)
        
        def __ne__(self,other):
            return not self.__eq__(other)
        
        def stackable(self,other):
          return (self.bonus_source == 'Dodge' or self.bonus_source != other.bonus_source or self.bonus_source == other.bonus_source and self.bonus_attribute != other.bonus_attribute)

        def __init__(self, #('Elf Robe','Competence','attacks','4',10) #time measured in rounds, 6 second per round
                     item_source, #name of the item itself
                     bonus_source, #
                     bonus_attribute,
                     value = 1,
                     duration = 6):
            self.item_source = item_source
            self.bonus_source = bonus_source
            self.bonus_attribute = bonus_attribute
            self.value = value
            self.duration = duration

            
        def __repr__(self):
          return f'{self.item_source}\t{self.bonus_source}\t{self.bonus_attribute}\t{str(self.value)}\t{str(self.duration)}'

class bonus_tracker:
  def __init__(self,char_data = []):
        self.blist = list()
        self.backup_bonus = list()
        self.blist.clear()
        self.backup_bonus.clear()
        self.char = char_data
  
  def change_priority(self,Bonus): #should only be called by functions activate and deactivate
      print(f'change_priority called on {Bonus.item_source}')
      start,end = (self.backup_bonus,self.blist)[Bonus in self.blist],(self.blist,self.backup_bonus)[Bonus in self.blist]#default is a promotion, if not in blist end is now in blist
      if start == self.blist:
        print ("starting blist")
      else:
        print ("starting back_up")
      if end == self.blist:
        print ("ending blist")
      else:
        print ("ending back_up")
      end.append(Bonus)
      start.remove(Bonus)
      print(self)
    
  def __str__(self):
      return (f'Current effects\n{self.blist}\n\nWaiting Effects\n{self.backup_bonus}')

#('Elf Robe','Competence','Str','4',10)
  def add(self, bonus):#change the noted bonus
    print('\nAdding bonus')
    self.char.data[bonus.bonus_attribute] += bonus.value
    self.blist.append(bonus)
    print('Bonus Added')
    print(self.char)


  def expire(self,bonus): #revert the noted bonus
    print('\nbonus expired')
    self.char.data[bonus.bonus_attribute] -= bonus.value
    print('calling prio change')
    self.change_priority(bonus)
    print('bonus removed')
    print(self.char)


  def activate(self, bonusList):#gain a source name and an enhancement list, add each bonus 
      for bon in bonusList: #if it exists, call it out
        print(f'\n**add {bon}')
        if (bon in self.blist or bon in self.backup_bonus):
          print('Duplicate Bonus Error')
          print(bon)
          return
      
        if not self.blist: #if bonus list is empty, add automatically
          self.add(bon)
          continue

        for boni in self.blist:
          if not boni.stackable(bon):#if bonusList has no bonus greater than bon, add bon to bonusList, else add to backup_bonus
            print('Comparing:')
            self.compare(boni,bon)
            continue


  def compare(self,sett,new):
      print('\nEntered compare function')
      if new > sett:
        print('\nCalling expire function from compare')
        self.expire(sett)
        print('\nCalling add function from compare')
        self.add(new)
      else:
        self.backup_bonus.append(new)

  def reduce(): #called account for passed time on all existing bonuses
      pass
  def deactivate(self,bonus): #called on a bonus that has a duration equal to zero. Apply -1*Buff to character and erase buff
      pass
      #self.change_priority(temp)
  
condition = { #known list of bonuses
  'shaken' : [bonus('Shaken','Morale','Str',-4,10), bonus('Shaken','Morale','Dex',-4,10)],
  'dazzled' : [bonus('Dazzled','Untyped',group['attacks'],-1,3)],
  'booboo' : [bonus('Booboo','Untyped', 'Str',-2,3)]
}

#('Alchemical','Will', 'Dex', 'Fort',2)
#receive bonus
#print(creature,"recieved an",bonus,"bonus to his", raised)
'''
Check to see if buff is valid
if valid add to '''

#character.equip(item) => character.equipped_list.add(item.name), character.bonus_list.add(item.bonus_list)

'''
Deafened
A deafened character cannot hear. He takes a –4 penalty on initiative checks, automatically fails Perception checks based on sound, takes a –4 penalty on opposed Perception checks, and has a 20% chance of spell failure when casting spells with verbal components. Characters who remain deafened for a long time grow accustomed to these drawbacks and can overcome some of them.
'''
