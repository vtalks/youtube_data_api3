import unittest
from unittest.mock import patch

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

    @patch("youtube_data_api3.video.fetch_video_data")
    def test_fetch_video_data(self, fake_fetch_video_data):
        # mock fetch video data
        fake_fetch_video_data.return_value = {
            "id": "fake_video_id",
            "snippet": {
                "channelId": "fake_channel_id",
                "title": "video title",
                "description": "video description",
                "publishedAt": "2012-10-01T15:27:35.000Z",
            },
            "statistics": {
                "viewCount": 20,
            },
            "contentDetails": {
                "duration": "PT1H46M12S",
            },
        }

        data = video.fetch_video_data("youtube_api_key", "fake_video_id")

        self.assertEqual(data["id"], fake_fetch_video_data.return_value["id"])


