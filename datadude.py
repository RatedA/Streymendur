from twitchAPI import Twitch
import asyncio
import json
import os
import tomli

with open('./config.toml', 'rb') as f:
    config = tomli.load(f)

app_id = config['ids']['app_id']
app_secret = config['ids']['app_secret']

#get latest file
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


def update_user_file(user_file, new_user_file):
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
    user_id = []
    with open (user_file, 'r') as f:
        data = json.load(f)
    for value in data.values():
        user_id.append(value['stream_id']) 
    return user_id


async def check_users(read_ids):
    user_ids = read_ids("data/users/user.json")    
    twitch = await Twitch(app_id, app_secret) 
    dumpdict = {}
    with open('./data/users/user_live.json', mode='w', encoding="utf-8", errors='ignore') as file:
        async for stream in twitch.get_streams(user_id=user_ids):
            if stream.type == "live":
                updated_user = {stream.user_login:{"stream_id":stream.user_id, "game":stream.game_name, "type":stream.type, "viewers":stream.viewer_count, "tags":stream.tags, "title":stream.title}}
            #print(updated_user)
                dumpdict.update(updated_user)
        writer = json.dumps(dumpdict, ensure_ascii=False, indent=4, sort_keys=True,)
        file.write(writer)    
    

asyncio.run(check_users(read_ids))



#update_user_file("data/users/user.json", latest_file)
