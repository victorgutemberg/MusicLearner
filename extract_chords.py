from utils import atenuate, outlier_filter, supress_neighbours, remove_gaps

import sys
import pickle
import librosa
import librosa.display
import matplotlib.pyplot as plt

file_path = sys.argv[1]
y, sr = librosa.load(file_path)

initial_chroma = librosa.feature.chroma_cqt(y, sr)
K = 1/2
THRESHOLD = 0.8

atenuate(initial_chroma, 0.4, 0.15)
chroma = supress_neighbours(initial_chroma, K)

chroma /= chroma.max()
atenuate(chroma, 0.4, 0.15)

chroma[chroma < THRESHOLD] = 0

for key in chroma:
    remove_gaps(key, min_sound_size=6, max_silence_size=8)
    outlier_filter(key, min_sound_size=10)

chroma /= chroma.max()

info = {
    'duration': y.size/sr,
    'chroma': chroma
}

file_object =  open('chrods.info', 'wb')
pickle.dump(info, file_object)

# librosa.display.specshow(chroma, sr=sr, x_axis='time', y_axis='chroma')
# plt.colorbar()
# plt.show()
