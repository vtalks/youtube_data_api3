import unittest
from unittest.mock import patch

from youtube_data_api3 import channel


class ChannelTest(unittest.TestCase):

    def test_channel_code(self):
        url = "https://www.youtube.com/channel/UC_BzFbxG2za3bp5NRRRXJSw"
        expected_code = "UC_BzFbxG2za3bp5NRRRXJSw"
        channel_code = channel.get_channel_code(url)
        self.assertEqual(expected_code, channel_code)

    def test_channel_code_fail(self):
        url = "invalid_url"
        with self.assertRaises(Exception) as context:
            channel.get_channel_code(url)

        self.assertTrue('Invalid url "invalid_url"' in str(context.exception))

    @patch("youtube_data_api3.channel.fetch_channel_data")
    def test_fetch_channel_data(self, fake_fetch_channel_data):
        # mock fetch channel data
        fake_fetch_channel_data.return_value = {
            "id": "fake_channel_id",
            "snippet": {
                "title": "channel title",
                "description": "channel description",
                "publishedAt": "2012-10-01T15:27:35.000Z",
            },
            "contentDetails": {
                "duration": "PT1H46M12S",
            },
        }

        data = channel.fetch_channel_data("youtube_api_key", "fake_channel_id")

        self.assertEqual(data["id"], fake_fetch_channel_data.return_value["id"])