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


if __name__ == "__main__":
    #creating instance of store
    store1 = Store('San Jose, CA', 'John Doe')
