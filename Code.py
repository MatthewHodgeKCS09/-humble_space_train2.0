class Appointment:
    def __init__(self):
        self.car = input("Car Type: ")
        self.reported_problem = input('Reported Problem: ')
        self.customer_name = input('Customer Name: ')
        self.customer_phone_number = input('Customer Phone #: ')
        
        def print_customer_name(self):
            print(f'Customer: {self.customer_name}')

appt_1 = Appointment()
appt_1.print_customer_name()
