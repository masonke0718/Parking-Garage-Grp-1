class ParkingGarage():
    def __init__(self,tickets,parkingSpaces,currentTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTickets = currentTickets
    def enteringGarage(self):
        if self.tickets == []:
            print("Garage full")
        elif self.tickets !=[]:
            poped = self.tickets.pop()
            print(f"Welcome to our Garage.  Here's your ticket #: {poped}")
            self.currentTickets[poped] = ""
            self.parkingSpaces.pop()
    def exitingGarage(self):
        exitTicketNumber = int(input("What's your ticket #? "))
        if exitTicketNumber in list(self.currentTickets.keys()):
            print("We found your ticket.")
        else:
            print("Sorry, we could not find that ticket number") 
        for currentTicket in list(self.currentTickets.keys()):
            if currentTicket == exitTicketNumber:
                pay = input("Please pay now by typing 'pay' or type 'quit' to exit.")
                if pay.lower() == 'pay':
                    self.currentTickets[currentTicket] = "Paid"   # Updating Status of dictionary to paid
                    self.currentTickets.pop(currentTicket)
                    self.tickets.append(currentTicket)
                    self.parkingSpaces.append(currentTicket)
                    print("Thank You. You have 15 minutes to exit the garage. Have a nice day!")
                elif pay.lower() == 'quit':
                    print("That's fine.  But you're now stuck in the garage. Get comfortable")
                    break
                elif currentTicket != exitTicketNumber:
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
