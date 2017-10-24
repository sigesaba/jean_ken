import unittest

from classes.Recorder import Recorder
from classes.JeanKen import JeanKen


class TestWinLossRecordMethods(unittest.TestCase):

    def setUp(self):
        self.recorder = Recorder(10)
        self.jeanken = JeanKen()

    def tearDown(self):
        pass

    def test_count_win_loss_record(self):
        self.recorder.record_win_loss(self.jeanken.gestures, 'win', 1, 3)
        self.recorder.record_win_loss(self.jeanken.gestures, 'lose', 1, 2)
        self.recorder.record_win_loss(self.jeanken.gestures, 'draw', 1, 1)
        self.assertEqual(len(self.recorder.win_loss), 3)
        ave = '{winning_ave:.1%}'.format(winning_ave=self.recorder.getWinningAve(self.recorder.played, self.recorder.won))
        self.assertEqual('33.3%', ave)

    def test_count_win_loss_record_fail(self):
        with self.assertRaises(TypeError):
            self.recorder.record_win_loss('win', 1)

    def test_play_times_limit(self):
        self.recorder.record_win_loss(self.jeanken.gestures, 'win', 1, 3)
        self.recorder.record_win_loss(self.jeanken.gestures, 'lose', 1, 2)
        self.recorder.record_win_loss(self.jeanken.gestures, 'draw', 1, 1)
        self.recorder.record_win_loss(self.jeanken.gestures, 'win', 1, 3)
        self.recorder.record_win_loss(self.jeanken.gestures, 'lose', 1, 2)
        self.recorder.record_win_loss(self.jeanken.gestures, 'draw', 1, 1)
        self.recorder.record_win_loss(self.jeanken.gestures, 'win', 1, 3)
        self.recorder.record_win_loss(self.jeanken.gestures, 'lose', 1, 2)
        self.recorder.record_win_loss(self.jeanken.gestures, 'draw', 1, 1)
        self.assertFalse(self.recorder.has_reached_to_play_limit())
        self.recorder.record_win_loss(self.jeanken.gestures, 'win', 1, 3)
        self.assertTrue(self.recorder.has_reached_to_play_limit())

if __name__ == '__main__':
    unittest.main()