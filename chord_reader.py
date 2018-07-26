import serial
import time
import numpy as np
import pickle

ser = serial.Serial('COM4', 9600)
time.sleep(5)

class Leds:
    def __init__(self, ser):
        self.ser = ser
        self.lightsOn = set()
    
    def switchLights(self, lightsOn):
        lightsOn = set(lightsOn)
        lightsToBeOff = self.lightsOn - lightsOn
        lightsToBeOn = lightsOn - self.lightsOn
        [self.switchLight(key, 0) for key in lightsToBeOff if 0 <= key <= 11]
        [self.switchLight(key, 1) for key in lightsToBeOn if 0 <= key <= 11]
        self.lightsOn = lightsOn
    
    def switchLight(self, key, value):
        cmd = '{} {}\n'.format(key, value)
        self.ser.write(cmd.encode())
        # self.ser.flush()

lds = Leds(ser)

def randon(lds):
    while 1:
        numberOfKeys = np.random.randint(1, 6)
        keys = np.random.randint(1, 13, size=numberOfKeys)
        lds.switchLights(keys)
        time.sleep(0.2)

def cursorToFrame(cursor, duration, num_of_frames):
    frame = np.ceil((num_of_frames/duration)*cursor)
    return int(min(frame, num_of_frames - 1))


def read_chords(input_path, lds):
    input_file = open(input_path, 'rb')
    info = pickle.load(input_file)

    duration = info['duration']
    chroma = info['chroma']
    num_of_frames = chroma[0].size
    
    start = time.time()
    cursor = 0

    # print(duration, num_of_frames)

    while cursor < duration:
        cursor = time.time() - start
        frame = cursorToFrame(cursor, duration, num_of_frames)
        keys = np.nonzero(chroma[:,frame])[0].tolist()
        # if len(keys) > 0:
        #     print(keys)
        lds.switchLights(keys)
        time.sleep(1/1000)

if __name__ == '__main__':
    read_chords('chrods.info', lds)