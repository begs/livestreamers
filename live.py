import sys, json, requests;
from os.path import exists;
from configparser import ConfigParser;
from setup import *;

# Only necessary to set default encoding in Python 2.* - doesn't work on Python 3.*
try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except Exception:
    pass

config_object = ConfigParser()

# Run setup from setup.py if config hasn't been created
if not exists('config.ini'):
    runSetup()

config_object.read("config.ini")

config = config_object["config"]
accessToken = config["accessToken"]
clientId = config["clientId"]
userId = config["userId"]

# Define headers
headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': clientId,
    'Authorization': 'Bearer ' + accessToken,
}
try:
    response = requests.get('https://api.twitch.tv/helix/streams/followed?user_id=' + userId, headers=headers)

    data = response.json()
    numStreams = len(data["data"])

except (KeyError, ValueError):
    print("Error - make sure the config is configured correctly.")
    sys.exit(1)

print ("\nCHANNEL " + ' '*13 + "GAME" + ' '*37 + "VIEWERS" + ' '*8 + "\n" + '-'*80)


for i in range (0, numStreams):
    channelName = data["data"][i]["user_name"];
    channelGame = data["data"][i]["game_name"];
    channelViewers = str(data["data"][i]["viewer_count"]);
    streamType = data["data"][i]["type"];

    # Check if stream is actually live or VodCast
    if(streamType == "live"):
        streamType = "";
    else:
        streamType = "(vodcast)";

    #Truncate long channel names/games
    if(len(channelName) > 18):
        channelName = channelName[:18] + ".."
    if(len(channelGame) > 38):
        channelGame = channelGame[:38] + ".."

    #Formatting
    print ("{} {} {} {}".format(
	channelName.ljust(20),
	channelGame.ljust(40),
	channelViewers.ljust(8),
	streamType
    ))

    if (i == numStreams-1):
        print ('-'*80)
