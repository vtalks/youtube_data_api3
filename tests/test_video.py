import unittest

from youtube_data_api3 import video


class VideoTest(unittest.TestCase):

    def test_video_code(self):
        url = "https://www.youtube.com/watch?v=5UG57xQL_RE"
        expected_code = "5UG57xQL_RE"
        video_code = video.get_video_code(url)
        self.assertEqual(expected_code, video_code)

    def test_video_code_fail(self):
        url = "invalid_url"
        with self.assertRaises(Exception) as context:
            video.get_video_code(url)

        self.assertTrue('Invalid url "invalid_url"' in str(context.exception))
