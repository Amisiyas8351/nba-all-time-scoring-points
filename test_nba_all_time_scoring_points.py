"""utilizing unittest to handle user inputs"""
import unittest
from unittest.mock import patch
from nba_all_time_scoring_points import get_avg_games_per_season, get_career_avg_points, get_first_season, get_info_total_points

"""testing the functions below from the "nba_all_time_scoring_points" module by utilizing a test case class"""
class TestNBAStats(unittest.TestCase):
    """testing the "get_avg_games_per_season" utilizing the "self" parameter"""
    def test_get_avg_games_per_season(self):
        self.assertEqual(get_avg_games_per_season("Anthony Davis"), 66)
        self.assertEqual(get_avg_games_per_season("Anthony Edwards"), 79.3)
        self.assertEqual(get_avg_games_per_season("Bam Adebayo"), 61.3)

    """testing the "get_career_avg_points" utilizing the "self" parameter"""
    def test_get_career_avg_points(self):
        self.assertEqual(get_career_avg_points("Anthony Davis"), 24)
        self.assertEqual(get_career_avg_points("Anthony Edwards"), 22)
        self.assertEqual(get_career_avg_points("Bam Adebayo"), 14)

    """testing the "get_first_season" utilizing the "self" parameter"""
    def test_get_first_season(self):
        self.assertEqual(get_first_season("Anthony Davis"), 2012)
        self.assertEqual(get_first_season("Anthony Edwards"), 2020)
        self.assertEqual(get_first_season("Bam Adebayo"), 2017)

    """testing the "get_info_total_points" utilizing the "self" parameter and utilzing mock inputs"""
    def test_get_info_total_points(self):
        with patch('builtins.input', side_effect = ['Anthony Davis', '2025', 'end', '7']):
            with patch('builtins.print') as mock_print:
                get_info_total_points()
                print_calls = mock_print.call_args_list
                self.assertGreater(len(print_calls), 1)

if __name__ == '__main__':
    unittest.main()

##Enter "python -m unittest test_nba_all_time_scoring_points" to test the program