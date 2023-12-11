from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    print()

    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    print()
    print('HasFewerThan')
    for player in stats.matches(matcher):
        print(player)

    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    print()
    print('Not')
    for player in stats.matches(matcher):
        print(player)

    # Jonny Brodzinski     NYR          1  + 1  = 2
    # Ben Harpur           NYR          1  + 5  = 6
    # Ryan Carpenter       NYR          1  + 2  = 3
    # Ryan Lindgren        NYR          1  + 17 = 18
    # Libor Hajek          NYR          1  + 0  = 1
    # Zac Jones            NYR          1  + 1  = 2
    # Will Cuylle          NYR          0  + 0  = 0
    # Jaroslav Halak       NYR          0  + 0  = 0
    # Igor Shesterkin      NYR          0  + 0  = 0

    print()
    print('All')
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    # 1058

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    print()
    print('Or')
    for player in stats.matches(matcher):
        print(player)

    # David Pastrnak       BOS          61 + 52 = 113
    # Tage Thompson        BUF          47 + 47 = 94
    # Nikita Kucherov      TBL          30 + 83 = 113
    # Brayden Point        TBL          51 + 44 = 95
    # Mikko Rantanen       COL          55 + 50 = 105
    # Leon Draisaitl       EDM          52 + 76 = 128
    # Connor McDavid       EDM          64 + 89 = 153
    # Jason Robertson      DAL          46 + 63 = 109
    # Erik Karlsson        SJS          25 + 76 = 101

    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    print()
    print('Or and many more')
    for player in stats.matches(matcher):
        print(player)

    # Mika Zibanejad       NYR          39 + 52 = 91
    # Artemi Panarin       NYR          29 + 63 = 92
    # Adam Fox             NYR          12 + 60 = 72
    # David Pastrnak       BOS          61 + 52 = 113
    # Carter Verhaeghe     FLA          42 + 31 = 73
    # Aleksander Barkov    FLA          23 + 55 = 78
    # Brandon Montour      FLA          16 + 57 = 73
    # Matthew Tkachuk      FLA          40 + 69 = 109

    query = QueryBuilder()

    matcher = (
      query
      .playsIn("NYR")
      .hasAtLeast(10, "goals")
      .hasFewerThan(20, "goals")
      .build()
    )

    print()
    print('QueryBuilder1 - AND')
    for player in stats.matches(matcher):
        print(player)

    # Barclay Goodrow      NYR          11 + 20 = 31
    # Jimmy Vesey          NYR          11 + 14 = 25
    # Adam Fox             NYR          12 + 60 = 72
    # Kaapo Kakko          NYR          18 + 22 = 40
    # Alexis Lafrenière    NYR          16 + 23 = 39

    matcher = (
        query.oneOf(query
                    .playsIn("PHI")
                    .hasAtLeast(10, "assists")
                    .hasFewerThan(5, "goals")
                    .build(),
                    query.playsIn("EDM")
                    .hasAtLeast(50, "points")
                    .build()
                    )
        .build()
    )

    print()
    print('QueryBuilder2 - OR')
    for player in stats.matches(matcher):
        print(player)

    # Nick Seeler          PHI          4  + 10 = 14
    # Rasmus Ristolainen   PHI          3  + 17 = 20
    # Cam York             PHI          2  + 18 = 20
    # Tyson Barrie         EDM          13 + 42 = 55
    # Zach Hyman           EDM          36 + 47 = 83
    # Ryan Nugent-Hopkins  EDM          37 + 67 = 104
    # Leon Draisaitl       EDM          52 + 76 = 128
    # Connor McDavid       EDM          64 + 89 = 153

if __name__ == "__main__":
    main()
