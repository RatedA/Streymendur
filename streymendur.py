from twitchAPI.twitch import Twitch
from twitchAPI.helper import limit
import tomllib
import os
import asyncio
import time
import csv
import datetime

#https://pytwitchapi.readthedocs.io/en/stable/index.html
with open('./config.toml', 'rb') as f:
    config = tomllib.load(f)

app_id = config['ids']['app_id']
app_secret = config['ids']['app_secret']




async def get_streams(): 
    #rippa twitch live channels
    twitch = await Twitch(app_id, app_secret) 
    async for stream in twitch.get_streams(stream_type='live'):
        #yielda stream sem async stream
        yield stream
        

    

async def write_to_csv():
    start_time = time.perf_counter()
    #keyra get_stream() 
    streams = get_streams()
    #búa til og opna csv file
    timecheck = datetime.datetime.now()
    formattime = timecheck.strftime("%d-%m-%Y_%H-%M")
    with open('Streymendur/streymendur/'+'twitch_'+formattime+'.csv', mode='w', encoding="utf-8", errors='ignore') as file:        
        writer = csv.writer(file)
        #búa til raðir
        writer.writerow(['User Id', 'User Name', 'Game', 'Tags'])
        #breyta úr async stream object í str
        async for stream in streams:
            writer.writerow([stream.user_id, stream.user_name, stream.game_name, stream.tags])
            
    end_time = time.perf_counter()
    timetook = end_time-start_time
    print (f"Took {timetook/60:0.2f}mins")
asyncio.run(write_to_csv())

