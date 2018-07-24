import sys
import librosa
import librosa.display
import matplotlib.pyplot as plt

file_path = sys.argv[1]
y, sr = librosa.load(file_path)

chroma = librosa.feature.chroma_cqt(y, sr)
print(chroma)
# chroma[chroma < 0.5] = 0
librosa.display.specshow(chroma, x_axis='time', y_axis='chroma')
plt.colorbar()
plt.show()