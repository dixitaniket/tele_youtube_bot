from pytube import YouTube
import sys
def internal_youtube_routine(endpoint):
    try:
        yt_obj=YouTube(endpoint)
        print(yt_obj)
        internal_stream = yt_obj.streams.filter(only_audio=True,file_extension="webm")[-1]
        
        print("downloading")
        internal_stream.download()
        return yt_obj.title
        
    except Exception as e:
        print(e)
        return False


