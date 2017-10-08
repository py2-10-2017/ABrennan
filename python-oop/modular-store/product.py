class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = round(price,2)
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

        self.addTax()

    def addTax(self):
        tax = 0.078
        self.cost = round(self.price * (1+tax),2)
        return self.cost

    def displayAll(self):
        return "Price: ${}\nName: {}\nWeight: {}\nBrand: {}\nCost: ${}\n".format(self.price, self.name,self.weight,self.brand,self.cost)

if __name__ == "__main__":
    #creating an instance of the class
    prod1 = Product(17.991,"Therapeutic Repair Lotion","16 fl oz","Adamia")
    prod2 = Product(7.692,"Vitamins E A D Moisturizing Lotion","16 fl oz","GNC")
    prod3 = Product(4.99,"Regenerist Regenerating Face Lotion with Sunscreen","1.7 fl oz","Olay")
    prod4 = Product(18.99,"Daily Mosturizing Lotion for Dry Skin","18 fl oz","Aveeno")
    prod5 = Product(4.16,"Smooth Daily Moisturizing Body Lotion","16.9 fl oz","Nivea")
    prod6 = Product(11.19,"Original Herbal Body Moisturizer","17 fl oz","Hempz")
