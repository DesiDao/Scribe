import random
import math
from delta import bonus_tracker


class invList:
  def __init__(self):
    self.great = []
    self.great.clear()
  def apend(self,i):
    self.great.append(i)
  def __repr__(self):
    return repr(self.great)

class skill:
  def __init__(self,name,attr,CC,AbMod,Rank,MiscMod,ACP,Mod):
    self.name = name
    self.attr= attr
    self.CC= CC
    self.AbMod= AbMod
    self.Rank= Rank
    self.MiscMod= MiscMod
    self.ACP= ACP
    self.Mod= Mod

class creature:
    def __str__(self):
      T = self.name+' '+str(self.data['Will'])+' '+str(self.data['StrMod'])+' '+str(self.data['Str'])
      return T 
      
    def __init__(self, Json):
        self.bonus_tracker = bonus_tracker(self)
        self.myinvList = invList()
        self.char_image = Json['PicURL']
        self.deity = Json['Deity']
        self.name = Json['Name']
        self.race= Json['Race']
        self.char_class = Json['Class']
        self.level = Json['Level']

        self.data ={
          'char_image' : Json['PicURL'],
          'deity' : Json['Deity'],
          'name' : Json['Name'],
          'race': Json['Race'],
          'char_class' : Json['Class'],
          'level' : Json['Level'],
          'speed' : Json['Speed'],
          'hp' : Json['HP'],
          'ac' : Json['AC'],
          'init' : Json['Init'],
          'align' : Json['Alignment'],
          'size' : Json['Size'],

          'mbab' : int(Json['MBAB']),
          'rbab' : int(Json['RBAB']),
          'cmb' : int(Json['CMB']),
          'cmd' : int(Json['CMD']),

          'Str': int(Json['Str']),
          'Dex': int(Json['Dex']),
          'Con': int(Json['Con']),
          'Int': int(Json['Int']),
          'Wis': int(Json['Wis']),
          'Cha': int(Json['Cha']),
  
          'StrMod': int(Json['StrMod']),
          'DexMod': int(Json['DexMod']),
          'ConMod': int(Json['ConMod']),
          'IntMod': int(Json['IntMod']),
          'WisMod': int(Json['WisMod']),
          'ChaMod': int(Json['ChaMod']),
    
          'Will': int(Json['Will']),
          'Reflex': int(Json['Reflex']),
          'Fort': int(Json['Fort'])
        }


        '''
        self.general ={
          'speed' : Json['Speed'],
          'hp' : Json['HP'],
          'ac' : Json['AC'],
          'init' : Json['Init'],
          'align' : Json['Alignment'],
          'size' : Json['Size']
        }
        #add to bonus list => self.spell_fail = 0
        self.attacks = {
          'mbab' : Json['MBAB'],
          'rbab' : Json['RBAB'],
          'cmb' : Json['CMB'],
          'cmd' : Json['CMD']
        }
        self.scores = {
            'Str': Json['Str'],
            'Dex': Json['Dex'],
            'Con': Json['Con'],
            'Int': Json['Int'],
            'Wis': Json['Wis'],
            'Cha': Json['Cha']
        }
        self.mod = {
            'Str': Json['StrMod'],
            'Dex': Json['DexMod'],
            'Con': Json['ConMod'],
            'Int': Json['IntMod'],
            'Wis': Json['WisMod'],
            'Cha': Json['ChaMod']
        }
        self.saves = {
            'Will': Json['Will'],
            'Reflex': Json['Reflex'],
            'Fort': Json['Fort']
        }


        self.deity = Json['Deity']
        self.name = Json['Name']
        self.race= Json['Race']
        self.char_class = Json['Class']
        self.level = Json['Level']

        #General
        self.speed = Json['Speed']
        self.hp = Json['HP']
        self.ac = Json['AC']
        self.init = Json['Init']
        self.align = Json['Alignment']
        self.size = Json['Size']

        #attacks 
        self.mbab = Json['MBAB']
        self.rbab = Json['RBAB']
        self.cmb = Json['CMB']
        self.cmd = Json['CMD']

        self.Str= Json['Str']
        self.Dex= Json['Dex']
        self.Con= Json['Con']
        self.Int= Json['Int']
        self.Wis= Json['Wis']
        self.Cha= Json['Cha']

        self.StrMod= Json['StrMod']
        self.DexMod= Json['DexMod']
        self.ConMod= Json['ConMod']
        self.IntMod= Json['IntMod']
        self.WisMod= Json['WisMod']
        self.ChaMod= Json['ChaMod']

        self.Will= Json['Will']
        self.Reflex= Json['Reflex']
        self.Fort= Json['Fort']
        '''
        self.skill_list = []
        base = 'Skill'
        counter = 1
        while True:
          try:
              temp = base
              if counter <= 9:
                temp += '0'
              temp += str(counter)
              Skill = skill(Json[temp],Json[temp+'Ab'],Json[temp+'CC'],Json[temp+'AbMod'],Json[temp+'Rank'],Json[temp+'MiscMod'],Json[temp+'ACP'],Json[temp+'Mod'])
              self.skill_list.append(Skill)
              counter+=1
          except KeyError:
              break
#Make a save

    def save(self, ty, DC):
        roll = random.randint(1, 20)
        attempt = self.saves[ty] + roll
        if roll == 20:
            print('Natural 20!')
        if roll == 1:
            print('Natural 1!')
        if attempt >= DC:
            return True
        return False


#Attack another being

    def attack(self, other):
        roll = random.randint(1, 20)
        hit = roll + self.mod['Str']
        print(self.name, 'attacks', other.name, 'with a', hit, '!')
        print(other.name, 'defends with a', other.ac, 'to defence!')
        if (roll == 20):
            print('Critical Hit!')
        if hit >= other.ac:
            dam = random.randint(1, 6) + self.mod['Str']
            if (roll == 20):
                dam *= 2
            other.hp -= dam
            print('HIT FOR', dam, 'DAMAGE!')
        else:
            print('MISS')
        print(other.name, 'has', other.hp, 'hp remaining!')
        print('')
        print('')

    def DUEL(self, b):
        print('I,', self.name + ',',
              'challenge this BITCH. ASS. PUSSY over yander,', b.name + ',',
              'to a duel to the death! Do you dare muderfukka?!')
        counter = 0
        if (b.save('Fort', 20)):
            initA = random.randint(1, 20) + self.init
            initB = random.randint(1, 20) + b.init
            print(self.name, 'has initiative', initA, '!')
            print(b.name, 'has initiative', initB, '!')
            initiative = ([self, b], [b, self])[initA < initB]
            print(initiative[0].name,
                  'has won the coin toss! LET\'S DRAW BLOOD!!!\n')
            while (self.hp > 0 and b.hp > 0):
                counter += 1
                print('~~~~~~~~~~~~~~~ROUND', counter, '~~~~~~~~~~~~~~~')
                initiative[0].attack(initiative[1])
                if (initiative[1].hp < 0):
                    break
                initiative[1].attack(initiative[0])
            victor = (self.name, b.name)[self.hp < 0]
        else:
            print('Nah bro, I\'m good! *skidaddles*')
            victor = self.name
        print(victor, 'has won the duel after', counter, 'rounds of battle!')

    def pick_up(self, item):
      print(item.name,item.bonus)
      self.bonus_tracker.add(item.name,item.bonus)
      print (4*'\n')
      print('The item has been equipped')
      print(self.bonus_tracker.current_status())
