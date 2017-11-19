import sys, json; 

data = json.load(sys.stdin); 
num = data["_total"]; 

#For prettier output formatting
class formatting:
	BOLD = "\033[1m"
	ENDC = "\033[0m"
	OKGREEN = "\033[92m"

for i in range (0, num): 
	if (i == 0):
		print "\n"

	channelName = data["streams"][i]["channel"]["name"];
	channelGame = data["streams"][i]["channel"]["game"];
	channelViewers = str(data["streams"][i]["viewers"]);

	#Attempt to get output properly tabulated
	if (len(channelName) < 8):
		channelName = channelName + "\t"
	if (len(channelGame) < 5):
		channelGame = channelGame + "\t"

	print formatting.BOLD + channelName + "\t" + formatting.ENDC + channelGame + "\t" + formatting.OKGREEN + channelViewers + formatting.ENDC

	if (i == num-1):
		print "\n"