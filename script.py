import sys, json; 

data = json.load(sys.stdin); 
numStreams = data["_total"]; 

#For prettier output formatting
class formatting:
	BOLD = "\033[1m"
	ENDC = "\033[0m"
	OKGREEN = "\033[92m"

for i in range (0, numStreams): 
	if (i == 0):
		print "\n"

	channelName = data["streams"][i]["channel"]["name"];
	channelGame = data["streams"][i]["channel"]["game"];
	channelViewers = str(data["streams"][i]["viewers"]);

	#Attempt to get output properly tabulated
	if (len(channelName) < 8):
		channelName = channelName + "\t"
	elif(len(channelName) > 12):
		channelName = channelName[:12] + ".."

	if(len(channelGame) < 5):
		channelGame = channelGame + "\t\t"
	elif(len(channelGame) < 16 and len(channelGame) > 5):
		channelGame = channelGame + "\t"
	
	if(len(channelGame) > 20):
		channelGame = channelGame[:20] + ".."

	print formatting.BOLD + channelName + "\t" + formatting.ENDC + channelGame + "\t" + formatting.OKGREEN + channelViewers + formatting.ENDC

	if (i == numStreams-1):
		print "\n"