# import datetime

# currentYear = datetime.datetime.now().year

# class Car(object):
#     def __init__(self, color, model, make, price, year):
#         self.color = color
#         self.model = model
#         self.make = make
#         self.price = price
#         self.year = year

#     def service(self):
#         if(currentYear - self.year > 4):
#             print("You Need To Service Your Vehicle!!")
#         else:
#             print("You Vehicle's Condition Is Good!!")

# car = Car('red', 'A', 'ABC', 2634675, 2020)

# car.service()

class Mobile(object):
    def __init__(self, color, model, company, screensize, memory, battery):
        self.color = color
        self.model = model
        self.company = company
        self.screensize = screensize
        self.memory = memory
        self.battery = battery

    def checkbattery(self) :
        if(self.battery < 20):
            print("Charge Your Phone!!")

    def checkmemory(self):
        if(self.memory > 125):
            print("Your Phone Is High On Space!!")
        elif(self.memory > 80 and self.memory < 125):
            print("You Have A Little Space Use It Wisely!!")
        else:
            print("Your Phone Has A Lot Of Space!!")
    
    def checkscreensize(self):
        if(self.screensize > 6):
            print("Your Phone Size Is Too Huge!!")
        elif(self.screensize > 5.5 and self.screensize < 6):
            print("Your Phone Size Is Just Alright!!")
        else:
            print("Your Phone Is Too Small!!")

mobile = Mobile("blue", 'iPhone6', 'Apple', 7, 120, 10)
mobile.checkbattery()
mobile.checkmemory()
mobile.checkscreensize()