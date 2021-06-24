#! /usr/bin/env python3

from dataclasses import dataclass
import requests as req
import sys 
import os 
import json 


GURL = "https://api.github.com/users/"

@dataclass
class git_api():
    token: str 

    @property
    def header(self):
      return {'Authorization' : f'token {self.token}'}

    def get(self, url=None):
        
        return req.get(url, headers=self.header)
    
    def list_repos(self, uname='LordMero'):
        j = req.get(GURL + uname + "/repos").json()

        return [r['name'] for r in j]
           
    def create_repo(self, name):
        r = req.post('https://api.github.com/user/repos', json={'name': name}, headers=self.header)
        print(r.status_code)

    def delete_repo(self, name):
        pass
    
@dataclass 
class pretty_json():
    json: dict

    def __get__(self):
        return self.json

    def __str__(self):
        return json.dumps(self.json,  indent = 1)

if __name__ == "__main__": 
    g = git_api(token=os.environ['GITTOKEN'])


    #g.create_repo('ciccio')

    print(g.list_repos())
