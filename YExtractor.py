import youtube_dl
from YVideo import YVideo


def Get_Videos(url):
    '''
    Get all youtube videos from given url
    Output: YVideo List (see YVideo.py for more info)
    '''

    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            url,
            download=False
        )

    videos = []

    if 'entries' in result:
        # playlistm channel or list of videos
        for entry in result['entries']:
            videos.append( 
                YVideo(
                    entry['title'],
                    entry['id']
                    )
                )
    else:
        # Just a video
        videos.append( 
                YVideo(
                    result['title'],
                    result['id']
                    )
                )

    return videos
