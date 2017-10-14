import unittest

from classes.JeanKen import JeanKen


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.jeanken = JeanKen()

    def tearDown(self):
        pass

    def test_player_choice_input_zero(self):
        with self.assertRaises(IndexError):
            self.jeanken.validatePlayerChoice(0)

        def test_player_choice_input_five(self):
            with self.assertRaises(IndexError):
                self.jeanken.validatePlayerChoice(5)

    def test_judge_draw(self):
        self.assertEqual(self.jeanken.judge(1, 1), 'draw')

    def test_judge_win_at_rock(self):
        self.assertEqual(self.jeanken.judge(1, 3), 'win')

    def test_judge_lose_at_rock(self):
        self.assertEqual(self.jeanken.judge(1, 2), 'lose')

    def test_judge_win_at_paper(self):
        self.assertEqual(self.jeanken.judge(2, 1), 'win')

    def test_judge_lose_at_paper(self):
        self.assertEqual(self.jeanken.judge(2, 3), 'lose')

if __name__ == '__main__':
    unittest.main()