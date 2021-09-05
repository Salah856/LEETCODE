class ParkingSystem(object):

    def __init__(self, big, medium, small):
	    self.data = {1: big, 2: medium, 3: small}

    def addCar(self, carType):
        if self.data[carType]:
            self.data[carType] -= 1
            return True
        else:
            return False 
