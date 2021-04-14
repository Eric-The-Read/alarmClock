# Alarm Clock
This is an alarm clock made using the PySimpleGUI library. This is one of my first projects built for a GUI.

# Motivation
My motivation for this project was to build an alarm clock with some/most of the functionality one would expect from a regular alarm clock app. I wanted to learn how to structure a python project, `import` from submodules, etc. Additionally, I wanted to learn how to build a GUI, so I decided to start with something that most people use on a daily basis.

# Features
Ability to customize alarms, which includes:
- Alarm tones
- Renaming an alarm
- Selecting days alarm plays
- Toggle alarm on/off

The time can also be formatted using the format codes in the datetime module, described [here](https://docs.python.org/3/library/datetime.html)

# Running
To install dependencies:
```
pip install /path/to/alarmClock
```
Next, open alarm clock app using:
```
python /path/to/alarmClock/cli.py
```

# Note
I tried to structure this project in a logical and intuitive manner, although I imagine that the organizational system and the code contained within are a nightmare to more experienced programmers. I would love to hear your feedback, questions or concerns regarding this project.

# Credits
- [jason990420](https://github.com/PySimpleGUI/PySimpleGUI/issues/3668 )-> Example for triggering a combo box to drop down automatically when the mouse hovers over it

- MikeTheWatchGuy's examples on PySimpleGUI github issues page

- PySimpleGUI [documentation](https://pysimplegui.readthedocs.io/en/latest/) & [Cookbook](https://pysimplegui.readthedocs.io/en/latest/cookbook/)

- [This](https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory) Stackoverflow question regarding listing all files in a directory.

- Default sounds are from [soundbible.com](https://soundbible.com/)

## Sound Files
- [siren.ogg](https://commons.wikimedia.org/wiki/File:Alarm_(Sirenenprobe_am_5._Oktober_2019)_in_%C3%96sterreich_1_Min_auf_und_ab.ogg) Attribution: 32-Fuß-Freak, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons

- [pager.wav](https://soundbible.com/1766-Fire-Pager.html) Attribution: jason, Public Domain, via Sound Bible

- [beep.wav](https://soundbible.com/1251-Beep.html) Attribution: Mike Koenig, CC BY 3.0,<https://creativecommons.org/licenses/by/3.0/>, via Sound Bible

- [shipBell.wav](https://soundbible.com/1746-Ship-Bell.html) Attribution: Mike Koenig, CC BY 3.0, <https://creativecommons.org/licenses/by/3.0/>, via Sound Bible

- [rooster.wav](https://soundbible.com/1218-Rooster-Crow.html) Attribution: Mike Koenig, CC BY 3.0, <https://creativecommons.org/licenses/by/3.0/>, via Sound Bible

