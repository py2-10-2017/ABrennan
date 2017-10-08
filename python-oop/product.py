"""
The owner of a store wants a program to track products. Create a product class to fill the following requirements.

Product Class:
Attributes: Price, Item Name, Weight, Brand, Cost, Status: default "for sale"

Methods:
- Sell: changes status to "sold"
- Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
- Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.
- Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be chained.
"""
if __name__ != "__main__": #changing so that class is only available if module is imported
    class Product(object):
        def __init__(self, price, name, weight, brand):
            self.price = round(price,2)
            self.name = name
            self.weight = weight
            self.brand = brand
            self.status = 'for sale'

            self.addTax()

        def sellProd(self):
            self.status = 'sold'
            return self

        def addTax(self):
            tax = 0.078
            self.cost = round(self.price * (1+tax),2)
            return self.cost

        def returnProd(self, reason):
            if self.status == 'for sale' or self.status == 'used':
                print "*** You cannot return an item that hasn't been purchased ***"
            else:
                if reason == 'defective':
                    print "*** RETURN: item is defective ***"
                    self.status = 'defective'
                    self.price = 0
                    self.addTax()
                else:
                    print "*** RETURN: item no longer wanted ***"
                    self.status = 'used'
                    self.price = round((self.price * .80),2)
                    self.addTax()

            return self

        def displayAll(self):
            return "Price: ${}\nName: {}\nWeight: {}\nBrand: {}\nCost: ${}\nStatus: {}\n".format(self.price, self.name,self.weight,self.brand,self.cost,self.status)

        def __repr__(self):
            return "Price is ${}, name is {}, weight is {}, brand is {}, cost is ${}, and status is {}".format(self.price, self.name,self.weight,self.brand,self.cost,self.status)


"""
#creating an instance of the class
prod1 = Product(17.991,"Therapeutic Repair Lotion","16 fl oz","Adamia")
prod2 = Product(7.692,"Vitamins E A D Moisturizing Lotion","16 fl oz","GNC")
prod3 = Product(4.99,"Regenerist Regenerating Face Lotion with Sunscreen","1.7 fl oz","Olay")
prod4 = Product(18.99,"Daily Mosturizing Lotion for Dry Skin","18 fl oz","Aveeno")
prod5 = Product(4.16,"Smooth Daily Moisturizing Body Lotion","16.9 fl oz","Nivea")
prod6 = Product(11.19,"Original Herbal Body Moisturizer","17 fl oz","Hempz")

prod1.displayAll()
prod2.sellProd().displayAll()
prod3.returnProd('defective').displayAll()
prod4.returnProd('no longer wanted').displayAll()
prod5.sellProd().returnProd('defective').displayAll()
prod6.sellProd().returnProd('no longer wanted').displayAll()
"""
