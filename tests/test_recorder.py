import unittest

from classes.Recorder import Recorder


class TestWinLossRecordMethods(unittest.TestCase):

    def setUp(self):
        self.recorder = Recorder()

    def tearDown(self):
        pass

    def test_count_win_loss_record(self):
        self.recorder.record_win_loss('win', 1, 3)
        self.recorder.record_win_loss('lose', 1, 2)
        self.recorder.record_win_loss('draw', 1, 1)
        self.assertEqual(len(self.recorder.win_loss), 3)


if __name__ == '__main__':
    unittest.main()