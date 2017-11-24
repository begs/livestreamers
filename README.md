# livestreamers
A simple script that uses Twitch.tv API to check if a user's followed channels are live.

## Usage
Replace *** in ```live.py```with your [OAuth](https://twitchapps.com/tmi/). 

Then simply run the script. Example output:
![output](https://puu.sh/ysDFc/3a79ff8d3e.png)


For easier usage you can add a shortcut function in your ```.bash_profile```
```bash
function live() {
  cd ~/livestreamers
  . live.py
}
```
