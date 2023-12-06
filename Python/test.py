import os
"""
    The above Python code is a script that allows you to download a YouTube video by providing its URL,
    and it includes a progress bar to track the download progress.
    
    :param youtube_url: The `youtube_url` parameter is a string that represents the URL of the YouTube
    video that you want to download
"""
from pytube import YouTube
from tqdm import tqdm

# Create a directory for storing downloaded videos
download_dir = 'downloaded_videos'
os.makedirs(download_dir, exist_ok=True)

# Function to download a YouTube video with a progress bar


def download_video(youtube_url):
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()

        video_title = yt.title
        video_filename = os.path.join(download_dir, f"{video_title}.mp4")

        print(f"Downloading: {video_title}")
        with tqdm(total=stream.filesize, unit='B', unit_scale=True) as pbar:
            stream.download(output_path=download_dir, filename=video_title)
            pbar.update(stream.filesize)
        print(f"Downloaded: {video_title}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    youtube_url = input("Enter the YouTube URL: ")
    download_video(youtube_url)
