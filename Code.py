class Appointment:
    def __init__(self):
        self.car = input("Car Type: ")
        self.reported_problem = input('Reported Problem: ')
        self.customer_name = input('Customer Name: ')
        self.customer_phone_number = input('Customer Phone #: ')
        
    def print_customer_name(self):
        print(f'Customer: {self.customer_name}')

class Schedule:
    def __init__(self):
        self.appointments = []

    def add_appointment(self):
        time = input('Chose appointment time: ')
        self.appointments.append(time)
        print(f"Appointment booked for {time}.")

class Payment:
    def __init__(self):
        self.payments = []

    def add_payments(self):
        charge = input("Charge: $")
        self.payments.append(charge)
        print(f"Payment of {charge} confirmed.")

appt_1 = Appointment()
appt_1.print_customer_name()
my_schedule = Schedule()
my_schedule.add_appointment()
my_payment = Payment()
my_payment.add_payments()


