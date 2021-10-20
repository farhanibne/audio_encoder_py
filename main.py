import movie.editor as mp
clip = mp.VideoFilterClip('video.mp4')
clip.audio.write_audio_file('audio.mp3')