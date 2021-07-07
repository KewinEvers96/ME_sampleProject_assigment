from urllib import request
import json
import sys


def getPlayers(height):
    url = 'https://mach-eight.uc.r.appspot.com'

    response = request.urlopen(url).read()

    data = response.decode()
    json_data = json.loads(data)
    players = json_data['values']
    
    dict_players = dict()
    for player in players:
        height_in_dict = dict_players.get(int(player['h_in']), False)
        if height_in_dict is False:
            dict_players[int(player['h_in'])] = ["{} {}".format(player['first_name'], player['last_name'])]
        else:
            dict_players[int(player['h_in'])].append("{} {}".format(player['first_name'], player['last_name']))

    
    for playerHeight, players in dict_players.items():
        
        substraction = height - playerHeight
        if substraction < 0:
            break
        matchedPlayers = dict_players.get(substraction, False)
        if matchedPlayers is False:
            continue
        print(players, matchedPlayers)

if __name__ == "__main__":
    try:
        getPlayers(int(sys.argv[1]))
    except Exception as e:
        print(e)