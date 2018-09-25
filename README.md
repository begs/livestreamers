# livestreamers
A python script that uses Twitch.tv API to check if a user's followed channels are live.

## Installation
* Clone ```git clone https://github.com/begs/livestreamers.git``` or [download](https://github.com/begs/livestreamers/archive/master.zip) the repository.

## Usage
Replace ```***``` in ```live.py``` with your Twitch.tv [OAuth](https://twitchapps.com/tmi/). You want the string *after* "oauth:". 

Then simply run the ```live.py``` script. Example output:

![output](https://i.imgur.com/S6Fb0mS.gif)


For easier usage you can add an alias in your ```.bash_profile```:
```bash
function live() {
  cd ~/livestreamers
  . live.py
  cd ~
}
```

## Step-by-step for Windows usage
* You need a way to use bash in Windows. I use [Git Bash](https://git-scm.com/downloads) together with [ConEmu](https://conemu.github.io/).
* If not installed already - download [Python](https://www.python.org/download/releases/2.7/).
	* Add Python to PATH. 
		* System -> Advanced settings -> Environment variables -> Path -> Edit -> Add ```c:\Python27```
* I use [Streamlink](https://github.com/streamlink/streamlink/releases) and [VLC](https://www.videolan.org/vlc/download-windows.nb.html) to open streams from terminal.
* For easier usage, add alias to your bashrc: ```vim ~/.bashrc```:
```bash
#Runs livestreamers script
function live() {
	cd ~/livestreamers
	. live.py
	cd ~
}
#Quicker way to launch streamlink
function twitch() {
    streamlink twitch.tv/$1 best
}

```
