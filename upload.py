from instagrapi import Client
import time

def post_video_with_caption(session_id, video_path, caption):
    """
    Posts a video to Instagram with a caption using the provided session ID.
    """
    # Initialize the Instagram client
    cl = Client()

    try:
        # Login using the session ID
        cl.login_by_sessionid(session_id)

        # Upload the video
        print("Uploading video...")
        video = cl.video_upload(video_path, caption=caption)
        print("Video posted successfully!")
        print(f"Video URL: https://www.instagram.com/p/{video.code}/")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Logout to clear the session
        cl.logout()


if __name__ == "__main__":
    # Replace these values with your own
    SESSION_ID = "64772357342%3Ax9gYGSvWSs6WSN%3A29%3AAYentzz1O-jtJ6u0SnUmOHnJFmgCGXq9Q72xZQnZcA"  # Your Instagram session ID
    VIDEO_PATH = "video.mp4"  # Path to the video file
    CAPTION = "This is a test video posted using instagrapi! 🎥"  # Caption for the video

    # Post the video with a delay to avoid detection
    print("Starting video upload process...")
    time.sleep(2)  # Initial delay to mimic human behavior
    post_video_with_caption(SESSION_ID, VIDEO_PATH, CAPTION)
