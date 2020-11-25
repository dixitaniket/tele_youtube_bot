from pytube import YouTube
import sys
endpoint=sys.argv[1]
try:
    yt_obj=YouTube(endpoint)
    internal_stream = yt_obj.streams.filter(only_audio=True,file_extension="webm")[-1]
    print(internal_stream)
    internal_stream.download("/home/aniket/Music")
except Exception as e:
    print(e)

print("thanks for using the service")


