import numpy as np
import cv2
import time
import pyaudio
import wave
import ffmpeg
# The duration in seconds of the video captured
capture_duration = 10


# the file name output you want to record into
filename = "recorded.wav"
# set the chunk size of 1024 samples
chunk = 1024
# sample format
FORMAT = pyaudio.paInt16
# mono, change to 2 if you want stereo
channels = 1
# 44100 samples per second
sample_rate = 16000
record_seconds = 5
# initialize PyAudio object
p = pyaudio.PyAudio()
# open stream object as input & output
stream = p.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)
frames = []
vid = []
#data = stream.read(int(chunk/8))
cap = cv2.VideoCapture(0)




#data = stream.read(chunk+chunk//2)
start_time = time.time()
i=0
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    i+=1
    if ret==True:
        #out.write(frame)
        vid.append(frame)
        #cv2.imshow('frame',frame)
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        if(i%2==0):
            frames.append(data)

print(i)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, i*2/capture_duration, (640,480))

for i in vid:
    out.write(i)



print(time.time()-start_time)
cap.release()
out.release()
cv2.destroyAllWindows()



print("Finished recording.")
# stop and close stream
stream.stop_stream()
stream.close()
# terminate pyaudio object
p.terminate()
# save audio file
# open the file in 'write bytes' mode
wf = wave.open(filename, "wb")
# set the channels
wf.setnchannels(channels)
# set the sample format
wf.setsampwidth(p.get_sample_size(FORMAT))
# set the sample rate
wf.setframerate(sample_rate)
# write the frames as bytes
wf.writeframes(b"".join(frames))
# close the file
wf.close()


video = ffmpeg.input('output.avi')
audio = ffmpeg.input('recorded.wav')
out = ffmpeg.output(video, audio, '/home/shaashwatlobnikki/Desktop/PySync/vid.mp4', vcodec='copy', acodec='aac', strict='experimental')
out.run()