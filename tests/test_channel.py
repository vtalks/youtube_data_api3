import unittest

from youtube_data_api3 import channel


class ChannelTest(unittest.TestCase):

    def test_channel_code(self):
        url = "https://www.youtube.com/channel/UC_BzFbxG2za3bp5NRRRXJSw"
        expected_code = "UC_BzFbxG2za3bp5NRRRXJSw"
        channel_code = channel.get_channel_code(url)
        self.assertEqual(expected_code, channel_code)
