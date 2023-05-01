from twitchAPI import Twitch
import asyncio
import json
import os
import utility
import datetime
#from datetime import datetime
#this dude adds new users to user.json and updates user_live.json
config = utility.openConfig()
user_file = config['dirs']['user_file']
user_live_file = config['dirs']['user_live']
user_data = utility.openUser()
live_data = utility.openLiveUser()

app_id = config['ids']['app_id']
app_secret = config['ids']['app_secret']

dirpath = './data/'
user_dirpath = './data/users/'
latest_file = None
latest_time = 0

#sos help

for entry in os.scandir(dirpath):
    if entry.is_file():
        mod_time = entry.stat().st_mtime_ns
        if mod_time > latest_time:
            latest_file = dirpath+entry.name
            latest_time = mod_time


def create_user_infile(user_file, new_user_file):
    with open(new_user_file, 'r') as f:
        new_user_data = json.load(f)
    with open(user_file, 'r') as f:
        user_data = json.load(f)

    for key, value in new_user_data.items():
        if key not in user_data:
            user_data[key] = value
    
    with open(user_file, 'w') as f:
        json.dump(user_data, f, indent=4)    


def read_ids(user_file):
    create_user_infile(user_file, latest_file)
    #check_users demands a list so get stream_id as list
    user_id = []
    with open (user_file, 'r') as f:
        data = json.load(f)
    for value in data.values():
        user_id.append(value['stream_id']) 
    return user_id

def addUserData():    
    for key, value in live_data.items():
        if key in user_data:
            user_data[key] = value
            #print(user_data[key])
    with open(user_file, 'w') as f:
        json.dump(user_data, f, indent=4) 


async def check_users(read_ids):
    user_ids = read_ids(user_file)    
    twitch = await Twitch(app_id, app_secret) 
    dumpdict = {}
    time_now = datetime.datetime.now()
    with open('./data/users/user_live.json', mode='w', encoding="utf-8", errors='ignore') as file:
        async for stream in twitch.get_streams(user_id=user_ids):
            #if stream.type == "live":
            live_time = stream.started_at.replace(tzinfo=None)
                #makes time in hours:min instead of days,hours:mins
            delta = time_now.replace(microsecond=0,) - live_time
            deltasec = int(delta.total_seconds())
            hours, remaining_seconds = divmod(deltasec, 3600)
            minutes, _ = divmod(remaining_seconds, 60)
            uptime = f'{hours}:{minutes}'
            timestamp = live_time.timestamp()
            updated_user = {stream.user_login:{"stream_id":stream.user_id, "game":stream.game_name, "type":stream.type, "viewers":stream.viewer_count, "tags":stream.tags, "title":stream.title,"live_since":str(live_time),"live_for":uptime,"timestamp":timestamp}}
            dumpdict.update(updated_user)
        writer = json.dumps(dumpdict, ensure_ascii=False, indent=4, sort_keys=True,)
        file.write(writer)
    addUserData()    




asyncio.run(check_users(read_ids)) #creates new users, runs ids through api and dumps res to user_live

