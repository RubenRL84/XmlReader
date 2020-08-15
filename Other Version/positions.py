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
    time.sleep(10)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    posicao = soup.find('span', {'class': "dataValue"}).find_next(('span', {'class': "dataValue"})).find_next('span', {'class': "dataValue"}).find_next(('span', {'class': "dataValue"})).find_next('span', {'class': "dataValue"}).find_next(('span', {'class': "dataValue"})).find_next('span', {'class': "dataValue"}).find_next(('span', {'class': "dataValue"})).find_next('span', {'class': "dataValue"}).getText().strip()
    print(posicao)
    return posicao


if __name__ == "__main__":
    getPosition('https://www.transfermarkt.com/raphael-aflalo/profil/spieler/613505')
