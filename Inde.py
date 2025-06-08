import os
import yt_dlp

# download the Instagram vedio with just link of instagram 
# Single Vedio at a time 
def download_instagram_video(url, output_path='F:/INSTA'):
    # Ensure output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # yt-dlp download options
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,
        'format': 'mp4',
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("✅ Download completed and saved to F:\\INSTA\n")
        except Exception as e:
            print(f"❌ Failed to download: {e}\n")

if __name__ == "__main__":
    print("📥 Instagram Video Downloader")
    print("Type 'exit' to quit.\n")

    while True:
        instagram_url = input("Enter Instagram video URL: ").strip()
        if instagram_url.lower() == "exit":
            print("👋 Exiting program. Goodbye!")
            break
        download_instagram_video(instagram_url)
