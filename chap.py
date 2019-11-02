class Airlane():
    def __init__(self,make,model,year,maxspeed,odometr = 0):
        self.make = make 
        self.model = model 
        self.year = year 
        self.maxspeed = maxspeed
        self.odometr = odometr#0
        self.is_flying = False

    def take_off(self, is_flying):
        self.is_flying == True

    def land(self, is_flying):
        self.land == False

    def fly(self, km):
        self.odometr += km

    def print_arg(self):
        print(self.make, self.model, self.year, self.maxspeed)


air = Airlane("boing323", "444", "2019", "400")
air.print_arg()
air.take_off(True)
air.land(False)
air.fly(5000)
print(air.odometr)

