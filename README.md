# livestreamers
A simple script that uses Twitch.tv API to check if a user's followed channels are live.

## Usage
Replace *** in ```live.py``` with your [OAuth](https://twitchapps.com/tmi/). 

Then simply run the ```live.py``` script. Example output:
![output](https://puu.sh/ysDHl/533d20b5df.png)


For easier usage you can add a shortcut function in your ```.bash_profile```
```bash
function live() {
  cd ~/livestreamers
  . live.py
}
```
