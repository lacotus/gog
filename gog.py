# imports, 1 - for handling url requests, 2 - for creating interactable cmd interface
# 1
import requests
import bs4
# 2
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError

# ==========================
# == Handle URLs / Search ==
# ==========================

# get search term and create url
text = input('What are you searching for? ')
url = ('https://google.com/search?q=' + text)

# fetch on the url
request_result = requests.get(url)

# create the soup
soup = bs4.BeautifulSoup(request_result.text, "html.parser")

print(soup)

# grab all major headings
heading_object = soup.find_all('h3')

# iterate through and print as string
for info in heading_object:
	print(info.getText())
	print('-------------------')

# ===========================
# == Start PyInquirer Code ==
# ===========================

# Use the 'from InquirerPy import inquirer' section of this link: 
# https://inquirerpy.readthedocs.io/en/latest/
# Should be under headline 'Alternate Syntax'

