import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class PlayerMatcher:
    expected: Player

    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, other):
        return self.expected.name == other.name and self.expected.team == other.team and self.expected.goals == other.goals and self.expected.assists == other.assists
               
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_exist(self):
        answer = PlayerReaderStub().get_players()[2]
        pl = self.stats.search("Kurri")
        self.assertEqual(PlayerMatcher(pl), answer)

    def test_search_no_exist(self):
        pl = self.stats.search("Loiri")
        self.assertEqual(pl, None)

    def test_team(self):
        answer = [
            PlayerReaderStub().get_players()[0],
            PlayerReaderStub().get_players()[2],
            PlayerReaderStub().get_players()[4]
        ]
        pls = self.stats.team("EDM")
        self.assertEqual(len(answer), len(pls))
        for i in range(len(answer)):
            self.assertEqual(PlayerMatcher(pls[i]), answer[i])

    def test_top(self):
        answer = [
            PlayerReaderStub().get_players()[4],
            PlayerReaderStub().get_players()[1],
            PlayerReaderStub().get_players()[3]
        ]
        pls = self.stats.top(2)
        self.assertEqual(len(answer), len(pls))
        for i in range(len(answer)):
            self.assertEqual(PlayerMatcher(pls[i]), answer[i])



