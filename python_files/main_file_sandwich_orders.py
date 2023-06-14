complete_order_list = []
alphabet_list = ["A", "B", "C", "D", "E", "F"]
full_customer_details_list = [["Pickup or Delivery", "Name", "Address", "Phone Number"]]

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
            print("Quantity exceeds the maximum of 5. Please try again.")
    return quantity

def check_if_in_list(L, item):
    for row in L:
        if item in row:
            return True

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
        output = "{:64}:  {:<80}".format(L[0][i], L[1][i])
        print(output)
    return None

def print_sandwich_menu(L):
    print("SANDWICH MENU")
    for i in range(0, len(L)-1):
        output = "{}: {:60}: ${:<10}".format(L[i][0], L[i][1], L[i][2])
        print(output)
    return None

def order_sandwich(L1, L2):
    print("SANDWICH MENU")
    for i in range(0, len(L1)):
        output = "{}: {:60}: ${:<10}".format(L1[i][0], L1[i][1], L1[i][2])
        print(output)
    print("." * 120)

    running = True
    while running == True:
        print("MAKE AN ORDER")
        sandwich_choice_letter = get_string("{:60}".format("Select Sandwich Type (Enter Corresponding Alphabet): "))
        x = check_if_in_list(L1, sandwich_choice_letter)
        if x == True:
            if sandwich_choice_letter == "X":
                running = False
            else:
                order_type_index = get_sandwich_index(L1, sandwich_choice_letter)
                order_type = L1[order_type_index][1]
                y = check_if_in_list(L2, order_type)
                if y == True:
                    print("ERROR: You have already made an order for {} sandwiches. ".format(order_type))
                    print("." * 120)
                    print("OPTIONS")
                    duplicate_options = [
                        ["A", "Edit Quantity of {} Sandwiches".format(order_type)],
                        ["B", "Cancel Duplicate Order and Return to Main Menu"],
                    ]
                    print_two_list(duplicate_options)
                    print("")
                    going = True
                    while going == True:
                        chosen_option = get_string("Select Option (Enter Corresponding Alphabet): ")
                        if chosen_option == "A":
                            print("." * 120)
                            edit_order(complete_order_list, alphabet_list)
                            return None
                        elif chosen_option == "B":
                            return None
                        else:
                            print("Invalid Input. Please try again.")
                else:
                    order_type_price = L1[order_type_index][2]
                    order_quantity = get_quantity("{:60}".format("Quantity (Maximum of 5):"))
                    order_type_total_price = order_quantity*order_type_price
                    order_list = [order_type, order_quantity, order_type_price, order_type_total_price]
                    complete_order_list.append(order_list)
                    print("." * 120)
                    print("PROCESSED ORDER")
                    order_output = "{} x {} Sandwiches".format(order_quantity, order_type)
                    print(order_output)
                    running = False
        else:
            print("Invalid Input. Please try again.")
            print("." * 120)


def review_orders(L, delivery):
    if len(L) == 0:
        print("ERROR: Unable to review orders as no orders have been made")
        return None
    else:
        print("ORDER REVIEW")
        order_total = get_order_total(complete_order_list, delivery)
        for i in range(0, len(L)):
            output = "{} x {:60}: {:<1} x ${:4} = ${:4.2f}".format(L[i][1], L[i][0], L[i][1], L[i][2], L[i][3])
            print(output)
        if delivery == True:
            print("{:>81}".format("+ $3 Delivery Fee"))
        total_charge = "{:<64}: ${:4.2f}".format("Total Charge", order_total)
        print("_" * 120)
        print(total_charge)

def get_number_of_digits(phone_number_entry):
    x = phone_number_entry
    digits = 0
    while phone_number_entry > 0:
        digits += 1
        phone_number_entry = phone_number_entry//10
    return digits

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
        print("." * 120)
        method = get_string("Select Preferred Method (Enter Corresponding Alphabet): ")
        print("." * 120)
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
            number = get_integer("House Number: ")
            street = get_string("Street: ")
            suburb = get_string("Suburb: ")
            postcode = get_integer("Postcode: ")
            address = str(number) + " " + street + ", " + suburb + ", " + str(postcode)
            going = True
            while going == True:
                phone_number_entry = get_integer("Phone Number: (+64) ")
                digits = get_number_of_digits(phone_number_entry)
                if digits == 8:
                    phone_number = "+64 " + str(phone_number_entry)
                    customer_details_list = ["Delivery", name, address, phone_number]
                    full_customer_details_list.append(customer_details_list)
                    delivery = True
                    running = False
                    going = False
                else:
                    print("Invalid Input: 8 digits were expected. Please try again.")
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
    if len(L1) == 0:
        print("ERROR: Unable to proceed to checkout as no orders have been made")
        return None
    else:
        delivery, method = get_customer_details_preferences(L2)
        if method == "X":
            checkout = "No"
        else:
            print("." * 120)
            print_receipt(L1, L2, delivery)
            print()
            checkout = get_string("Confirm and Proceed to Checkout (Yes/No)? ")
            print("." * 120)
            running = True
            while running == True:
                if checkout == "Yes":
                    print("STEP 4: CHECKOUT")
                    print("Your Order Has Been Processed. Thank You for Supporting the Marsden Gourmet Sandwich Bar!")
                    print("." * 120)
                    running = False
                elif checkout == "No":
                    full_customer_details_list.pop(1)
                    print("Returning to Main Menu...")
                    running = False
                else:
                    print("." * 120)
                    print("Invalid Input. Please try again.")
        return checkout

def cancel_total_order(L):
    if len(L) == 0:
        print("ERROR: Unable to cancel all orders as no orders have been made")
        return None
    else:
        running = True
        while running == True:
            cancel_confirm = get_string("Confirmation: Do you want to the cancel all orders (Yes/No)? ")
            if cancel_confirm == "Yes":
                complete_order_list.clear()
                print("ACTION: All orders have been cancelled")
                running = False
            elif cancel_confirm == "No":
                print("ACTION: No orders have been cancelled. Returning to Main Menu.")
                running = False
            else:
                print("." * 120)
                print("Invalid Input. Please try again.")


def edit_order(L1, L2):
    if len(L1) == 0:
        print("ERROR: Unable to edit orders as no orders have been made")
        return None
    else:
        print("EDIT ORDER")

        edit_options = [
            ["A", "Remove a Sandwich Type"],
            ["B", "Edit Quantity of Sandwich"],
            ["X", "Cancel and Return to Main Menu"]
        ]
        print_two_list(edit_options)
        going = True
        while going == True:
            running = True
            while running == True:
                print("." * 120)
                user_choice = get_string("Select Operation (Enter Corresponding Alphabet): ")
                if user_choice == "A":
                    running = False
                elif user_choice == "B":
                    running = False
                elif user_choice == "X":
                    return None
                else:
                    print("Invalid Input. Please try again.")

            print("." * 120)
            print("ORDER REVIEW")
            for i in range(0, len(L1)):
                output = "{}: {} x {:60}".format(L2[i], L1[i][1], L1[i][0])
                print(output)

            print("." * 120)
            order_letter_input_loop = True
            while order_letter_input_loop == True:
                edit_sandwich_type_letter = get_string("Select Relevant Order (Enter Corresponding Alphabet): ")
                x = check_if_in_list(L2, edit_sandwich_type_letter)
                if x == True:
                    edit_sandwich_type_index = get_sandwich_index(alphabet_list, edit_sandwich_type_letter)
                    edit_sandwich_type = L1[edit_sandwich_type_index][0]
                    edit_sandwich_quantity = L1[edit_sandwich_type_index][1]
                    order_letter_input_loop = False
                    going = False
                else:
                    print("Invalid Input. Please try again.")

            if user_choice == "A":
                complete_order_list.pop(edit_sandwich_type_index)
                print("ACTION: Removed {} x {} Sandwiches".format(edit_sandwich_quantity, edit_sandwich_type))
                going = False
            elif user_choice == "B":
                new_quantity_loop = True
                while new_quantity_loop == True:
                    new_quantity = get_quantity("Enter New Quantity for {} Sandwiches: ". format(edit_sandwich_type))
                    L1[edit_sandwich_type_index][1] = new_quantity
                    if new_quantity == edit_sandwich_quantity:
                            print("." * 120)
                            no_quantity_change_continue = get_string("NOTE: There are already {} {} sandwiches. Are you sure you want to continue with it (Yes/No)? ".format(new_quantity, edit_sandwich_type))
                            if no_quantity_change_continue == "Yes":
                                print("ACTION: Quantity of {} Sandwiches will remain at {}".format(edit_sandwich_type, edit_sandwich_quantity))
                                new_quantity_loop = False
                                going = False
                            elif no_quantity_change_continue == "No":
                                print("Alright. Please Enter New Quantity Again. ")
                                print("."*120)
                            else:
                                print("Invalid Input. Please try again.")
                    else:
                        print("ACTION: Quantity of {} Sandwiches: Updated from {} to {}".format(edit_sandwich_type, edit_sandwich_quantity, new_quantity))
                        new_quantity_loop = False
                        going = False

def main():
    print("." * 120)
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
        ["D", "Edit Order"],
        ["E", "Cancel All Orders"],
        ["F", "Proceed to Checkout"],
        ["X", "Quit"]
    ]

    running = True
    while running == True:
        print("." * 120)
        print("MAIN MENU")
        print_two_list(main_menu_list)
        print("." * 120)
        user_choice = get_string("Select Operation (Enter Corresponding Alphabet): ")
        print("."*120)

        if user_choice == "A":
            print_sandwich_menu(sandwich_list)
        elif user_choice == "B":
            order_sandwich(sandwich_list, complete_order_list)
        elif user_choice == "C":
            delivery = False
            review_orders(complete_order_list, delivery)
        elif user_choice == "D":
            edit_order(complete_order_list, alphabet_list)
        elif user_choice == "E":
            cancel_total_order(complete_order_list)
        elif user_choice == "F":
            checkout = proceed_checkout(complete_order_list, full_customer_details_list)
            if checkout == "Yes":
                running = False
        elif user_choice == "X":
            print("Thank you for your time!")
            print("." * 120)
            running = False
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()