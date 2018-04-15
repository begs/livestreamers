# livestreamers
A python script that uses Twitch.tv API to check if a user's followed channels are live.

## Usage
Replace ```***``` in ```live.py``` with your [OAuth](https://twitchapps.com/tmi/). 

Then simply run the ```live.py``` script. Example output:
![output](https://puu.sh/ysDHl/533d20b5df.png)


For easier usage you can add a shortcut function in your ```.bash_profile```
```bash
function live() {
  cd ~/livestreamers
  . live.py
}
```
## Step-by-step for Windows usage
* You need a way to use bash in Windows. I use [Git Bash](https://git-scm.com/downloads) together with [ConEmu](https://conemu.github.io/).
* Clone livestreamers ```git clone https://github.com/begs/livestreamers.git```.
* If not installed - download [Python](https://www.python.org/download/releases/2.7/).
* Might be necessary to add Python to path. ```PATH=$PATH:/c/Python27/```
* If you want an alias for the script: make a bash profile file in Windows - ```touch .bashrc```, and add the ```live``` function from above.
* I use [Streamlink](https://github.com/streamlink/streamlink/releases) and [VLC](https://www.videolan.org/vlc/download-windows.nb.html) to open streams from terminal.
