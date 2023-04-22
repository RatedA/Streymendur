import requests
import csv
import asyncio
#import json

#app_id = 'mk861jwh10u4x9m6mp0x862b457cxh'
#app_secret = 'q2d77wx8acmge96pyaqatb257evpa6'
#gamelist = ['489136']

streamURL = "https://api.twitch.tv/helix/streams/" #?first=100&stream_type=live"
searchURL = "https://api.twitch.tv/helix/search/channels?query=iceland&live_only=true"
gameURL = "https://api.twitch.tv/helix/games/top/?first=100"
authURL = 'https://id.twitch.tv/oauth2/token'
Client_ID = 'mk861jwh10u4x9m6mp0x862b457cxh'
Secret  = 'q2d77wx8acmge96pyaqatb257evpa6'

AutParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }

def scrapeTwitch():
    channels = []
    AutCall = requests.post(url=authURL, params=AutParams) 
    access_token = AutCall.json()['access_token']

    head = {
    'Client-ID' : Client_ID,
    'Authorization' :  "Bearer " + access_token
    }
    response = requests.get(url = searchURL, headers = head).json()

    for stream in response['data']:
        viewers = stream['viewer_count']
        if viewers >= 100:
            tags = stream['tags']
            name = stream['user_name']
            stream_id = stream['user_id']
            game_name = stream['game_name']
            #cursor = stream['cursor']
            channels.append((name, stream_id, tags, game_name))
            #channels.insert(0, response['pagination'])
    return channels

#def pagination():
     
 

def writeData(streams):
    with open('E:\orri\Documents\pyprojects\Streymendur\prufa.csv', 'w', encoding="utf-8", errors='ignore') as f:
        writer = csv.writer(f)
        writer.writerows(streams)
    return 0

def main():
    streams = scrapeTwitch()
    writeData(streams)
    return 0
if __name__ == '__main__':
	main()