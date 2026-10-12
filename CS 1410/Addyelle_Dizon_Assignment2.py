vending_items = [("1. Coke",        1.75, 1), 
                ("2. Sprite",       1.25, 1), 
                ("3. Fanta ",       1.50, 1), 
                ("4. Water",        1.00, 1), 
                ("5. Apple Juice",  0.50, 1), 
                ("6. Reese's",      0.75, 1), 
                ("7. Hershey's",    0.50, 1),
                ("8. Swedish Fish", 1.00, 1),
                ("9. Doritos",      1.50, 1), 
                ("10. M&M's",       1.25, 1)]
# organization of the items in the list

class Item:
    def __init__(self, description, price=1, quantity=10):
        self.description = description
        self.price = price
        self.quantity = quantity

        if 0 > self.price >= 2.5:
            price  = 1
        if 1 <= self.quantity >= 20:
            quantity = 0

    def set_description(self, new_description):
        self.description = new_description
    
    def set_price(self, new_price):
        if 0 > self.price >= 2.5:
            print("Price has to be $0.01 and $2.50")
        self.price = new_price
    
    def set_quantity(self, new_quantity):
        if 1 <= self.quantity >= 20:
            print("Quantity has to be between 1 and 20")
        self.quantity = new_quantity

    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    def get_quantity(self):
        return self.quantity

class Vending_Machine:
    def __init__(self, items):
        self.items = items
    
    def purchase(self):
        print("Which item would you like to purchase?")
        for item in vending_items:
            print(item)
        vending_choice = int(input())
        match vending_choice:
            case 1:
                print("Would you like to purchase:", vending_items[0])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[0])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 2:
                print("Would you like to purchase:", vending_items[1])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[1])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 3:
                print("Would you like to purchase:", vending_items[2])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[2])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 4:
                print("Would you like to purchase:", vending_items[3])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[3])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 5:
                print("Would you like to purchase:", vending_items[4])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[4])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 6:
                print("Would you like to purchase:", vending_items[5])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[5])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 7:
                print("Would you like to purchase:", vending_items[6])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[6])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 8:
                print("Would you like to purchase:", vending_items[7])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[7])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 9:
                print("Would you like to purchase:", vending_items[8])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[8])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case 10:
                print("Would you like to purchase:", vending_items[9])
                option = input()
                if option == "yes" or "y":
                    print("You have just purchased", vending_items[9])
                elif option == "no" or "n":
                    self.purchase()
                else:
                    print("Invalid choice")
                    self.purchase()
            case default:
                print("Does not exist, please choose another option.")
    
    def load(self):
        for item in vending_items:
            if item == 0:
                print(vending_items)
            elif item != 0:
                print("Please provide a description of the item: ")
                desc = input()
                print("Next, please provide a price for the item: ")
                price = float(input())
                print("Finally, please provide the amount you are loading: ")
                amnt = int(input())

                if price >= 0.00 and price <= 2.50:
                    if amnt > 0 and amnt < 21:
                        loadeditem = (desc, "$" + str(price), amnt)
                        print(loadeditem)
                        break
                    else:
                        print("Please try inputting a valid amount.")
                else:
                    print("Please try inputting a valid price.")
    
    def remove(self):
        print("Which item would you like to remove: ")
        for i in range(len(vending_items)):
            print(vending_items[i])
        removal = int(input())
        match removal:
            case 1:
                vending_items.remove(("1. Coke",        1.75, 1))
                Vending_Machine.remove(self)
            case 2:
                vending_items.remove(("2. Sprite",       1.25, 1))
                Vending_Machine.remove(self)
            case 3:
                vending_items.remove(("3. Fanta ",       1.50, 1))
                Vending_Machine.remove(self)
            case 4:
                vending_items.remove(("4. Water",        1.00, 1))
                Vending_Machine.remove(self)
            case 5:
                vending_items.remove(("5. Apple Juice",  0.50, 1))
                Vending_Machine.remove(self)
            case 6:
                vending_items.remove(("6. Reese's",      0.75, 1))
                Vending_Machine.remove(self)
            case 7:
                vending_items.remove(("7. Hershey's",    0.50, 1))
                Vending_Machine.remove(self)
            case 8:
                vending_items.remove(("8. Swedish Fish", 1.00, 1))
                Vending_Machine.remove(self)
            case 9:
                vending_items.remove(("9. Doritos",      1.50, 1))
                Vending_Machine.remove(self)
            case 10:
                vending_items.remove(("10. M&M's",       1.25, 1))
                Vending_Machine.remove(self)
            case default:
                print("Please choose a valid option.")
                Vending_Machine.remove(self)

def main():
    vending_machine = Vending_Machine(vending_items)
    
    while True:
        print("1. Purchase Item")
        print("2. Load items")
        print("3. Remove items")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                result = vending_machine.purchase()
                print(result)
            case 2: 
                load = vending_machine.load()
            case 3:
                remove = vending_machine.remove()
            case 4:
                break
            case default:
                print("Invalid choice")

main()