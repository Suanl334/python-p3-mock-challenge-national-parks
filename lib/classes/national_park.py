class NationalPark:
    def __init__(self, name=""):
        if not isinstance(name, str):
            raise Exception
        self._name = name
        self._trips = []
        self._visitors = []
        self._total_visits = 0
        self._best_visitor = []

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        raise Exception("Cannot change the name of the NationalPark")

    name = property(get_name, set_name)

    def trips(self, new_trip=None):
        from classes.trip import Trip

        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
            self._total_visits += 1
        return self._trips

    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor

        if (
            new_visitor
            and isinstance(new_visitor, Visitor)
            and new_visitor not in self._visitors
        ):
            self._visitors.append(new_visitor)
            self._best_visitor.append(0)
            self._best_visitor[self._visitors.index(new_visitor)] += 1
        elif new_visitor in self._visitors:
            self._best_visitor[self._visitors.index(new_visitor)] += 1
        return self._visitors

    def total_visits(self):
        return self._total_visits

    def best_visitor(self):
        return self._visitors[self._best_visitor.index(max(self._best_visitor))]
