import ffmpeg

video = ffmpeg.input('output.avi')
print(video)
audio = ffmpeg.input('recorded.wav')
out = ffmpeg.output(video, audio, '/home/shaashwatlobnikki/Desktop/PySync/vid.mp4', vcodec='copy', acodec='aac', strict='experimental')
out.run()