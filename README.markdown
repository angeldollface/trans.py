# TRANS.PY :snake: :loud_sound:

![GitHub CI](https://github.com/angeldollface/trans.py/actions/workflows/python.yml/badge.svg)

***Transcribe audio files! :snake: :loud_sound:***

## ABOUT :books:

I had to transcibe a long audio file recently for a project at university and I didn't want to do this manually. To do the transcription for me, I coded this tool. Enjoy. :heart:

## USAGE :hammer:

### Requirements

To use this tool, you need the following tools installed and available from the command line:

- [Python 3.x](https://www.python.org/)
- [Git](https://git-scm.org)

### Steps

- 1.) Open a command prompt.

- 2.) Clone this repository's source code with this command:

```bash
git clone https://github.com/angeldollface/trans.py.git
```

- 3.) Change directory into the source code's root directory:

```bash
cd trans.py
```

- 4.) Install *trans.py*'s dependencies:

```bash
python3 -m pip install -r requirements.txt
```

- 5.) Find out how long your audio file is in seconds. The audio file needs to be in the *WAV* file format.

- 6.) Place your audio files into the `trans.py` directory. Transcribe them by running this command from the command line (You can only transcribe one file at a time. Make sure to change the file names of the output files accordingly so no data is lost.):

```bash
python3 src/trans.py --source yourfile.wav --target output.txt --length 45
```

The command above will transcribe a file by the name of `yourfile.wav` with the length of 45 seconds into a text file called `output.txt`. Obviously `yourfile.wav` represents your *WAV* file and 45 represents the length of your *WAV* file in seconds. `python3` may not be the name of your Python 3.x executable, so adjust the command above accordingly.

***IMPORTANT: If you have longer audio files, this tool might struggle! I recommend you chop your WAV file into smaller bits using [Audacity](https://audacityteam.org/).***

## CHANGELOG :black_nib:

### Version 1.0.0

- Initial release.
- Added more documentation.

## NOTE :scroll:

- *Trans.py :snake: :loud_sound:* by Alexander Abraham :black_heart: a.k.a. *"Angel Dollface" :dolls: :ribbon:*
- Licensed under the MIT license.

