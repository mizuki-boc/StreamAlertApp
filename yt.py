from apiclient.discovery import build
from apiclient.errors import HttpError

if __name__ == "__main__":
    # API情報
    DEVELOPER_KEY = ""
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    JUN_CHANNEL_ID = "UCx1nAvtVDIsaGmCMSe8ofsQ"

    test_lofi = "UClFyIegrk4g6CFqGYCwTViA"

    youtube = build(
        YOUTUBE_API_SERVICE_NAME, 
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
        )

    search_response = youtube.search().list(
    q="[]",
    part="id,snippet",
    type='video',
    channelId=test_lofi
    ).execute()

    print(search_response)

    # AIzaSyCa82nI3eTXVDEVbchHFFOkf4haU7sIQJo