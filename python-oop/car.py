"""
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

"""

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = '15%'
        else:
            self.tax = '12%'
        self.displayAll()

    def displayAll(self):
        print "Price: {}\nSpeed: {}\nFuel: {}\nMileage: {}\nTax: {}\n".format(self.price, self.speed,self.fuel,self.mileage,self.tax)
        return self

#creating an instance of the class
car1 = Car(20000,"90mph","gas","30mpg")
car2 = Car(7000,"60mph","gas","20mpg")
car3 = Car(38000,"110mph","gas","25mpg")
car4 = Car(9000,"75mph","gas","18mpg")
car5 = Car(50000,"120mph","hybrid","32mpg")
car6 = Car(65897,"90mph","hybrid","60mpg")
