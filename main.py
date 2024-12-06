# Theme Park Task

class Attraction(): 
    def __init__(self, name, capacity, status):
        self._name = name
        self._capacity = capacity
        self._status = status

    def getDetails(self): 
        print(f"Attraction: {self._name}, Capacity: {self._capacity}")
    
    def start(self): 
        if self._status == "Open": 
            print("The attraction is starting")
        elif self._status == "Closed": 
            print("The attraction is closed")
        else: 
            print("The status of the attraction cannot be established.")
    
    def openAttraction(self): 
        self._status = "Open"

    def closeAttraction(self): 
        self._status = "Closed"
    
class ThrillRide(Attraction): 
    def __init__(self, name, capacity,status, minHeight): 
        super().__init__(name, capacity, status)
        self._minHeight = minHeight
    
    def start(self): 
        if self._status == "Open": 
            print(f"Thrill Ride {self._name} is starting. Hold on tight!")
        elif self._status == "Closed": 
            print("The attraction is closed")
        else: 
            print("The status of the attraction cannot be established.")

    def isEligible(self, visitor): 
        if visitor._height >= self._minHeight: 
            return True
        else: 
            return False
              
class FamilyRide(Attraction): 
    def __init__(self, name, capacity, status, minAge): 
        super().__init__(name, capacity, status)
        self._minAge = minAge
    
    def start(self): 
        if self._status == "Open": 
            print(f"Family Ride {self._name} is now starting. Enjoy the fun!")
        elif self._status == "Closed": 
            print("The attraction is closed")
        else: 
            print("The status of the attraction cannot be established.")


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
        self._rideHistory = []

    def ride(self, attraction): 
        if attraction.isEligible(self) == True: 
            print(f"Visitor {self._name} is riding {attraction._name}")
            self._rideHistory.append(attraction._name)
        else: 
            print(f"Visitor {self._name} cannot ride this.")
    
    def viewHistory(self): 
        print(self._rideHistory)

class Manager(Staff): 
    def __init__(self, name, role): 
        super().__init__(name, role)
        self._team = []

    def addStaff(self, staff): 
        self._team.append(f"Name: {staff._name}, Role: {staff._role}")
    
    def getTeamSum(self): 
        print(self._team)

dragonCoaster = ThrillRide("Dragon Coaster", 20, " ", 140)
merryGoRound = FamilyRide("Merry-Go-Round", 30, " ", 4)
daniel = Visitor("Daniel", 3, 145)
daniel.ride(dragonCoaster)
daniel.ride(merryGoRound)
daniel.viewHistory()
dragonCoaster.openAttraction()
merryGoRound.openAttraction()
dragonCoaster.start()
merryGoRound.start()

parthiv = Staff("Parthiv", "Operator")
vahid = Staff("Vahid", "Gamer")
ali = Manager("Ali", "Manager")
ali.addStaff(parthiv)
ali.addStaff(vahid)
ali.getTeamSum()
