# DO NOT CHANGE OR DELETE ANYTHING FROM HERE 
import hashlib
import random
import json
import requests
import os

class xyz:

    def __init__(self,url):
        self.url = url
        self.name = str(random.randint(111111,666666)) + '.jpg'
        self.md5 = None

    def downloadit(self):
        r = requests.get(self.url)
        open(self.name,'wb').write(r.content)
    
    def hashit(self):
        openFile = open(self.name,'rb')
        readFile = openFile.read()

        md5Hash = hashlib.md5(readFile)
        md5Hashed = md5Hash.hexdigest()

        self.md5 = md5Hashed

    def checkit(self):
      with open('Hashes.json') as h:
        hashes = json.load(h)
      
      self.result = ''

      if self.md5 in hashes:
        self.result = hashes[self.md5]['name']
      else:
        self.result = 'NOT FOUND'

      h.close()


    def deleteit(self):
        os.remove(self.name)

    def start(self):
      self.downloadit()
      self.hashit()
      self.checkit()
      self.deleteit()

      return self.result