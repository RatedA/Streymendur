import requests
import csv
import asyncio
import json
#
streamURL = "https://api.twitch.tv/helix/streams/" #?first=100&stream_type=live"
searchURL = "https://api.twitch.tv/helix/games?name=Apex Legends"
#gameURL = "https://api.twitch.tv/helix/games/top/?first=100"
authURL = 'https://id.twitch.tv/oauth2/token'
Client_ID = 'mk861jwh10u4x9m6mp0x862b457cxh'
Secret  = '2mjouwif6knma8fo65rtkykyyq9t52'

AutParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }

def scrapeTwitch():
    #channels = []
    AutCall = requests.post(url=authURL, params=AutParams) 
    access_token = AutCall.json()['access_token']
    #id = []
    head = {
    'Client-ID' : Client_ID,
    'Authorization' :  "Bearer " + access_token
    }
    response = requests.get(url = searchURL, headers = head).json()
    print(response)
    #open('wrongstuff.json' as)
    #obj = json.dumps(response, indent=2)
    #print(obj)

if __name__ == '__main__':
	scrapeTwitch()