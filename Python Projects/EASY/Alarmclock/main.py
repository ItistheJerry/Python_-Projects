# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203/
# https://dl.prokerala.com/downloads/ringtones/files/mp3/twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3

from playsound import playsound
import time
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play

# Loading and Playing an MP3 file


# sound = AudioSegment.from_file("Alarm.mp3", format="mp3")
# play(sound)

# for Setting the target time (year, month, day, hour, minute, second)
# making a different alarm clock for the above later


CLEAR = "\033[2J" # to Remove everything from Screen
CLEAR_AND_RETURN = "\033[H" # to clear the cursor and typed content and return the cursor to starting point

def alarm(seconds):
    time_elapsed = 0


    print(CLEAR)


    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1


        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # 125 // 60 = 2
        seconds_left = time_left % 60 # 125 % 60 = 5


        print(f"{CLEAR_AND_RETURN}Alarm set up To fuck you up in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("Alarm.mp3")


minutes = int(input("How many minutes till I fuck Your Focus:: \n"))

seconds = int(input("How many seconds to add to your fuck up:: \n"))

total_seconds = minutes * 60 + seconds

alarm(total_seconds)