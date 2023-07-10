class Visitor:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception
        self._name = name
        self._trips = []
        self._national_parks = []

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        raise Exception("Cannot change the name of the visitor")

    name = property(get_name, set_name)

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips

    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark

        if (
            new_national_park 
            and isinstance(new_national_park, NationalPark) 
            and new_national_park not in self._national_parks
        ):
            self._national_parks.append(new_national_park)
        return self._national_parks
