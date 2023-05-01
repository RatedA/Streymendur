import json
import tomli

def openConfig():
    with open("./config.toml", 'rb') as file:
            config = tomli.load(file)
    return config

def openUser():
    with open('./data/users/user.json', 'r') as file:
        readUser = json.load(file)
    return readUser

def openLiveUser():
    with open('./data/users/user_live.json', 'r') as file:
        readLiveUser = json.load(file)
    return readLiveUser

def writeUser():
    with open('./data/users/user.json', 'r') as file:
        writeUser = json.load(file)
    return writeUser

def writeLiveUser():
    with open('./data/users/user_live.json', 'r') as file:
        writeLiveUser = json.load(file)
    return writeLiveUser