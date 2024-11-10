from getJson import jGet
from creature import creature
import requests
from bs4 import BeautifulSoup
import re
from creature import creature
from delta import bonus_tracker
from delta import bonus

switch = {
            'Wis': 0,
            'Int': 0,
            'Cha': 0,
            'Con': 0,
            'Str': [say_hi],
            'Dex':[say_hi,say_bye]
            }




key = 'Dex'

for x in switch.get(key, 'Con'):
  x()


print(switch["Str"])
