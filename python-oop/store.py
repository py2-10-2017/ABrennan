"""
Store class:
Attributes:
- products: an array of products objects
- location: store address
- owner: store owner's name

Methods:
- add_product: add a product to the store's product list
- remove_product: should remove a product according to the product name
- inventory: print relevant information about each product in the store

"""
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


class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        p = product.name
        i = 0
        for product in self.products:
            if product.name == p:
                self.products.pop(i)
            i += 1
        return self

    def inventory(self):
        if self.products:
            print '\n\nInventory for store location {}, owned by {}:'.format(self.location, self.owner)
            i = 1
            for product in self.products:
                print '---- Product # ', i, '----\n', product.displayAll()
                i += 1
        else:
            print 'This company is out of business\n\n'

        return self


#creating an instance of the class
prod1 = Product(17.991,"Therapeutic Repair Lotion","16 fl oz","Adamia")
prod2 = Product(7.692,"Vitamins E A D Moisturizing Lotion","16 fl oz","GNC")
prod3 = Product(4.99,"Regenerist Regenerating Face Lotion with Sunscreen","1.7 fl oz","Olay")
prod4 = Product(18.99,"Daily Mosturizing Lotion for Dry Skin","18 fl oz","Aveeno")
prod5 = Product(4.16,"Smooth Daily Moisturizing Body Lotion","16.9 fl oz","Nivea")
prod6 = Product(11.19,"Original Herbal Body Moisturizer","17 fl oz","Hempz")

#creating instance of store
store1 = Store('San Jose, CA', 'John Doe')

#no inventory - store is out of business
store1.inventory()


#adds 6 products to the store and prints inventory
store1.add_product(prod1).add_product(prod2).add_product(prod3).add_product(prod4).add_product(prod5).add_product(prod6).inventory()

#remove 2 products and prints inventory
store1.remove_product(prod6).remove_product(prod2).inventory()
