# livestreamers
A simple script that uses Twitch.tv API to check if a users followed channels are live.

## Usage
Replace *** in ```live.py```with your [OAuth](https://twitchapps.com/tmi/). 

Then simply run the script. Example output:
![output](https://puu.sh/ypiYy/21abcfc047.png)


For easier usage (with bash) you can add a shortcut function in your ```.bash_profile```
```bash
function live() {
  cd ~/livestreamers
  . live.py
}
```
