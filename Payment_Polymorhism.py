#Polymorphism using Payment Gateways
import time

global cash_input

cash_input = int(input('Enter your Amount : '))
class Upi_Payment():

    def __init__(self):
        print(f'{'*-*'*10} Upi Transaction {'*-*'*10}')
    def payment(self,amount):
        print('')
        
        print(time.sleep(3))
        return f'The amount from Upi {cash_input} /- has been received..'
    

class Credit_Card():
    def __init__(self):
        print(f'{'#-#' * 10} Credit Card Transaction {'#-#'*10}')
    
    def payment(self,amount):
        print('')

        print(time.sleep(3))
        return f'The amount from Credit Card {cash_input} /- has been received..'
    
class Cash():
    def __init__(self):
        print(f' {'$-$-' * 10} Cash payment {'$-$-' * 10}')
    
    def payment(self,amount):
        print('')
        
        print(time.sleep(3))
        return f'The amount {cash_input} /- has been received..'
    


Raju = Upi_Payment()
print(Raju.payment(cash_input))
