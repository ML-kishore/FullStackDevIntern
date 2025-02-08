class TicketBooking():

    stop_transaction = False
    max_attempts = 5

    def seat_book(self,seats):
        ticket = 125
        amount = ticket*seats
        return amount
    
    def payment(self,money):
        return self.money

    
    def login(self):

        attempts = self.max_attempts
        stop_transaction = self.stop_transaction

        while attempts !=0 and stop_transaction == False:

            user_name = input('Enter the username :')
            password = input('Enter your password :')
            user = "Kishore"
            pwd = "4873"

            if user_name == user and password == pwd:
                stop_transaction = True
                print('Logged Successfully')
                seat_nos = int(input('Enter Your seats : '))
                total = self.seat_book(seat_nos)
                payment_confirm = input(f"Payment is {total}/- would you like to pay 'y/n': ").lower()
                if payment_confirm == 'Yes':
                    print(self.payment(total))
                else:
                    print("Transaction Cancelled!!!")
            else:
                print('Invalid Credientials')
                attempts-=1
        if not stop_transaction:
            print('Maximum attempts have been reached !!! Try after sometime :( ')

Kumar = TicketBooking()
Kumar_ticket=Kumar.login()
print(Kumar_ticket)