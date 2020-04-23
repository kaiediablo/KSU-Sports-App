'''
-To use this code, you will first need to install the three packages being imported below using pip 3.
-pip3 needs to be installed because pip wont install pandas
'''
from bs4 import BeautifulSoup
import requests
#pandas will need to be installed to verify data accuracy
import pandas as pd

#Website we will be pulling data from
source = requests.get('https://ksuowls.com/sports/mens-basketball/schedule/2018-19').text
#lxml will also need to be installed to use this code
soup = BeautifulSoup(source, 'lxml')

#Verify that data from 2018-2019 season is being pulled (33 games)
basketball_opponents = soup.find_all('div', class_='sidearm-schedule-game-opponent-text')
print("Number of opponents:",len(basketball_opponents))

basketball_results = soup.find_all('div', class_='sidearm-schedule-game-result text-italic')
print("Number of finished games:",len(basketball_results))

basketball_gamedetails = soup.find_all('div', class_='sidearm-schedule-game-opponent-date flex-item-1')
print("Number of game times:",len(basketball_gamedetails))

#Lists to store the scraped information
opponents = []
results = []
game_times = []

#Add each respective result to 'Opponents' list
for opponent in basketball_opponents:
    name = opponent.a.text
    opponents.append(name)

#Add each respective result to 'Results' list
for score in basketball_results:
    #strip and replace rules added to make the output more legible
    final = score.text.strip('\n\n').rstrip('\n\n').replace(',\n',' ').replace('\n(OT)',' (OT)')
    results.append(final)

#Add each respective result to 'Game Details' list
for detail in basketball_gamedetails:
    #strip and replace rules added to make the output more legible
    time = detail.text.strip('\n').rstrip('\n').replace('\n',' ').replace('  ',' ')
    game_times.append(time)

#View contents of each list
print(opponents)
print(results)
print(game_times)

#Verify data is logged in an organized manner
test_df = pd.DataFrame({'Opponent':opponents,'Result':results,'Game Details':game_times})
print(test_df.info())
#Download full results for KSU Basketball's 2018-2019 season as csv file
test_df.to_csv('KSU Basketball 2018-2019 Season Results.csv')
