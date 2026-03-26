# Define the menu of restaurant
class Restaurant:
    def __init__(self):
        self.menu = {
             'Pizza':40,
             'Pasta':50,
             'Burger':60,
             'Tea':30,
             'Coffee':80,
        }
        self.order = {}
        print("--------------- SURAJ RASTURANT --------------")
        for item,price in self.menu.items():
         print(f"{item}: Rs{price}")  
    def add_order(self,item,quantity):
         if item in self.menu:
                  self.order[item] = self.order.get(item , 0) + quantity
                  print(f"{quantity} {item} added to order.")
         else:
              print("Item menu is not available")               
                                
    def generate_bill(self):
        print("------------------FINAL BILL------------------")
        subtotal = 0
        for item, qty in self.order.items():
                    price =self.menu[item]
                    subtotal +=price * qty
                    print(f"{item}: {price} x {qty} = {price * qty}")
                 
        # Discount calculate           
        discount = 0
        if subtotal > 500:
                discount = subtotal * 0.10
                total = subtotal - discount

        print("----------------------------------------------")
        print(f"Subtotal: {subtotal}")
        print(f"Discount:{discount}")
        print(f"Total Amount:{total}")
        print("----------------------------------------------")
        
my_restaurant = Restaurant()
while True:
           name = input("Enter item Name :").strip().title()
           q = input(f"Enter quantity: ")
           my_restaurant.add_order(name ,int(q))
           
           choice = input("Do you want to add another item(Yes/No):").lower()
           if choice == "no":
               break

obj = Restaurant()
my_restaurant.generate_bill()
print("Thank you! Visit Again")