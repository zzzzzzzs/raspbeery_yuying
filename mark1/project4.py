import os
os.system("arecord -D 'plughw:1' -f S16_LE -r 16000 -d 8 123.wav")