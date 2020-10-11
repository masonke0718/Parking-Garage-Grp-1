
class ParkingGarage():
    def __init__(self,tickets,parkingSpaces,currentTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTickets = currentTickets
    def enteringGarage(self):
        lok = len(list(self.currentTickets.keys()))
        lot = len(self.tickets)
        if lok == lot:
            print("Garage full")
        elif lok != lot:
            poped = self.tickets.pop()
            print(f"Welcome to our Garage.  Here's your ticket #: {poped}")
            self.currentTickets[poped] = ""
            self.parkingSpaces.pop()
    def exitingGarage(self):
        exitTicketNumber = int(input("What's your ticket #? Or type 'quit' to exit: "))
        for currentTicket in list(self.currentTickets.keys()):
           if currentTicket == exitTicketNumber:
                pay = input("We found your ticket. Please pay now by typing 'pay' or type 'quit' to exit.")
                if pay.lower() == 'pay':
                    self.currentTickets[currentTicket] = "Paid"   # Updating Status of dictionary to paid
                    self.currentTickets.pop(currentTicket)
                    self.tickets.append(currentTicket)
                    self.parkingSpaces.append(currentTicket)
                    print("Thank You. Have a nice day!")
                elif pay.lower() == 'quit':
                    print("That's fine.  But you're now stuck in the garage. Get comfortable")
                    break
                
        if exitTicketNumber != currentTicket:
                    print("Sorry, we could not find that ticket number")
                    
        
parking = ParkingGarage([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],{})  #INSTANTIATING here
def run():
    while True:
        response = input("Are you entering, exiting or quit(to leave screen)?")
        if response.lower() == 'quit':
            print("Thanks for stopping by")
            break
        if response.lower() == 'entering':
            parking.enteringGarage()
        if response.lower() == 'exiting':
            parking.exitingGarage()
run()  
