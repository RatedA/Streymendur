from twitchAPI.twitch import Twitch
from twitchAPI.helper import limit
import tomli
import json
import asyncio
import time
import datetime
"""




"""
#https://pytwitchapi.readthedocs.io/en/stable/index.html
 
with open('./config.toml', 'rb') as f:
    config = tomli.load(f)

app_id = config['ids']['app_id']
app_secret = config['ids']['app_secret']


async def get_streams(): 
    #rippa twitch live channels
    twitch = await Twitch(app_id, app_secret) 
    async for stream in twitch.get_streams(stream_type='live'):
        #yielda stream sem async stream
        yield stream
        

async def write_to_json():
    start_time = time.perf_counter()
    streams = get_streams()
    searchterm = ['icelandic', 'iceland', 'Icelandic', 'Iceland']
    timecheck = datetime.datetime.now()
    formattime = timecheck.strftime("%d-%m-%Y_%H-%M")
    dumpdict = {}
    #filtering magic
    with open('./data/'+'twitch_'+formattime+'.json', mode='w', encoding="utf-8", errors='ignore') as file:
        async for stream in streams:
            #from async stream to dict to json + filtering
            if stream.tags is not None and any(term in stream.tags for term in searchterm):
                jsonread = {stream.user_login:{'stream_id':stream.user_id}}
                print(jsonread)
                dumpdict.update(jsonread)
                
        writer = json.dumps(dumpdict, ensure_ascii=False, indent=4, sort_keys=True,)
        file.write(writer)

        
    end_time = time.perf_counter()
    timetook = end_time-start_time
    print (f"Took {timetook/60:0.2f}mins")


asyncio.run(write_to_json())