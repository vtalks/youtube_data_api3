import unittest
from unittest.mock import patch

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

    @patch("youtube_data_api3.playlist.fetch_playlist_data")
    def test_fetch_playlist_data(self, fake_fetch_playlist_data):
        # mock fetch playlist data
        fake_fetch_playlist_data.return_value = {
            "id": "fake_playlist_id",
            "snippet": {
                "title": "playlist title",
                "description": "playlist description",
                "publishedAt": "2012-10-01T15:27:35.000Z",
            }
        }

        data = playlist.fetch_playlist_data("youtube_api_key", "fake_playlist_id")

        self.assertEqual(data["id"], fake_fetch_playlist_data.return_value["id"])
