import requests
from bs4 import BeautifulSoup
import hashlib
from creature import creature


class jGet:
  def verified_Login(self): 
    #only way to add name will be through event listener
    s = requests.Session()
    r = s.get(self.url)
    soup = BeautifulSoup(r.text, "html.parser")
    form = soup.find("form",{"id":"login_form"})

    ######
    payload = dict([(t.get("name"),t.get("value","")) 
      for t in form.findAll("input")
      if t.get("name")
    ])

    md5 = hashlib.md5(self.password.encode('utf-8')).hexdigest()
    payload["vb_login_username"] = self.username
    payload["vb_login_password"] = self.password
    payload["vb_login_md5password"] = md5
    payload["vb_login_md5password_utf"] = md5

    r = s.post(f"{self.url}/login.php", 
	    params= {"do": "login"},
	    data = payload
    )
    r = s.get(f"{self.url}/sheets")
    soup = BeautifulSoup(r.text, "html.parser")
    check = soup.find(id='vb_login_username') #if check has a value other than 'None' it is good
    if not check:
      #if check == None, then login was successful and we should continue as normal
      #if check != None, it f*ked the login and everything failed!
      rows = soup.find("table").find_all("tr")[1:]
      if (self.name!=''): #if searching a name
        sheet_data = []
        for row in rows:
          tds = row.find_all("td")
          if (tds[1].text.strip() == self.name):
            download_link = f'{self.url}{tds[5].find("a")["href"]}'
            Json = s.get(download_link)
            if Json:#test that it actually got a file, only false should be from empty character sheet
              sheet_data.append({
                "json": Json.json()
              })
              return sheet_data[0]['json']['sheet_data']['jsondata']
            else:
              return False
            
      else: #list all
        sheet_data = []
        for row in rows:
          tds = row.find_all("td")
          download_link = f'{self.url}{tds[5].find("a")["href"]}'
          if (tds[2].text.strip() =='Pathfinder'):
            sheet_data.append({
              "name": tds[1].text.strip(),
              "game": tds[3].text.strip()
            })
        self.current_char = sheet_data
        return self.current_char
    
    else:
      return False

  def __init__(self,_u,_p,_n=''):
    self.username = _u
    self.password = _p
    self.url = "https://www.myth-weavers.com"
    self.data = ''
    self.name= _n

def returnJson(username='',password='',name=''):
    Json = jGet(username,password,name)
    Json = Json.verified_Login()
    return Json
