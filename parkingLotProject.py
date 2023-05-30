tickets=[i for i in range(10)]
parkingSpaces=[i for i in range(10)]
currentTicket={False}
currentTicketCount={}


class Parking():

    def __init__(self, tickets, parkingSpace):
        self.tickets = tickets
        self.parkingSpace = parkingSpace
        self.currentTicket = {'paid':False, 'ticketNumber': None, 'parkingspace': None }

    
    def take_ticket(self):
        if len(self.tickets) > 0 or len(self.parkingSpace) > 0:
            self.currentTicket['ticketNumber'] = self.tickets.pop()
            self.currentTicket['parkingspace'] = self.parkingSpace.pop()
            print(f"ticket number {self.currentTicket['ticketNumber']} has been assaigned to you")
        else:
            print('no avilable tickets or parking space !')
           
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
    def pay_parking(self):
        payment = input(f"Welcome to sustainable pavement car parking."
                        f"It is $1.00 for 15 mins or parking, select space to continue." 
                        f"If you wish to end press 'q'. ")
        if payment != '' and payment.lower() != 'q':
            print('Your ticket has been paid, you have 15 minutes to leave, thank you....')
            self.currentTicket['paid'] = True
        elif payment.lower() == 'q':
            return
        else:
            print("Your ticket hasn't been paid")
            
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display
#   a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
    def leave_garage(self):
        while self.currentTicket['paid'] is False:
            self.pay_parking()
        self.tickets.append(self.currentTicket['ticketNumber'])
        self.parkingSpace.append(self.currentTicket['parkingspace'])
        print('Thank you have a nice day')

if __name__ == '__main__':
    parking = Parking(tickets, parkingSpaces)
    parking.take_ticket()
    parking.pay_parking()
    parking.leave_garage()