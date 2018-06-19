import unittest

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
