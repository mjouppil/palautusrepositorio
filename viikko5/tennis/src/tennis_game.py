class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            score = self._get_even_score(self.m_score1)
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self._get_endgame_score(self.m_score1, self.m_score2)
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score

    def _get_even_score(self, m_score):
        if m_score == 0:
            score = "Love-All"
        elif m_score == 1:
            score = "Fifteen-All"
        elif m_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score

    def _get_endgame_score(self, m_score1, m_score2):
        difference = m_score1 - m_score2
        state = "Advantage" if abs(difference) <= 1 else "Win for"
        player = "player1" if difference > 0 else "player2"
        score = " ".join([state, player])
        return score
