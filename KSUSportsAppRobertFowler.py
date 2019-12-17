'''
To use this code, you will first need to install the three packages being imported below using pip.
'''
from bs4 import BeautifulSoup
import requests
#pandas will need to be installed to verify data accuracy
import pandas as pd

#Website we will be pulling data from
source = requests.get('https://ksuowls.com/sports/football/schedule').text
#lxml will also need to be installed to use this code
soup = BeautifulSoup(source, 'lxml')


#Verify that data from 2019 season is being pulled (14 games)
fb_opponents = soup.find_all('div', class_='sidearm-schedule-game-opponent-text')
print("Number of opponents:",len(fb_opponents))

fb_results = soup.find_all('div', class_='sidearm-schedule-game-result text-italic')
print("Number of finished games:",len(fb_results))

fb_gamedetails = soup.find_all('div', class_='sidearm-schedule-game-opponent-date flex-item-1')
print("Number of game times:",len(fb_gamedetails))

#Lists to store the scraped information
opponents = []
results = []
game_times = []

#Add each respective result to 'Opponents' list
for opponent in fb_opponents:
    name = opponent.a.text
    opponents.append(name)

#Add each respective result to 'Results' list
for score in fb_results:
    #strip and replace rules added to make the output more legible
    final = score.text.strip('\n\n').rstrip('\n\n').replace(',\n',' ').replace('\n(OT)',' (OT)')
    results.append(final)

#Add each respective result to 'Game Details' list
for detail in fb_gamedetails:
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
#Download full results for KSU Football's 2019 season as csv file
test_df.to_csv('KSU Football 2019-2020 Season Results.csv')