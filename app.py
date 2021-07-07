from urllib import request
import json
import sys
from player import Player


def getPlayers(height):
    url = 'https://mach-eight.uc.r.appspot.com'

    response = request.urlopen(url).read()

    data = response.decode()
    json_data = json.loads(data)
    players = json_data['values']
    
    listOfMatches = []

    dict_players = dict()
    index = 0
    for player in players:
        height_in_dict = dict_players.get(int(player['h_in']), False)
        if height_in_dict is False:
            dict_players[int(player['h_in'])] = [Player(index, player['first_name'] +" " + player['last_name'], player['h_in'])]
        else:
            dict_players[int(player['h_in'])].append(Player(index, player['first_name'] +" " + player['last_name'], player['h_in']))
        index += 1
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
        
        if substraction != playerHeight:
            for p1 in players:
                for p2 in matchedPlayers:
                    if p1 != p2:
                        listOfMatches.append((p1, p2))
                        counter +=1
        else:
            for i in range(len(players)):
                for j in range(i+1, len(players)):
                    listOfMatches.append((players[i], players[j]))
                    counter += 1
    if counter == 0:
        print("Not matches found")
    else:
        print("Pair of players matched", counter)
    
    return listOfMatches
if __name__ == "__main__":
    try:
        number = int(sys.argv[1])

        if number <= 0:
            raise Exception("Negative number o zero entered, please enter value greater than zero")

        
        listOfMatches = getPlayers(number)
        
        for match in listOfMatches:
            print(match[0], "\t", match[1])

    except IndexError as ie:
        print("Please specify a height to begin the query")

    except ValueError as ve:
        print("Please enter a number as height")

    except Exception as e:
        print(e)
