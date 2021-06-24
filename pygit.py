#! /usr/bin/env python3

from dataclasses import dataclass
import requests as req
import json 
import os
import argparse

from rich.console import Console
from rich.table import Table

GURL = "https://api.github.com"

@dataclass
class GitApi():
    token: str 

    @property
    def header(self):
      return {'Authorization' : f'token {self.token}'}

    def get(self, url=None):
        
        return req.get(url, headers=self.header)
    
    def list_repos(self, uname='LordMero'):
        j = req.get(f'{GURL}/users/{uname}/repos', params={'per_page': '1000'}).json()

        return [{'name': r['name'], 'url' : r['ssh_url'], "updated_at": r["updated_at"].split("T")[0]}for r in j]
           
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
class PrettyTable():
    table_name: str
    lst: list
    
    def __make_table(self):

        table = Table(title=self.table_name)
        table.add_column("Last Update", justify="right", style="cyan")
        table.add_column("Repository", justify="left", style="Magenta")
        table.add_column("URL", justify="left", style="green")
        
        for l in  self.lst:
            table.add_row(l["updated_at"], l["name"], l["url"])

        return table

    def print(self):
        console = Console()
        console.print(self.__make_table())

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--create", help="Name for the remote repository you want to create")
    parser.add_argument("-d", "--delete", help="Name for the remote repository you want to delete")
    parser.add_argument("-l", "--list", help="List remote repositories", action='store_true')
    parser.add_argument("-u", "--user", help="Specify username")
    parser.add_argument("-t", "--token", help="Specify Github API token")

    return parser.parse_args()

def main(ags):
    if args.token is None:
        g = GitApi(token=os.environ['GITTOKEN'])
    else:
        g = GitApi(token=args.token)
        
    if args.user is None:
        user = 'LordMero'
    else:
        user = args.user

    if args.create is not None: 
        r = g.create_repo(args.create)
        if r == 201:
          print(f"Repo {args.create} has been created!")
          print("")
          ans = input("Do you want to run git init? [y]/n", "s") or "y"
          if ans == "y":
            os.systmet("git init")
          else:
            print("Ok.")

    if args.delete is not None:
        r = g.delete_repo(args.delete, user)
        if r == 204:
            print(f"Repo {args.delete} has been deleted!")

    if args.list is not None:
        repos = PrettyTable("Repositories", g.list_repos(user))
        repos.print()


if __name__ == "__main__": 
    args = parse()
    main(args)
