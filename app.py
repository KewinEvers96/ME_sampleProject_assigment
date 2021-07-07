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

    height_checked = dict()
    height_pairs = []
    counter = 0
    for playerHeight, players in dict_players.items():
        
        if playerHeight in height_checked:
            continue 
        height_checked[playerHeight] = True
        
        substraction = height - playerHeight
        if substraction < 0:
            break
        matchedPlayers = dict_players.get(substraction, False)
        if matchedPlayers is False:
            continue
        height_checked[substraction] = True
        for p1 in players:
            for p2 in matchedPlayers:
                if p1 != p2:
                    print(p1, p2)
                    counter +=1
    
    if counter == 0:
        print("Not players found")
    else:
        print("Players matched", counter)
if __name__ == "__main__":
    try:
        number = int(sys.argv[1])

        if number < 0:
            raise Exception("Negative number entered, please enter a positive value")

        
        getPlayers(number)
    except IndexError as ie:
        print("Please specify a height to begin the query")

    except ValueError as ve:
        print("Please enter a number as height")

    except Exception as e:
        print(e)
