# livestreamers
A Python script that uses Twitch.tv API to check if a user's followed channels are live.

## Installation
Clone ```git clone https://github.com/begs/livestreamers.git``` or [download](https://github.com/begs/livestreamers/archive/master.zip) the repository.

## Dependencies
The script uses the 'requests' package in Python:  
```pip install requests```
or ```python -m pip install requests```

## Usage
The Twitch API now requires that the client ID is associated with the OAuth access token. 
You can generate these [here](https://twitchtokengenerator.com/) for example. This script requires adding ```user:read:follows``` to the scope.

You will also need your user ID. This can be found [here](https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/).

The script will prompt you for these and store them in ```config.ini```.

Example output:  
![output](https://i.imgur.com/0Cb48t8.gif)
