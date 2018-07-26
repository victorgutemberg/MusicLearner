import numpy as np


def normalizeRows(M):
    row_sums = M.sum(axis=1)
    return M / row_sums

def atenuate(M, threshold, value):
    M[M > threshold] += value
    M /= M.max()

def outlier_filter(A, min_sound_size):
    i = -1
    j = 0

    while j <= A.size:
        if j == A.size or A[j] == 0:
            if i != -1 and j - i < min_sound_size:
                A[i:j] = 0
            i = -1
        else:
            if i == -1:
                i = j
        j += 1

def supress_neighbours(M, K):
    M1 = np.zeros(M.shape)
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            neighbor1 = (i + 1)%len(M1)
            M1[i][j] = M[i][j] - (M[i - 1][j] + M[neighbor1][j])*K
            M1[i][j] = M1[i][j] if M1[i][j] > 0 else 0
    return M1

def get_range(A, i, j):
    return A[i:j]

def get_sounds_parts(A, min_sound_size):
    i = -1
    j = 0
    sounds = []

    while j < A.size:
        if A[j] == 0 or j == (A.size - 1):
            if i != -1 and j - i >= min_sound_size:
                sounds.append((i, j))
            i = -1
        else:
            if i == -1:
                i = j
        j += 1

    return sounds

def remove_gaps(A, min_sound_size, max_silence_size):
    sounds = get_sounds_parts(A, min_sound_size)

    for k in range(1, len(sounds)):
        silence_begin = sounds[k - 1][1]
        silence_end = sounds[k][0]

        if silence_end - silence_begin <= max_silence_size:
            sound = np.concatenate([get_range(A, *sounds[k - 1]), get_range(A, *sounds[k])])
            
            A[silence_begin:silence_end] = np.mean(sound)
