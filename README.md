# A simple dynamic wallpaper for linux,Written in python.

This is a simple dynamic wallpaper,that changes every two hours,in accordance to time of the day.Check out `assets` folder for the pictures
## Usage :

```bash
git clone https://github.com/learnedfool/Dynamic-Wallpaper
cd Dynamic-Wallpaper
chmod 700 .export_env_variable
./.export_env_variable
```
## NOTE :add `.export_env_variable` to startup applications so that the script gets executed on bootup

Open the crontab using :
```bash
crontab -e
```
Add the following lines at the last :
```bash
SHELL=/bin/bash
* */2 * * * ~./Xdbus; /usr/bin/python3 /path/to/wallpaper/script <username>
```