# Theme Park Task

class Attraction(): 
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity

    def getDetails(self): 
        print(f"Attraction: {self._name}, Capacity: {self._capacity}")
    
    def start(self): 
        print("The attraction is starting")
    
class ThrillRide(Attraction): 
    def __init__(self, name, capacity, minHeight): 
        super().__init__(name, capacity)
        self._minHeight = minHeight
    
    def start(self): 
        print(f"Thrill Ride {self._name} is starting. Hold on tight!")

    def isEligible(self, visitor): 
        if visitor._height >= self._minHeight: 
            return True
        else: 
            return False
              
class FamilyRide(Attraction): 
    def __init__(self, name, capacity, minAge): 
        super().__init__(name, capacity)
        self._minAge = minAge
    
    def start(self): 
        print(f"Family Ride {self._name} is now starting. Enjoy the fun!")

    def isEligible(self, visitor): 
        if visitor._age >= self._minAge: 
            return True
        else: 
            return False
        
class Staff(): 
    def __init__(self, name, role): 
        self._name = name
        self._role = role
    
    def work(self): 
        print(f"Staff {self._name} is performing their role: {self._role}")

class Visitor(): 
    def __init__(self, name, age, height): 
        self._name = name
        self._age = age
        self._height = height

    def ride(self, attraction): 
        if attraction.isEligible(self) == True: 
            print(f"Visitor {self._name} is riding {attraction._name}")
        else: 
            print(f"Visitor {self._name} cannot ride this.")
        
dragonCoaster = ThrillRide("Dragon Coaster", 20, 140)
merryGoRound = FamilyRide("Merry-Go-Round", 30, 4)
daniel = Visitor("Daniel", 3, 130)
daniel.ride(dragonCoaster)
daniel.ride(merryGoRound)
dragonCoaster.start()
merryGoRound.start()