from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("sample.mp4")
videoClip.write_gif("my_gif.gif")
print("GIF saved!")
