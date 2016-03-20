"""Simple example that shows how to use `alexa_client` and `simple_tts`
together to programatically interact with Amazon Alexa Voice Service.
"""
from alexa_client import AlexaClient
import simple_tts
import subprocess
import shlex
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def play_mp3(filename, padding=True, pad_each=False):
    """Plays MP3 audio file(s).

    Uses the shell command `mpg123` to play the MP3 file(s).

    Args:
        filename (str or list): File(s) to play.
        padding (bool): Whether to add a 1 second silent padding before the
                        first mp3 file to improve audio.
        pad_each (bool): Whether to add a 1 second silent padding before
                         each file in the list.

    Returns:
        None
    """
    cmd = "mpg123 "
    cmd_args = ["-q", ]
    pause = "{}/1sec.mp3".format(BASE_PATH)
    if padding:
        cmd_args.append(pause)
    if isinstance(filename, list):
        if pad_each:
            for f in filename:
                cmd_args.append(pause)
                cmd_args.append(f)
        else:
            cmd_args += filename
    else:
        cmd_args.append(filename)
    cmd += " ".join(cmd_args)
    cmd = shlex.split(cmd)
    # Use subprocess.Popen() and communicate() so the audio isn't cut off
    p = subprocess.Popen(cmd)
    p.communicate()


def main():
    alexa = AlexaClient()
    print
    print "Type 'quit' to exit"
    quit = False
    while not quit:
        text = raw_input("Command to send to Alexa: ")
        if text == 'quit':
            quit = True
        else:
            # Perform tts
            audio_command = simple_tts.tts(text)
            # Send the command to Alexa
            audio_response = alexa.ask(audio_command)
            # Play the response
            play_mp3(audio_response)


if __name__ == '__main__':
    main()
