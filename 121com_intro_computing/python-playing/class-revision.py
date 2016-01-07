class MyHotel:
    
    hotelId = 0

    def __init__(self, n, r):
        self.name = n
        self.rooms = r
        self.bookedRooms = 0
        MyHotel.hotelId += 1

    def makeBooking(self, name, length, date):
        if (self.rooms - self.bookedRooms) > 0:
            self.bookedRooms += 1
            print("A room at " + self.name + " has been booked in the name of "
                    + name + ' for ' + str(length) + ' nights on ' + date + '. ' +
                    str(self.rooms - self.bookedRooms) + " more rooms are available.")
        else:
            print("No rooms are available")


hotel1 = MyHotel('The Greenbridge', 234)
hotel1.makeBooking('Prince', 2, '11/04/2016')
