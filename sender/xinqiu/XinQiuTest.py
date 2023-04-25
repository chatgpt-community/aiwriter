import unittest
from XinQiu import XinQiu


class TestXinQiu(unittest.TestCase):

    def test_send_successful(self):
        event = {'content': 'marvin third testing'}
        sender = XinQiu()
        sender.send(event)


if __name__ == '__main__':
    unittest.main()