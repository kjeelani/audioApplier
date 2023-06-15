from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import argparse

def applyAudio(video_path, audio_path, offset=0, gain=1):
    video_input = VideoFileClip(video_path)
    audio_input = AudioFileClip(audio_path).volumex(gain).subclip(offset, video_input.end)
    processed_video = video_input.set_audio(audio_input)
    processed_video.write_videofile("final.mp4")


parser = argparse.ArgumentParser(description="Python script to add audio to video clip")
parser.add_argument("-v", "--video-file", help="Target video file")
parser.add_argument("-a", "--audio-file", help="Target audio file to embed with the video")
parser.add_argument("-o", "--offset", help="Start duration of the audio file, default is 0", default=0, type=int)
parser.add_argument("-g", "--amplification", type=float, default=1.0, help="The volume factor to multiply by the volume of the audio file, 1 means no change, below 1 will decrease volume, above will increase.")

args = parser.parse_args()

applyAudio(args.video_file, args.audio_file)