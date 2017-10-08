# Change all of your previous OOP assignments so that only the classes are available if the module is imported. Refer back to the optional modular store assignment if you need a refresher.
# Add a __repr__ method to each class. Format your string however you wish.
# Create a new document called manage.py and import all the previous OOP assignments.
# Create new instances of each of the imported classes. Print each instance.

from bike import Bike
from car import Car
from product import Product
from animal import Animal, Dog, Dragon
from math_dojo import MathDojo
from call_center import Call, CallCenter
from hospital import Patient, Hospital

#creating instances of the classes
bike1 = Bike("200","25mph")
car1 = Car(20000,"90mph","gas","30mpg")
prod1 = Product(17.991,"Therapeutic Repair Lotion","16 fl oz","Adamia")

a1 = Animal('Norman the Cheetah')
a1.walk().walk().walk().run().run()
a2 = Dog('Oscar the Labrador')
a2.walk().walk().walk().run().run().pet()
a3 = Dragon('Bessie the Dragon')
a3.fly()

total = MathDojo().add((1, 2),(1,3),5).subtract(2, [2,3], [1.1,2.3], (1,5,6))
call1 = Call(1,"Bambino","720-555-5555","I poured milk all over the floor")
callList = CallCenter()
patient4 = Patient("Alan Clarkson",['latex'])
hospital1 = Hospital("Regional Center", 2)

# printing the instances
print '\n\nBike Assignment:\n', bike1
print '\n\nCar Assignment:\n', car1
print '\n\nProduct Assignment:\n', prod1
print '\n\nAnimal Assignment:\n', a1, ';' , a2, ';' , a3
print '\n\nMath Dojo Assignment:\n', total
print '\n\nCall Center Assignment:\n', call1, callList
print '\n\nHospital Assignment:\n', patient4, 'and', hospital1
