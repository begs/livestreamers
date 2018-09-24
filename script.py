import sys, json; 

data = json.load(sys.stdin); 
numStreams = data["_total"]; 

#For prettier output formatting
class formatting:
	HEADER = "\033[95m"
	ENDC = "\033[0m"
	OKGREEN = "\033[92m"
	RED = "\033[91m"
	DEFAULT = "\033[99m"


print "\nCHANNEL " + ' '*13 + "GAME" + ' '*37 + "VIEWERS" + ' '*10 + "\n" + '-'*82

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
	print "{} {} {} {}".format(
		formatting.HEADER + channelName.ljust(20) + formatting.ENDC,
		channelGame.ljust(40), 
		formatting.OKGREEN + channelViewers.ljust(10), 
		formatting.RED + streamType + formatting.ENDC
		)

	if (i == numStreams-1):
		print '-'*82