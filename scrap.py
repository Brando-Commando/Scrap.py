import requests
import lxml
import mysql.connector
from bs4 import BeautifulSoup



search = input("What wikipedia page would you like to search?: ")

# replaces the whitespace with underline, allowing the url to be completed
search = search.replace(" ","_")

# combines the search variable to create a proper URL 
source = requests.get('https://en.wikipedia.org/wiki/' + search)

# Parse the HTML content, using the lxml parser with BeautifulSoup
soup = BeautifulSoup(source.content, 'lxml')

# prints only plain text, 
print(soup.get_text())