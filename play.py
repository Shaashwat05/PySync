import vlc
import time

file = 'vid.mp4'


instance = vlc.Instance()
media = instance.media_new(file)

player = vlc.MediaPlayer()
player.set_media(media)
player.play() 


still_playing = True
time.sleep(0.5) # Wait for players to start

while still_playing:
    time.sleep(1)

    if player.is_playing():
        continue
    else:
        still_playing = False


