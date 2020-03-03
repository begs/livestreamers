# livestreamers
A Python script that uses Twitch.tv API to check if a user's followed channels are live.

## Installation
Clone ```git clone https://github.com/begs/livestreamers.git``` or [download](https://github.com/begs/livestreamers/archive/master.zip) the repository.

## Dependencies
The script uses the 'requests' package in Python:  
```pip install requests```
or ```python -m pip install requests```

## Usage
The first time you run the script, it will prompt for your [OAuth](https://twitchapps.com/tmi/). You want the string *after* "oauth:".  
This is stored in "oauth.txt", in the same path as you run your script.

Then simply run the ```live.py``` script. Example output:
![output](https://i.imgur.com/0Cb48t8.gif)
