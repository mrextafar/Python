from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        yt.use_oauth = True
        yt.allow_oauth_cache = True
        
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Everything got right")
    except Exception as e:
        print("Everything got wrong", str(e))

video_url = input("url please: ")
download_video(video_url)