class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()

    def _sort_by_points(self, pl):
        return pl.points

    def top_scorers_by_nationality(self, country):
        players_by_country = [pl for pl in self.players if pl.nationality == country]
        players_by_country.sort(key=self._sort_by_points, reverse=True)
        return players_by_country
