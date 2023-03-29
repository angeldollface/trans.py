# TRANS.PY :snake: :loud_sound:

![GitHub CI](https://github.com/angeldollface/trans.py/actions/workflows/python.yml/badge.svg)

***Transcribe audio files! :snake: :loud_sound:***

## ABOUT :books:

I had a project for uni where I had to transcribe a long-ass audio and if you think I'd do this by hand, you're mental. Anyway, because most problems can be solved with code, I tried to solve this one with code too. ***Trans.py*** is that solution. Enjoy! :heart:

## USAGE :hammer:

### Requirements

To use this tool, you need the following tools installed and available from the command line:

- [Python 3.x](https://www.python.org/)
- [Git](https://git-scm.org)
- [FFMPEG](https://ffmpeg.org/)

### Steps

- 1.) Download the tool, simply save the file from [this link](https://raw.githubusercontent.com/angeldollface/trans.py/main/src/trans.py).(*You need to have your audio file in the **WAV** format.*)
- 2.) Find out how long your audio file is in seconds.
- 3.) To transcribe your file run this command in the same folder in which you saved this app and your *WAV* file:

```bash
python3 trans.py --source yourfile.wav --target output.txt --length 45
```

The command above will transcribe a file by the name of `yourfile.wav` with the length of 45 seconds into a text file called `output.txt`. Obviously `yourfile.wav` represents your *WAV* file and 45 represents the length of your *WAV* file in seconds.

***IMPORTANT: If you have longer audio files, this tool might struggle! I recommend you chop your WAV file into smaller bits using [Audacity](https://audacityteam.org/).***

## CHANGELOG :black_nib:

- Initial release.
- Added more documentation.

## NOTE :scroll:

- *Trans.py :snake: :loud_sound:* by Alexander Abraham :black_heart: a.k.a. *"Angel Dollface" :dolls: :ribbon:*
- Licensed under the MIT license.

