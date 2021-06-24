#! /usr/bin/env python3

from dataclasses import dataclass
import requests as req
import json 
import os
import argparse

GURL = "https://api.github.com"

@dataclass
class git_api():
    token: str 

    @property
    def header(self):
      return {'Authorization' : f'token {self.token}'}

    def get(self, url=None):
        
        return req.get(url, headers=self.header)
    
    def list_repos(self, uname='LordMero'):
        j = req.get(f'{GURL}/users/{uname}/repos').json()

        return [r['name'] for r in j]
           
    def create_repo(self, name):
        h = self.header

        h['Accept'] = 'application/vnd.github.v3+json'

        r = req.post(f'{GURL}/user/repos', json={'name': name}, headers=h)
        return r.status_code

    def delete_repo(self, name, uname='LordMero'):
        
        h = self.header

        h['Accept'] = 'application/vnd.github.v3+json'

        r = req.delete(f'{GURL}/repos/{uname}/{name}', headers=h)
        return r.status_code

@dataclass 
class pretty_json():
    json: dict

    def __get__(self):
        return self.json

    def __str__(self):
        return json.dumps(self.json,  indent = 1)

if __name__ == "__main__": 


    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--create", help="Name for the remote repository you want to create")
    parser.add_argument("-d", "--delete", help="Name for the remote repository you want to delete")
    parser.add_argument("-l", "--list", help="List remote repositories", nargs='?')
    parser.add_argument("-u", "--user", help="Specify username")
    parser.add_argument("-t", "--token", help="Specify Github API token")

    args = parser.parse_args()

    if args.token is None:
        g = git_api(token=os.environ['GITTOKEN'])
    else:
        g = git_api(token=args.token)
        
    if args.user is None:
        user = 'LordMero'
    else:
        user = args.user

    if args.create is not None: 
        r = g.create_repo(args.create)
        if r == 201:
          print(f"Repo {args.create} has been created! Remember to run git init locally.")

    if args.delete is not None:
        r = g.delete_repo(args.delete, user)
        if r == 204:
            print(f"Repo {args.delete} has been deleted!")


    if args.list is not None:
        print(g.list_repos(user))

