from pytube import YouTube
import sys
import os
def internal_youtube_routine(endpoint):
    try:
        yt_obj=YouTube(endpoint)
        print(yt_obj)
        internal_stream = yt_obj.streams.filter(only_audio=True,file_extension="webm")[-1]
        print("downloading")
        filename=internal_stream.download()
        #print(filename)
        new_filename=filename[:len(filename)-5]+".mp3"
        #print(new_filename)
        os.rename(filename,filename[:len(filename)-5]+".mp3")
        print("internal download complete")
        return new_filename

        
    except Exception as e:
        print(e)
        return False


