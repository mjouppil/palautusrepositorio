class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value >= self._value


class All:
    def __init__(self):
        pass

    def test(self, player):
        return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        player_res = not self._matcher.test(player)
        return player_res


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            # print(matcher)
            if matcher.test(player):
                return True

        return False


class QueryBuilder:
    def __init__(self, query_list=None, query=None):
        if not query_list:
            self._query = []
        else:
            self._query = query_list
        if not query:
            self._query.append(All())
        else:
            self._query.append(query)

    def build(self):
        ret = And(*self._query)
        return ret

    def playsIn(self, team):
        return QueryBuilder(self._query, PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._query, HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._query, HasFewerThan(value, attr))

    def oneOf(self, *queries):
        ret = QueryBuilder(None, Or(*queries))
        return ret
