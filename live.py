import sys, json, requests; 
#Only necessary to set default encoding in Python 2.* - doesn't work on Python 3.*
try:
	reload(sys)
	sys.setdefaultencoding('utf8')
except Exception:
    pass

headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': 'dsv0rf69bvzgi9ch6ys16vwncjax1z',
    'Authorization': 'OAuth ***',
}

response = requests.get('https://api.twitch.tv/kraken/streams/followed', headers=headers)
data = response.json()

#Try to get stream info from json. Gives KeyError if the OAuth fails         
#Count number of live streams
try:                                                                         
	numStreams = len(data['streams'])                                             
except KeyError:                                                             
    	print ("KeyError - make sure your OAuth is formatted correctly in live.py")
    	sys.exit(1)                                                              
               
print ("\nCHANNEL " + ' '*13 + "GAME" + ' '*37 + "VIEWERS" + ' '*8 + "\n" + '-'*80)

for i in range (0, numStreams): 
	channelName = data["streams"][i]["channel"]["name"];
	channelGame = data["streams"][i]["channel"]["game"];
	channelViewers = str(data["streams"][i]["viewers"]);
	streamType = data["streams"][i]["stream_type"];

	#Check if stream is actually live or VodCast
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
