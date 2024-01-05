import io

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
response = requests.get(url)
payload = response.text

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(payload, 'html.parser')

# Find the table in the HTML
table = soup.find('table')

# Create a DataFrame from the table
table_string_io = io.StringIO(str(table))
table_dataframe = pd.read_html(table_string_io, header=0)[0]

# Print the DataFrame
print(table_dataframe)
