import requests
import os
import sys
from dotenv import load_dotenv
from github import Github


load_dotenv()

USERNAME = os.getenv('GITHUB_USERNAME')
PASSWORD = os.getenv('GITHUB_PASSWORD')
repo_name = str(sys.argv[1])

g = Github(USERNAME, PASSWORD)
#g = Github("your token")  safer alternative, if you have an access token
u = g.get_user()
repo = u.create_repo(repo_name)