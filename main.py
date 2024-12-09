import time
from pygame import mixer
#from setting import BEATS_32 as BEATS
#from setting import BEATS_16 as BEATS
from setting import BEATS_6 as BEATS
from setting import BPS

def main():

    ''' index of current bar '''
    bar_index = 0

    notes_per_bar = len(BEATS["0"].keys())

    ''' time interval between each note based on the tempo '''
    interval = 60/(notes_per_bar*BPS)

    ''' starting note to fix audio drowning effects '''
    mixer.Channel(0).play(mixer.Sound("audio\\closed_hihat.wav"))
    time.sleep(0.5)

    running = True
    while running:
        for i, note in enumerate(BEATS[str(bar_index)].keys()):
            for j, hit in enumerate(BEATS[str(bar_index)][str(i)]):
                print(f"BPS: {BPS} | Notes per bar: {notes_per_bar} | ({i},{j}) | {hit}")
                if hit=="crash":
                    ''' crash sound set to unique channel for longer duration '''
                    mixer.Channel(7).play(mixer.Sound(f"audio\\{hit}.wav"))
                else:
                    mixer.Channel(i+j).play(mixer.Sound(f"audio\\{hit}.wav"))

            time.sleep(interval)

        ''' repeats the same '''
        bar_index = (bar_index+1)%4
    return

if __name__=="__main__":
    mixer.init()

    main()