from bs4 import BeautifulSoup
import requests


data = requests.get("https://store.steampowered.com/stats/?l=finnish")

soup = BeautifulSoup(data.text, 'html.parser')

leaderboard = soup.find('div', {'id': 'detailStats'})
table = leaderboard.find('table')
board =[]
for tr in table.find_all('tr',{'class': 'player_count_row'}):
    current_users = tr.find_all('td')[0].text.strip()
    todays_peak = tr.find_all('td')[1].text.strip()
    game = tr.find_all('td')[3].text.strip()
    print(current_users,todays_peak,game)


