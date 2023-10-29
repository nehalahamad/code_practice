import requests
from bs4 import BeautifulSoup
import pandas as pd



def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table')

    # fetching table heading
    thead = table.find('thead')
    trow = thead.find('tr')
    columns = [th.text for th in trow.find_all('th')]
    
    # fetching table data
    tbody = table.find('tbody')
    data =  []
    for row in tbody.find_all('tr'):
        data.append([d.text for d in row.find_all('td')])

    return data, columns


url = "https://icc2023.in/register-delegate-list"
# url = "https://icc2023.in/submitted-abstract-list/"
data, columns = get_data(url) 
data = pd.DataFrame(data, columns=columns)
print(data.shape)
print(data.head())