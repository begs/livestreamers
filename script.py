import sys, json;
reload(sys)
sys.setdefaultencoding('utf8')

#Load the stream info
data = json.load(sys.stdin);

#For prettier output formatting
class formatting:
	BOLD = "\033[1m"
	ENDC = "\033[0m"
	OKGREEN = "\033[92m"
	RED = "\033[91m"
	DEFAULT = "\033[99m"

#Try to get stream info from json. Gives KeyError if the OAuth fails         
try:                                                                         
    numStreams = data["_total"];                                             
except KeyError:                                                             
    print formatting.RED + "KeyError - make sure your OAuth is formatted correctly in live.py." + formatting.ENDC
    sys.exit(1)                                                              
                                                                             
for i in range (0, numStreams): 
	if (i == 0):
		print "\n"

	channelName = data["streams"][i]["channel"]["name"];
	channelGame = data["streams"][i]["channel"]["game"];
	channelViewers = str(data["streams"][i]["viewers"]);
	streamType = data["streams"][i]["stream_type"];

	#Attempt to get output properly tabulated
	if (len(channelName) < 8):
		channelName = channelName + "\t"
	elif(len(channelName) > 12):
		channelName = channelName[:12] + ".."

	if(len(channelGame) < 8):
		channelGame = channelGame + "\t\t"
	elif(len(channelGame) < 16 and len(channelGame) > 5):
		channelGame = channelGame + "\t"
	elif(len(channelGame) > 20):
		channelGame = channelGame[:20] + ".."

	#Check if stream is actually live or VodCast
	if(streamType == "live"):
		streamType = "";
	else:
		streamType = "(vodcast)";

	print formatting.BOLD + channelName + "\t" + formatting.ENDC + channelGame + "\t" + formatting.OKGREEN + channelViewers + formatting.RED + "\t" + streamType + formatting.ENDC

	if (i == numStreams-1):
		print "\n"
