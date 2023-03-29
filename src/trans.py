# TRANS.PY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

import speech_recognition as sr
import argparse

def process_audio(src, target, duration):
    """
    Main function to process the audio
    file.
    """
    try:
        target_file = open(target, 'w')
        target_file = open(target, 'a')
        recog = sr.Recognizer()
        audio = sr.AudioFile(src)
        with audio as source:
            sound = recog.record(source, duration=duration)
            target_file.write(recog.recognize_google(sound))
        target_file.close()
    except Exception as error:
        print(str(error))

def main():
    """
    Main point of entry
    for the tool.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--source')
    parser.add_argument('--target')
    parser.add_argument('--length')
    args = parser.parse_args()
    if args.source and args.target and args.length:
        audio_length = int(args.length)
        process_audio(args.source, args.target, audio_length)
    else:
        print('Invalid options supplied!')

if __name__ == '__main__':
    """
    We call the main
    function.
    """
    main()
    