import unittest
import requests_mock

from youtube_data_api3 import playlist


class PlaylistTest(unittest.TestCase):

    def test_playlist_code(self):
        url = "https://www.youtube.com/playlist?list=PLDWZ5uzn69eyM81omhIZLzvRhTOXvpeX9"
        expected_code = "PLDWZ5uzn69eyM81omhIZLzvRhTOXvpeX9"
        playlist_code = playlist.get_playlist_code(url)
        self.assertEqual(expected_code, playlist_code)

    def test_playlist_code_fail(self):
        url = "invalid_url"
        with self.assertRaises(Exception) as context:
            playlist.get_playlist_code(url)

        self.assertTrue('Invalid url "invalid_url"' in str(context.exception))

    def test_fetch_playlist_data(self):
        with requests_mock.Mocker() as m:
            fake_playlist_video_data = {
              "kind": "youtube#playlistListResponse",
              "etag": "etag",
              "nextPageToken": "next_page_token",
              "prevPageToken": "prev_page_token",
              "pageInfo": {
                "totalResults": 10,
                "resultsPerPage": 10,
              },
              "items": [
                  {
                      "id": "fake_playlist_id",
                      "snippet": {
                          "title": "playlist title",
                          "description": "playlist description",
                          "publishedAt": "2012-10-01T15:27:35.000Z",
                      }
                  },
              ]
            }
            m.get('https://www.googleapis.com/youtube/v3/playlists', json=fake_playlist_video_data)

            data = playlist.fetch_playlist_data("youtube_api_key", "fake_playlist_id")

            self.assertEqual(data["id"], fake_playlist_video_data["items"][0]["id"])
