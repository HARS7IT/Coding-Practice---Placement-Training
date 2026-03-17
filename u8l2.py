class Bike:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def _display_bike_details(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
a=Bike('Jawa','Perak','2015')
a._display_bike_details()