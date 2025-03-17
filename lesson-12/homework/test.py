import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

url="https://realpython.github.io/fake-jobs"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")
print(soup)