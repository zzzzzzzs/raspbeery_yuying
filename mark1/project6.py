import pyaudio
import wave
import os
from aip import AipSpeech
""" 你的 APPID AK SK """
APP_ID = '18705456'
API_KEY = 'YRq2K4CDQ2ROGVY3qrZVjSt0'
SECRET_KEY = 'GhVVnwbNhfgGAD0ImAgBAr63C4XONKZi'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
os.system("arecord -D 'plughw:1' -f S16_LE -r 16000 -d 8 123.wav")



p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)



frames = []
def fun():
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件 1536下架，换1537
a = client.asr(get_file_content('123.wav'), 'wav', 16000, {
    'dev_pid': 1537,
})
print(a)
