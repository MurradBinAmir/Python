class planet:
    def __init__(self):
        self.gravity = None
        self.temperature = None
        self.name = "Planet"
    

class mercury(planet):
    def __init__(self):
        self.name = "mercury"
        self.gravity = 3.7
        self.temperature = 167
class venus(planet):
    def __init__(self):
        self.name = "venus"
        self.gravity = 8.9
        self.temperature = 464

class  earth(planet):
    def __init__(self):
        self.name = "earth"
        self.gravity = 9.8
        self.temperature = 15

class mars(planet):
    def __init__(self):
        self.name = "mars"
        self.gravity = 3.7
        self.temperature = -65

class jupiter(planet):
    def __init__(self):
        self.name = "jupyter"
        self.gravity = 23.1
        self.temperature = -110

class saturn(planet):
    def __init__(self):
        self.name = "saturn"
        self.gravity = 9
        self.temperature = -140

class uranus(planet):
    def __init__(self):
        self.name = "uranus"
        self.gravity = 8.7
        self.temperature = -195

class neptune(planet):
    def __init__(self):
        self.name = "naptune"
        self.gravity = 11
        self.temperature = -200

class spaceCraft:
        mercury = mercury()
        venus = venus()
        earth = earth()
        mars = mars()
        jupiter = jupiter()
        saturn = saturn()
        uranus = uranus()
        neptune = neptune()
    
        planet_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

        for planet in planet_list:
            # 
            if -15<= planet.temperature <= 35 and 7.84<=planet.gravity <= 11.76:
                print(f"{planet.name} is habitable.")
            else:
                print(f"{planet.name} is not habitable.")
