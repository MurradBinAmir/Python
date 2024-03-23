class Vehicle():
    def __init__(self):
        self.Vehicle_type =  "Vehicle"
        
    def brake(self):
        print(f"{str(self.Vehicle_type)} is Braking")
        

class car(Vehicle):
    def  __init__(self):
        self.Vehicle_type="car"

class bike(Vehicle):
    def __init__(self):
        self.Vehicle_type= "bike"
class plane(Vehicle):
    def __init__(self):
        self.Vehicle_type= "plane"
    def brake(self):
        print(f"{str(self.Vehicle_type)} is Landing")


driveVehical = Vehicle().brake()
driveCar =  car().brake()
driveBike =  bike().brake()
drivePalne = plane().brake()
