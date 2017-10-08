from product import Product
from store import Store


#creating an instance of the class
prod1 = Product(17.991,"Therapeutic Repair Lotion","16 fl oz","Adamia")
prod2 = Product(7.692,"Vitamins E A D Moisturizing Lotion","16 fl oz","GNC")
prod3 = Product(4.99,"Regenerist Regenerating Face Lotion with Sunscreen","1.7 fl oz","Olay")
prod4 = Product(18.99,"Daily Mosturizing Lotion for Dry Skin","18 fl oz","Aveeno")
prod5 = Product(4.16,"Smooth Daily Moisturizing Body Lotion","16.9 fl oz","Nivea")
prod6 = Product(11.19,"Original Herbal Body Moisturizer","17 fl oz","Hempz")

#creating instance of store
store2 = Store('Phoenix, AZ', 'Jane Doe')

#no inventory - store is out of business
store2.inventory()


#adds 6 products to the store and prints inventory
store2.add_product(prod1).add_product(prod2).add_product(prod3).add_product(prod4).add_product(prod5).add_product(prod6).inventory()

#remove 2 products and prints inventory
store2.remove_product(prod6).remove_product(prod2).inventory()
