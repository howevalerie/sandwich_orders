complete_order_list = []
full_customer_details_list = [["Pickup or Delivery:", "Name:", "Address:", "Phone Number:"]]

def get_string(message):
    my_string = str(input(message)).capitalize()
    return my_string

def get_integer(message):
    my_integer = int(input(message))
    return my_integer

def get_quantity(message):
    running = True
    while running == True:
        quantity = int(input(message))
        if quantity <= 5:
            running = False
        else:
            print("Your desired quantity exceeds the maximum of 5. Please try again.")
    return quantity

def get_order_total(L, delivery):
    order_total = 0
    for i in range(0, len(L)):
        order_total += L[i][3]
    if delivery == True:
        order_total +=3
    return order_total

def get_sandwich_index(L, item):
    i = 0
    for x in L:
        if item in x:
            return i
        i +=1

def print_two_list(L):
    for i in range(0, len(L)):
        output = "{}: {:70}".format(L[i][0], L[i][1])
        print(output)
    return None

def print_customer_details(L):
    print("DETAILS")
    for i in range(0, len(L[1])):
        output = "{:20}  {:100}".format(L[0][i], L[1][i])
        print(output)
    return None

def print_sandwich_menu(L):
    print("SANDWICH MENU")
    for i in range(0, len(L)-1):
        output = "{}: {:60}: ${:<10}".format(L[i][0], L[i][1], L[i][2])
        print(output)
    return None

def order_sandwich(L):
    print("SANDWICH MENU")
    for i in range(0, len(L)):
        output = "{}: {:60}: ${:<10}".format(L[i][0], L[i][1], L[i][2])
        print(output)
    print("." * 100)

    running = True
    while running == True:
        print("MAKE AN ORDER")
        sandwich_choice_letter = get_string("{:60}".format("Sandwich Type (Enter Corresponding Alphabet): "))

        if any(sandwich_choice_letter in nested_list for nested_list in L):
            if sandwich_choice_letter == "X":
                running = False
            else:
                order_type_index = get_sandwich_index(L, sandwich_choice_letter)
                order_type = L[order_type_index][1]
                order_type_price = L[order_type_index][2]
                order_quantity = get_quantity("{:60}".format("Quantity (Maximum of 5):"))
                order_type_total_price = order_quantity*order_type_price
                order_list = [order_type, order_quantity, order_type_price, order_type_total_price]
                complete_order_list.append(order_list)
                print("." * 100)
                print("PROCESSED ORDER")
                order_output = "{} x {} Sandwiches".format(order_quantity, order_type)
                print(order_output)
                running = False
        else:
            print("Invalid Input. Please try again.")
            print("." * 100)


def review_orders(L, delivery):
    print("ORDER REVIEW")
    order_total = get_order_total(complete_order_list, delivery)
    for i in range(0, len(L)):
        output = "{} x {:60}: {:<1} x ${:4} = ${:4.2f}".format(L[i][1], L[i][0], L[i][1], L[i][2], L[i][3])
        print(output)
    if delivery == True:
        print("{:>81}".format("+ $3 Delivery Fee"))
    total_charge = "{:<64}: ${:4.2f}".format("Total Charge", order_total)
    print("_" * 100)
    print(total_charge)

def get_customer_details_preferences(L):
    running = True
    while running == True:
        print("STEP 1: PICKUP OR DELIVERY?")
        pickup_delivery = [
            ["A", "Pickup (No Additional Fee)"],
            ["B", "Delivery (Incurs an Additional $3 Delivery Fee)"],
            ["X", "Cancel and Return to Main Menu"]
        ]
        print_two_list(pickup_delivery)
        print("." * 100)
        method = get_string("Select Your Preferred Method (Enter Corresponding Alphabet): ")
        print("." * 100)
        if method == "A":
            print("STEP 2: ENTER DETAILS")
            print()
            name = get_string("Enter Your Name: ")
            customer_details_list = ["Pickup", name]
            full_customer_details_list.append(customer_details_list)
            delivery = False
            running = False
        elif method == "B":
            print("STEP 2: ENTER DETAILS")
            print()
            name = get_string("Name: ")
            address = get_string("Address: ")
            phone_number = get_string("Phone Number: ")
            customer_details_list = ["Delivery", name, address, phone_number]
            full_customer_details_list.append(customer_details_list)
            delivery = True
            running = False
        elif method == "X":
            print("Returning to Main Menu...")
            delivery = False
            running = False
        else:
            print("Invalid Input. Please try again.")
    return delivery, method

def print_receipt(L1, L2, delivery):
    print("STEP 3: CONFIRM ORDER AND DETAILS")
    print()
    print_customer_details(L2)
    print()
    review_orders(L1, delivery)

def proceed_checkout(L1, L2):
    delivery, method = get_customer_details_preferences(L2)
    if method == "X":
        checkout = "No"
    else:
        print("." * 100)
        print_receipt(L1, L2, delivery)
        print()
        checkout = get_string("Confirm and Proceed to Checkout (Yes/No)? ")
        print("." * 100)
        running = True
        while running == True:
            if checkout == "Yes":
                print("STEP 4: CHECKOUT")
                print("Your Order Has Been Processed. Thank You for Supporting the Marsden Gourmet Sandwich Bar!")
                print("." * 100)
                running = False
            elif checkout == "No":
                print("Returning to Main Menu...")
                running = False
            else:
                print("." * 100)
                print("Invalid Input. Please try again.")
    return checkout

def main():
    print("." * 100)
    print("Welcome to the Marsden Gourmet Sandwich Bar!")

    sandwich_list = [
        ["A", "Halloumi, Apricot Jam and Coleslaw", 15.95],
        ["B", "Crispy Pork Belly Banh Mi", 18.95],
        ["C", "Roasted Beetroot, Carrot, Spiced Nuts and Feta Cheese", 15.95],
        ["D", "Bratwurst Sausage, Scrambled Egg and Baby Spinach", 14.95],
        ["E", "Smoked Salmon, Olives and Gouda Cheese", 16.95],
        ["F", "Buttermilk Chicken, Pickled Cabbage and Crispy Shallots", 15.95],
        ["X", "Return to Main Menu", "-----"]
    ]

    main_menu_list = [
        ["A", "Display Sandwich Menu"],
        ["B", "Place an Order"],
        ["C", "Review Order"],
        ["D", "Proceed to Checkout"],
        ["X", "Quit"]
    ]

    running = True
    while running == True:
        print("." * 100)
        print("MAIN MENU")
        print_two_list(main_menu_list)
        print("." * 100)
        user_choice = get_string("Enter the corresponding letter for your desired operation: ")
        print("."*100)

        if user_choice == "A":
            print_sandwich_menu(sandwich_list)
        elif user_choice == "B":
            order_sandwich(sandwich_list)
        elif user_choice == "C":
            delivery = False
            review_orders(complete_order_list, delivery)
        elif user_choice == "D":
            checkout = proceed_checkout(complete_order_list, full_customer_details_list)
            if checkout == "Yes":
                running = False
        elif user_choice == "X":
            print("Thank you for your time!")
            print("." * 100)
            running = False
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()