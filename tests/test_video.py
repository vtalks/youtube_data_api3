import unittest

from youtube_data_api3 import video


class VideoTest(unittest.TestCase):

    def test_video_code(self):
        url = "https://www.youtube.com/watch?v=5UG57xQL_RE&t="
        expected_code = "5UG57xQL_RE&t="
        video_code = video.get_video_code(url)
        self.assertEqual(expected_code, video_code)
