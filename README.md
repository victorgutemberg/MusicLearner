# Music Learner

This project aims to teach anyone to play the piano (or keyboard) through example.
The idea of the project is to extract the chords from existing musics that you want to learn how to play.

First, run the extract_chords script which will extract the chords played throughout the music and save them into a chords.info file.

`python extract_chords.py <path to the audio file>`

Then, you can use the chord_reader to show via LED which keys to play at each time.

`python chord_reader.py`

There is an extra script called chord_recognition that shows a graphical analysis of a chrod.

`python chord_recognition.py <path to the audio file>`

## Installing dependencies

To install the dependencies, simply run `pip install -r requirements.txt`.
