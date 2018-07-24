import sys
import librosa
import librosa.display
import matplotlib.pyplot as plt

file_path = sys.argv[1]
y, sr = librosa.load(file_path)

chroma = librosa.feature.chroma_cqt(y, sr)
K = 1/2
THRESHOLD = 0.35

for i in range(len(chroma)):
    for j in range(len(chroma[i])):
        neighbor1 = (i + 1)%len(chroma)

        chroma[i][j] = chroma[i][j] - (chroma[i - 1][j] + chroma[neighbor1][j])*K

        chroma[i][j] = chroma[i][j] if chroma[i][j] > 0 else 0

chroma[chroma < THRESHOLD] = 0
librosa.display.specshow(chroma, x_axis='time', y_axis='chroma')
plt.colorbar()
plt.show()