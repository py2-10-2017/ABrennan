# Create an Animal class and give it attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

if __name__ != "__main__": #changing so that class is only available if module is imported
    class Animal(object):
        def __init__(self,name):
            self.name = name
            self.health = 75

        def walk(self):
            self.health -= 1
            return self

        def run(self):
            self.health -= 5
            return self

        def displayHealth(self):
            return 'Health of {}: {}'.format(self.name,self.health)

        def __repr__(self):
            return '{}: {} health points'.format(self.name,self.health)


    class Dog(Animal):
        def __init__(self, dogName):
            super(Dog, self).__init__(dogName)
            self.health = 150

        def pet(self):
            self.health += 5
            return self

    class Dragon(Animal):
        def __init__(self, dragonName):
            super(Dragon, self).__init__(dragonName)
            self.health = 170

        def fly(self):
            self.health -= 10
            return self

        def displayHealth(self):
            print 'Eek, a dragon!'
            super(Dragon, self).displayHealth()


"""
a1 = Animal('Norman the Cheetah')
a1.walk().walk().walk().run().run().displayHealth()

a2 = Dog('Oscar the Labrador')
a2.walk().walk().walk().run().run().pet().displayHealth()

a3 = Dragon('Bessie the Dragon')
a3.fly().displayHealth()


# Create a new Animal and confirm that it can not call the pet()
a4 = Animal('Ollie the Monkey')
# a4.pet().displayHealth()
# Error: 'Animal' object has no attribute 'pet'

# Create a new Animal and confirm that it can not call the fly()
a5 = Animal('David the Squirrel')
# a5.fly().displayHealth()
# Error: 'Animal' object has no attribute 'fly'

# Confirm that your Dog class can not fly().
a6 = Dog('Larry the Pug')
# a6.fly().displayHealth()
# Error: 'Dog' object has no attribute 'fly'
"""
