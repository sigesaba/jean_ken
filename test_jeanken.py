import unittest

from classes.JeanKen import JeanKen


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.jeanken = JeanKen()

    def tearDown(self):
        pass

    def test_player_choice_input_str(self):
        with self.assertRaises(ValueError):
            self.jeanken.set_player_choice("a")

    def test_player_choice_input_zero(self):
        with self.assertRaises(IndexError):
            self.jeanken.set_player_choice("0")

    def test_player_choice_input_five(self):
        with self.assertRaises(IndexError):
            self.jeanken.set_player_choice("5")

    def test_judge_draw(self):
        self.jeanken.set_player_choice("1")
        self.jeanken.judge(1)
        self.assertEqual(self.jeanken.result, 'draw')

    def test_judge_win_at_rock(self):
        self.jeanken.set_player_choice("1")
        self.jeanken.judge(3)
        self.assertEqual(self.jeanken.result, 'win')

    def test_judge_lose_at_rock(self):
        self.jeanken.set_player_choice("1")
        self.jeanken.judge(2)
        self.assertEqual(self.jeanken.result, 'lose')

    def test_judge_win_at_paper(self):
        self.jeanken.set_player_choice("2")
        self.jeanken.judge(1)
        self.assertEqual(self.jeanken.result, 'win')

    def test_judge_lose_at_paper(self):
        self.jeanken.set_player_choice("2")
        self.jeanken.judge(3)
        self.assertEqual(self.jeanken.result, 'lose')

if __name__ == '__main__':
    unittest.main()