items = ["1. Coke", "2. Sprite", "3. Fanta", "4. Water", "5. Apple Juice", "6. Reese's", "7. Hershey's", "8. Swedish Fish", "9. Doritos", "10. M & M's"]
item_descriptions = ["Item 1: A Coke bottle", "Item 2: A Sprite bottle", "Item 3: A Fanta bottle", "Item 4: A water bottle", "Item 5: An apple juice pouch", "Item 6: A Reese's Puffs candy", "Item 7: A Hershey's chocolate bar", "Item 8: A Swedish Fish bag", "Item 9: A Doritos chips bag", "Item 10: An M & M's bag"]
item_prices = [1.75, 1.25, 1.50, 1.00, 0.50, 0.75, 0.50, 1.00, 1.50, 1.25]
item_amounts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def vending_choice_options():
    print("----------------------")
    print("Please pick a number: ")
    print("----------------------")
    print("1. Purchase an item")
    print("2. Load a new item")
    print("3. Remove an item")
    print("4. Refill an item")
    print("5. Quit")
    print("----------------------")

def desc_price_amnt():
    for i in range(len(items)):
        print(items[i] + "\t" + str(item_prices[i]) + "\t" + str(item_amounts[i]))

def yesnochoice():
    yesno = input()
    if yesno == "y":
        print("Thank you for your purchase!")
        purchasing()
    elif yesno == "n":
        purchasing()
    else:
        print("Invalid choice. Please choose a valid option.")
        yesnochoice()

def purchasing():
    while choice == 1:
        print("--------------------------------------")
        print("Which item would you like to purchase?")
        print("--------------------------------------")
        for item in items:
            print(item)
        vending_choice = int(input())
        match vending_choice:
            case 1:
                item_amounts[0]
                print("---------")
                print(item_descriptions[0])
                print("$" + str(item_prices[0]))
                print("---------")
                print("Would you like to purchase", items[0] + "?", "y/n")
                yesnochoice()
                item_amounts[0] -= 1
                return item_amounts[0]
            case 2:
                item_amounts[1]
                print("---------")
                print(item_descriptions[1])
                print("$" + str(item_prices[1]))
                print("---------")
                print("Would you like to purchase", items[1] + "?", "y/n")
                yesnochoice()
                item_amounts[1] -= 1
                return item_amounts[1]
            case 3:
                item_amounts[2]
                print("---------")
                print(item_descriptions[2])
                print("$" + str(item_prices[2]))
                print("---------")
                print("Would you like to purchase", items[2] + "?", "y/n")
                yesnochoice()
                item_amounts[2] -= 1
                return item_amounts[2]
            case 4:
                item_amounts[3]
                print("---------")
                print(item_descriptions[3])
                print("$" + str(item_prices[3]))
                print("---------")
                print("Would you like to purchase", items[3] + "?", "y/n")
                yesnochoice()
                item_amounts[3] -= 1
                return item_amounts[3]
            case 5:
                item_amounts[4]
                print("---------")
                print(item_descriptions[4])
                print("$" + str(item_prices[4]))
                print("---------")
                print("Would you like to purchase", items[4] + "?", "y/n")
                yesnochoice()
                item_amounts[4] -= 1
                return item_amounts[4]
            case 6:
                item_amounts[5]
                print("---------")
                print(item_descriptions[5])
                print("$" + str(item_prices[5]))
                print("---------")
                print("Would you like to purchase", items[5] + "?", "y/n")
                yesnochoice()
                item_amounts[5] -= 1
                return item_amounts[5]
            case 7:
                item_amounts[6]
                print("---------")
                print(item_descriptions[6])
                print("$" + str(item_prices[6]))
                print("---------")
                print("Would you like to purchase", items[6] + "?", "y/n")
                yesnochoice()
                item_amounts[6] -= 1
                return item_amounts[6]
            case 8:
                item_amounts[7]
                print("---------")
                print(item_descriptions[7])
                print("$" + str(item_prices[7]))
                print("---------")
                print("Would you like to purchase", items[7] + "?", "y/n")
                yesnochoice()
                item_amounts[7] -= 1
                return item_amounts[7]    
            case 9:
                item_amounts[8]
                print("---------")
                print(item_descriptions[8])
                print("$" + str(item_prices[8]))
                print("---------")
                print("Would you like to purchase", items[8] + "?", "y/n")
                yesnochoice()
                item_amounts[8] -= 1
                return item_amounts[8]  
            case 10:
                item_amounts[9]
                print("---------")
                print(item_descriptions[9])
                print("$" + str(item_prices[9]))
                print("---------")
                print("Would you like to purchase", items[9] + "?", "y/n")
                yesnochoice()
                item_amounts[9] -= 1
                return item_amounts[9]
            case default:
                print("---------------------------------------------")
                print("Does not exist, please choose another option.")
                purchasing()
        for item in items:
            if item == 0:
                items.remove(item)

def loading():
    while choice == 2:
        for item in items:
            if item == 0:
                print("Please load the empty numbers.")
                print(items)
            elif item != 0:
                print("------------------------------------------")
                print("Please provide a description of the item: ")
                print("------------------------------------------")
                desc = input()
                print("-------------------------------------------")
                print("Next, please provide a price for the item: ")
                print("-------------------------------------------")
                price = float(input())
                print("----------------------------------------------------")
                print("Finally, please provide the amount you are loading: ")
                print("----------------------------------------------------")
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

def removing():
    while choice == 3:
        print("--------------------------")
        desc_price_amnt()
        print("--------------------------")
        print("Please remove an item.")
        removal = int(input())
        match removal:
            case 1:
                items.remove("1. Coke")
                desc_price_amnt()
                removing()
            case 2:
                items.remove("2. Sprite")
                desc_price_amnt()
                removing()
            case 3:
                items.remove("3. Fanta")
                desc_price_amnt()
                removing()
            case 4:
                items.remove("4. Water")
                desc_price_amnt()
                removing()
            case 5:
                items.remove("5. Apple Juice")
                desc_price_amnt()
                removing()
            case 6:
                items.remove("6. Reese's")
                desc_price_amnt()
                removing()
            case 7:
                items.remove("7. Hershey's")
                desc_price_amnt()
                removing()
            case 8:
                items.remove("8. Swedish Fish")
                desc_price_amnt()
                removing()
            case 9:
                items.remove("9. Doritos")
                desc_price_amnt()
                removing()
            case 10:
                items.remove("10. M & M's")
                desc_price_amnt()
                removing()
            case default:
                print("Please choose a valid option.")
                removing()
    
def refilling():
    while choice == 4:
        print("--------------------------")
        for i in range(len(items)):
            print(items[i] + "\t" + str(item_amounts[i]))
        print("--------------------------")
        print("Please choose a number.")
        print("--------------------------")
        add = int(input())
        match add:
            case 1:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[0] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[0] + " are " + str(item_amounts[0]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 2:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[1] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[1] + " are " + str(item_amounts[1]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 3:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[2] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[2] + " are " + str(item_amounts[2]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 4:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[3] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[3] + " are " + str(item_amounts[3]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 5:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[4] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[4] + " are " + str(item_amounts[4]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 6:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[5] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[5] + " are " + str(item_amounts[5]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 7:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[6] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[6] + " are " + str(item_amounts[6]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 8:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[7] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[7] + " are " + str(item_amounts[7]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 9:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[8] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[8] + " are " + str(item_amounts[8]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case 10:
                print("-------------------------------")
                print("How much would you like to add?")
                print("-------------------------------")
                adding = int(input())
                if adding < 20:
                    item_amounts[9] += adding
                    print("-------------------------------")
                    print("The new amount of items for " + items[9] + " are " + str(item_amounts[9]))
                    print("-------------------------------")
                    refilling()
                else:
                    print("----------------------")
                    print("Please add new amount.")
                    refilling()
            case default:
                print("Please choose a valid option.")
                refilling()

def quit():
    while choice == 5:
        print("Are you sure you want to quit? y/n")
        yn = input()
        if yn == "y":
            print("Goodbye.")
        elif yn == "n":
            quit()
        else:
            print("Please pick a valid choice.")
            quit()
    
    else:
        print("Please choose a valid option.")


vending_choice_options()
choice = int(input())
match choice:
    case 1:
        purchasing()
    case 2:
        loading()
    case 3:
        removing()
    case 4:
        refilling()
    case 5:
        quit()

