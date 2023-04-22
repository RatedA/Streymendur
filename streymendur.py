from twitchAPI.twitch import Twitch
from twitchAPI.helper import limit
import asyncio
import time
import csv
import datetime
#twitchAPI.helper import first limit
#https://pytwitchapi.readthedocs.io/en/stable/index.html
app_id = 'mk861jwh10u4x9m6mp0x862b457cxh'
app_secret = '2mjouwif6knma8fo65rtkykyyq9t52'
#twitch = await Twitch(app_id, app_secret, target_app_auth_scope=[AuthScope.USER_EDIT])



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

