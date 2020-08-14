import time

import requests
from bs4 import BeautifulSoup


def getPosition(url):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    page = requests.get(url, headers=headers)

    # print(page.status_code)
    time.sleep(15)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    posicao = soup.find('div', {'class': "factsheet"}).find_next('span', {'class': 'icn_zerozero'}).find_next('span', {
        'class': 'icn_zerozero'}).next_sibling
    print(posicao)
    return posicao


if __name__ == "__main__":
    getPosition('https://www.zerozero.pt/player.php?id=183886')
