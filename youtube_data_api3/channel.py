import requests

from urllib.parse import urlsplit


def get_channel_code(url):
    """ Parse a Youtube Channel URL and get its code

    Example:
        https://www.youtube.com/channel/UC6gsueJf0YTIF3inlGKWLPg
        must return:
        UC6gsueJf0YTIF3inlGKWLPg
    """
    path = urlsplit(url).path
    parts = path.split("/")
    if "channel" not in parts:
        raise Exception('Invalid url "%s"' % url)
    channel_code = parts[-1]
    return channel_code


def fetch_channel_data(youtube_api_key, channel_code):
    channel_url = "https://www.googleapis.com/youtube/v3/channels"
    payload = {'id': channel_code,
               'part': 'snippet,contentDetails',
               'key': youtube_api_key}
    resp = requests.get(channel_url, params=payload)
    if resp.status_code != 200:
        raise Exception('Error fetching channel data "%s"' % resp.status_code)
    response_json = resp.json()
    channel_data = None
    if len(response_json["items"]) > 0:
        channel_data = response_json["items"][0]
    return channel_data
