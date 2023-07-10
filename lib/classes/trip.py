
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        
        self.national_park.trips(self)
        self.national_park.visitors(self.visitor)
        self.visitor.trips(self)
        self.visitor.national_parks(self.national_park)
        