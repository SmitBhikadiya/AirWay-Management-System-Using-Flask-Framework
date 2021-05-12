class Flight:
    counter = 0
    def __init__(self, origin, destination, timeDuration, timeTakeoff, timeLanding):
        self.origin = origin
        self.destination = destination
        self.timeDuration = timeDuration
        self.timeTakeoff = timeTakeoff
        self.timeLanding = timeLanding
        self.id = Flight.counter
        Flight.counter += 1
        self.passengers = []
    
    def delay(self,timeDuration):
        self.timeDuration += timeDuration

    def add_passengers(self,p):
        p.flight_id = self.id
        self.passengers.append(p)

    def find_passengers(self,p):
        if p in self.passengers:
            print(f"\nPassenger is found!\nPassenger name : {p.name}")
        else:
            print("\nPassenger is not find on this flight")

    def print_info(self):
        print(f"Flight Origin : {self.origin}")
        print(f"Flight Destination : {self.destination}")
        print(f"Flight timeDuration : {self.timeDuration}")

        # pasengers list
        print("Passengers on Flights ")
        for passenger in self.passengers:
            print(f"{passenger.name}")

class Passenger:
    def __init__(self,name,passport_id,dob,mobile_no,email,address,gender,country):
        self.name = name
        self.passport_id = passport_id
        self.dob = dob
        self.mobile_no = mobile_no
        self.email = email
        self.address = address
        self.gender = gender
        self.country = country

def main():
    flight1 = Flight(origin="Mumbai",destination="Delhi",timeDuration=540,timeTakeoff="3:10 PM IST",timeLanding="1:00 AM IST")
    flight2 = Flight(origin="Kolkata",destination="Ahemedabad",timeDuration=359,timeTakeoff="9:00 AM IST",timeLanding="3:30 PM IST")
    #flight3 = Flight(origin="Hydrabad",destination="Delhi",timeDuration=300,timeTakeoff="5:00 AM IST",timeLanding="9:30 PM IST")
    #flight4 = Flight(origin="Surat",destination="Goa",timeDuration=200,timeTakeoff="1:00 PM IST",timeLanding="2:30 PM IST")
    #flight5 = Flight(origin="Kolkata",destination="Hariyana",timeDuration=500,timeTakeoff="3:00 PM IST",timeLanding="10:30 PM IST")
    #flight6 = Flight(origin="Delhi",destination="Vadodara",timeDuration=530,timeTakeoff="7:00 AM IST",timeLanding="3:59 PM IST")

    # create a passenger
    Smit = Passenger(name="Smit",passport_id="PID1234",dob="28/01/2001",mobile_no="7096794624",email="sbhikadiya892@rku.ac.in",address="malinivadi, gadhadaroad, Botad 364710",gender="Male",country="India")

    # add paasenger
    flight1.add_passengers(Smit)

    #get information 
    #flight1.print_info()
    #flight2.print_info()

    #find perticuler passengert on perticuler flights
    #flight1.find_passengers(Pujan)

if __name__ == "__main__":
    main()