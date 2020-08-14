from xml.etree import ElementTree
import csv
import sys

file = sys.argv[1]

if __name__ == "__main__":

    # Lê ficheiro xml

    tree = ElementTree.parse(file)

    # Cria ficheiro para escrita
    infoFile = open('playerInfo.csv', 'w', newline='', encoding='utf-8')
    csvwriter = csv.writer(infoFile, delimiter=';')

    # Preenche primeira linha
    col_names = ['Name', 'Team', 'Position', 'Number', 'Id', 'Got Stats', 'link']
    csvwriter.writerow(col_names)
    link = ""

    root = tree.getroot()
    # Scrapping da info
    for playerData in root.findall('Player'):
        player_info = []
        name = playerData.find('Names').get('ShortName')
        player_info.append(name)
        team = playerData.get('TeamShortName')
        player_info.append(team)
        position = playerData.find('Function').get('DataValue')
        player_info.append(position)
        number = playerData.get('Number')
        player_info.append(number)
        playerId = playerData.get('Id')
        player_info.append(playerId)

        if playerData.find('SeasonStats'):
            gotStats = "True"
            if playerData.get('TeamShortName') is None:
                fullName = name = playerData.find('Names').get('FullName')
                query = 'zerozero ' + fullName
                try:
                    from googlesearch import search
                except ImportError:
                    print("No Module named 'google' Found")
                for i in search(query, tld='pt', lang='pt', num=1, stop=1, pause=2):
                    link = i
        else:
            gotStats = "False"
            link = ""
        player_info.append(gotStats)
        player_info.append(link)

        csvwriter.writerow(player_info)
    infoFile.close()
    print('CSV complete')
