"""This file facilitates a program for ordering sandwiches."""

# Declare List for All Sandwich Orders
complete_order_list = []

# Declare List of the First Six Alphabets
alphabet_list = ["A", "B", "C", "D", "E", "F"]

# Declare List for Storing Customer Details
full_customer_details_list = [["Pickup or Delivery", "Name", "Address", "Phone Number"]]


def get_string(message):
    """Get string input.

    :param message: string
    :return: string
    """
    running = True
    while running == True:
        # Get input
        my_string = input(message)
        # Remove spaces from input
        my_string_stripped = my_string.strip()
        # Ensure input length is greater than 0
        if len(my_string_stripped) > 0:
            return str(my_string).capitalize()
        else:
            print("ERROR: Input is required. ")
            print("." * 120)


def get_integer(message):
    """Get integer input.

    :param message: string
    :return: integer
    """
    running = True
    while running == True:
        # Get input
        my_integer = input(message)
        # Ensure input is an integer
        if my_integer.isdigit() == True:
            return int(my_integer)
        else:
            print("ERROR: Invalid Input. Please try again.")
            print("." * 120)


def get_quantity(message):
    """Get a quantity that it is greater than 0 and lower than 5.

    :param message: string
    :return: integer
    """
    running = True
    while running == True:
        # Get the customer's desired quantity
        quantity = get_integer(message)
        # Ensure quantity is not 0
        if quantity == 0:
            print("ERROR: Quantity must be greater than 0. Please try again.")
            print("." * 120)
        else:
            # Ensure quantity is less than 5
            if quantity <= 5:
                running = False
            else:
                print("ERROR: Quantity exceeds the maximum of 5. Please try again.")
                print("." * 120)
    return quantity


def check_if_in_list(list_1, item):
    """Take item and check if it is in the list.

    :param list_1: list
    :param item: string
    :return: boolean
    """
    # Loop through nested lists
    for row in list_1:
        # Check if item is in each nested list
        if item in row:
            return True


def get_order_total(list_1, delivery):
    """Calculate the total charge for all the orders.

    :param list_1: list
    :param delivery: boolean
    :return: integer
    """
    order_total = 0
    # Loop through total order and add costs according to quantity
    for i in range(0, len(list_1)):
        order_total += list_1[i][3]
    # Add $3 delivery fee if customer chooses delivery
    if delivery == True:
        order_total += 3
    return order_total


def get_sandwich_index(list_1, item):
    """Find index of sandwich type in list.

    :param list_1: list
    :param item: string
    :return: integer
    """
    i = 0
    # Loop through nested lists
    for row in list_1:
        # Check if item is in each nested list
        if item in row:
            # If item is in nested list, return the index of the sandwich type
            return i
        i += 1


def print_two_list(list_1):
    """Print list.

    :param list_1: list
    :return: None
    """
    # Loop through list
    for i in range(0, len(list_1)):
        # Print items from list
        output = "{}: {:70}".format(list_1[i][0], list_1[i][1])
        print(output)
    return None


def print_customer_details(list_1):
    """Print customer details.

    :param list_1: list
    :return: None
    """
    print("DETAILS")
    # Loop through the customer details list
    for i in range(0, len(list_1[1])):
        # Print customer details from the list
        output = "{:64}:  {:<80}".format(list_1[0][i], list_1[1][i])
        print(output)
    return None


def get_phone_number_digits(phone_number_entry):
    """Get number of digits in the customer's phone number entry.

    :param phone_number_entry: integer
    :return: integer
    """
    # Count the number of digits in the phone number entry
    digits = 0
    while phone_number_entry > 0:
        digits += 1
        phone_number_entry = phone_number_entry//10
    return digits


def get_valid_postcode(message):
    """Ensure that the customer's postcode entry is 4 digits long

    :param message: string
    :return: integer
    """
    running = True
    while running == True:
        postcode_entry = get_integer(message)
        # Count the number of digits in the postcode entry
        digits = 0
        while postcode_entry > 0:
            digits += 1
            postcode_entry = postcode_entry//10
        # Postcode entry has four digits
        if digits == 4:
            return postcode_entry
        # Postcode entry does not have four digits
        else:
            print("ERROR: Invalid Input: 4 digits were expected. Please try again.")
            print("." * 120)


def get_customer_details_preferences(list_1):
    """Get customer details according to the pickup or delivery preference.

    :param list_1: list
    :return: boolean, string
    """
    # Give options for pickup, delivery and return to main menu
    print("STEP 1: PICKUP OR DELIVERY?")
    pickup_delivery = [
        ["A", "Pickup (No Additional Fee)"],
        ["B", "Delivery (Incurs an Additional $3 Delivery Fee)"],
        ["X", "Cancel and Return to Main Menu"]
    ]
    print_two_list(pickup_delivery)
    print("." * 120)

    running = True
    while running == True:
        # Get customer choice (pickup or delivery)
        method = get_string("Select Preferred Method (Enter Corresponding Alphabet): ")
        print("." * 120)
        print("STEP 2: ENTER DETAILS")
        print()
        # Customer selects pickup
        if method == "A":
            # Get customer name
            name = get_string("Enter Your Name: ")
            # Store customer name in a list
            customer_details_list = ["Pickup", name]
            # Add list with customer details into full customer details list
            full_customer_details_list.append(customer_details_list)
            # Indicate that it is not a delivery (so no $3 delivery fee)
            delivery = False
            running = False
        # Customer selects delivery
        elif method == "B":
            # Get customer name
            name = get_string("Name: ")
            # Get customer address details
            number = str(get_integer("House Number: "))
            street = get_string("Street: ")
            suburb = get_string("Suburb: ")
            postcode = str(get_valid_postcode("Postcode: "))
            # Concatenate address details to create full address
            address = number + " " + street + ", " + suburb + ", " + postcode
            # Get customer phone number
            going = True
            while going == True:
                phone_number_entry = get_integer("Phone Number: (+64) ")
                digits = get_phone_number_digits(phone_number_entry)
                if digits == 8:
                    phone_number = "+64 " + str(phone_number_entry)
                    going = False
                else:
                    print("ERROR: Invalid Input: "
                          "8 digits were expected. Please try again.")
            # Store customer name, address and phone number in a list
            customer_details_list = ["Delivery", name, address, phone_number]
            # Add list with customer details into full customer details list
            list_1.append(customer_details_list)
            # Indicate delivery status (additional $3 delivery fee)
            delivery = True
            running = False
        # Customer wishes to return to the main menu
        elif method == "X":
            delivery = False
            running = False
        # Customer has entered an invalid input
        else:
            print("ERROR: Invalid Input. Please try again.")
            print("." * 120)
    return delivery, method


def print_receipt(list_1, list_2, delivery):
    """Print receipt.

    :param list_1: list
    :param list_2: list
    :param delivery: boolean
    :return: None
    """
    print("STEP 3: CONFIRM ORDER AND DETAILS")
    print()
    # Print customer details (eg. pickup/delivery, name, address, phone number)
    print_customer_details(list_2)
    print()
    # Print full review of orders
    review_orders(list_1, delivery)
    return None


def print_sandwich_menu(list_1):
    """Print total sandwich menu and prices.

    :param list_1: list
    :return: None
    """
    # Print sandwich menu
    print("SANDWICH MENU")
    for i in range(0, len(list_1)):
        output = "{}: {:60}: ${:<10}".format(list_1[i][0], list_1[i][1], list_1[i][2])
        print(output)
    return None


def order_sandwich(list_1, list_2):
    """Get sandwich orders.

    :param list_1: list
    :param list_2: list
    :return: None
    """
    # Print sandwich menu
    print_sandwich_menu(list_1)
    # Display option to return to main menu
    print("{}: {:60}".format("X", "Return to Main Menu"))
    print("." * 120)
    print("MAKE AN ORDER")
    running = True
    while running == True:
        # Get the corresponding letter for customer's choice of sandwich
        msg_sandwich_choice = "{:60}".format("Select Sandwich Type (Enter Corresponding Alphabet): ")
        sw_choice_letter = get_string(msg_sandwich_choice)
        # Check if corresponding letter is valid
        x = check_if_in_list(list_1, sw_choice_letter)
        # Customer enters a valid entry for corresponding letter
        if x == True:
            # Customer wishes to return to the main menu
            if sw_choice_letter == "X":
                running = False
            # Customer wishes to order a sandwich
            else:
                # Get index for desired sandwich
                sw_type_index = get_sandwich_index(list_1, sw_choice_letter)
                # Get the name of the desired sandwich
                sw_type = list_1[sw_type_index][1]
                # Check if an order for this sandwich type already exists
                already_ordered = check_if_in_list(list_2, sw_type)
                # Customer has already made an order for this sandwich type
                if already_ordered == True:
                    # Notify customer of duplication
                    print("ERROR: You have already made an order for {} sandwiches. ".format(sw_type))
                    print("." * 120)
                    # Display options: edit quantity or cancel duplicate order
                    print("OPTIONS")
                    duplicate_options = [
                        ["A", "Edit Quantity of " + sw_type + " Sandwiches"],
                        ["B", "Cancel Duplicate Order & Return to Main Menu"]
                    ]
                    print_two_list(duplicate_options)
                    print("")
                    going = True
                    while going == True:
                        # Get customer choice
                        msg_option_choice = "Select Option (Enter Corresponding Alphabet): "
                        chosen_option = get_string(msg_option_choice)
                        if chosen_option == "A":
                            print("." * 120)
                            # Direct customer to edit order quantity
                            edit_order(complete_order_list, alphabet_list)
                            return None
                        elif chosen_option == "B":
                            return None
                        else:
                            print("ERROR: Invalid Input. Please try again.")
                # Customer has NOT already made an order for this sandwich type
                else:
                    # Get individual price for the sandwich type
                    sw_price = list_1[sw_type_index][2]
                    # Get the desired quantity for the sandwich type
                    sw_quantity = get_quantity("{:60}".format("Enter Quantity (Maximum of 5): "))
                    # Calculate total cost of sandwiches at quantities
                    sw_total_price = sw_quantity*sw_price
                    # Store the order details in a list
                    order_list = [sw_type, sw_quantity, sw_price, sw_total_price]
                    # Add order details list to the complete order list
                    complete_order_list.append(order_list)
                    print("." * 120)
                    # Display the processed order
                    print("PROCESSED ORDER")
                    order_output = "{} x {} Sandwiches".format(sw_quantity, sw_type)
                    print(order_output)
                    running = False
        # Customer enters an invalid entry for corresponding letter
        else:
            print("ERROR: Invalid Input. Please try again.")
            print("." * 120)
    return None


def review_orders(list_1, delivery):
    """Allow the customer to review their orders.

    :param list_1: list
    :param delivery: boolean
    :return: None
    """
    # The customer cannot review orders until they place at least one order
    if len(list_1) == 0:
        print("ERROR: Unable to review orders as no orders have been made")
        return None
    else:
        print("ORDER REVIEW")
        # Calculate total cost
        order_total = get_order_total(complete_order_list, delivery)
        # Print order review
        for i in range(0, len(list_1)):
            output = "{} x {:60}: {:<1} x ${:4} = ${:4.2f}".format(list_1[i][1], list_1[i][0], list_1[i][1], list_1[i][2], list_1[i][3])
            print(output)
        total_charge = "{:<64}: ${:4.2f}".format("Total Charge", order_total)
        print("-" * 120)
        print(total_charge)
        return None


def edit_order(list_1, list_2):
    """Allow the customer to edit their orders.

    :param list_1: list
    :param list_2: list
    :return: None
    """
    # The customer cannot edit orders until they place at least one order
    if len(list_1) == 0:
        print("ERROR: Unable to edit orders as no orders have been made")
        return None
    else:
        print("EDIT ORDER")
        # Display customer options for editing orders
        edit_options = [
            ["A", "Remove a Sandwich Type"],
            ["B", "Edit Quantity of Sandwich"],
            ["X", "Cancel and Return to Main Menu"]
        ]
        print_two_list(edit_options)
        user_choice = "X"

        going = True
        while going == True:
            running = True
            while running == True:
                print("." * 120)
                # Get customer choice for editing orders
                user_choice = get_string("Select Operation (Enter Corresponding Alphabet): ")
                if user_choice == "A":
                    running = False
                elif user_choice == "B":
                    running = False
                elif user_choice == "X":
                    return None
                else:
                    print("ERROR: Invalid Input. Please try again.")

            # Display a review of customer orders
            print("." * 120)
            print("ORDER REVIEW")
            for i in range(0, len(list_1)):
                output = "{}: {} x {:60}".format(list_2[i], list_1[i][1], list_1[i][0])
                print(output)

            # Get customer to select which order to edit
            print("." * 120)
            edit_sandwich_type_index = 0
            edit_sandwich_type = ""
            edit_sandwich_quantity = 0
            order_letter_input_loop = True
            while order_letter_input_loop == True:
                edit_sandwich_type_letter = get_string("Select Relevant Order (Enter Corresponding Alphabet): ")
                x = check_if_in_list(list_2, edit_sandwich_type_letter)
                if x == True:
                    edit_sandwich_type_index = get_sandwich_index(alphabet_list, edit_sandwich_type_letter)
                    edit_sandwich_type = list_1[edit_sandwich_type_index][0]
                    edit_sandwich_quantity = list_1[edit_sandwich_type_index][1]
                    order_letter_input_loop = False
                    going = False
                else:
                    print("ERROR: Invalid Input. Please try again.")

            # Customer wishes to remove order
            if user_choice == "A":
                # Remove order
                complete_order_list.pop(edit_sandwich_type_index)
                # Provide customer confirmation
                print("ACTION: Removed {} x {} Sandwiches".format(edit_sandwich_quantity, edit_sandwich_type))
                going = False
            # Customer wishes to edit the quantity of the order
            elif user_choice == "B":
                new_quantity_loop = True
                while new_quantity_loop == True:
                    # Get new quantity
                    new_quantity = get_quantity("Enter New Quantity for {} Sandwiches: ". format(edit_sandwich_type))
                    list_1[edit_sandwich_type_index][1] = new_quantity
                    # The new quantity is the same as old quantity
                    if new_quantity == edit_sandwich_quantity:
                        print("." * 120)
                        # Inform customer
                        print("NOTE: There are already {} {} sandwiches.".format(new_quantity, edit_sandwich_type))
                        no_quantity_change_continue = get_string("Do you want to proceed with it (Yes/No)? ")
                        # Customer wishes not to change order quantity
                        if no_quantity_change_continue == "Yes":
                            print("ACTION: Quantity of {} Sandwiches will remain at {}".format(edit_sandwich_type, edit_sandwich_quantity))
                            new_quantity_loop = False
                            going = False
                        # Customer wishes to enter a different quantity
                        elif no_quantity_change_continue == "No":
                            print("Alright. Please Enter New Quantity Again. ")
                            print("."*120)
                        # Customer enters an invalid input
                        else:
                            print("ERROR: Invalid Input. Please try again.")
                    # The new quantity is the different to the old quantity
                    else:
                        # Display the processed change in quantity
                        print("ACTION: Quantity of {} Sandwiches: Updated from {} to {}".format(edit_sandwich_type, edit_sandwich_quantity, new_quantity))
                        new_quantity_loop = False
                        going = False
    return None


def cancel_total_order(list_1):
    """Allow the customer to cancel all their orders.

    :param list_1: list
    :return: None
    """
    # The customer cannot cancel the total order until they place at least one order
    if len(list_1) == 0:
        print("ERROR: Unable to cancel all orders as no orders have been made")
        return None
    else:
        running = True
        while running == True:
            # Get the customer's confirmation to cancel order
            cancel_confirm = get_string("Confirmation: Do you want to the cancel all orders (Yes/No)? ")
            # Customer wishes to cancel order
            if cancel_confirm == "Yes":
                # Clear list containing all orders
                complete_order_list.clear()
                # Confirm that all orders have been cancelled
                print("ACTION: All orders have been cancelled")
                running = False
            # Customer does not wish to cancel the order
            elif cancel_confirm == "No":
                # Confirm that no orders have been cancelled
                print("ACTION: No orders have been cancelled. Returning to Main Menu.")
                running = False
            # Customer enters an invalid input
            else:
                print("." * 120)
                print("ERROR: Invalid Input. Please try again.")


def proceed_checkout(list_1, list_2):
    """Get the customer through the checkout process.

    :param list_1: list
    :param list_2: list
    :return: string
    """
    # The customer cannot proceed to checkout until they place at least one order
    if len(list_1) == 0:
        print("ERROR: Unable to proceed to checkout as no orders have been made")
        return None
    else:
        # Get customer preference for pick up or delivery
        delivery, method = get_customer_details_preferences(list_2)
        # Customer wishes to return to main menu
        if method == "X":
            checkout = "No"
        # Customer has selected pick up or delivery
        else:
            print("." * 120)
            # Print full receipt
            print_receipt(list_1, list_2, delivery)
            print()
            print("." * 120)
            # Get customer confirmation before completing the checkout process
            checkout = get_string("Confirm and Proceed to Checkout (Yes/No)? ")
            print("." * 120)
            running = True
            while running == True:
                # Customer wises to complete checkout process
                if checkout == "Yes":
                    # Confirm that order has been processed
                    print("STEP 4: CHECKOUT")
                    print("Your Order Has Been Processed. Thank You for Supporting the Marsden Gourmet Sandwich Bar!")
                    print("." * 120)
                    running = False
                # Customer does not wish to complete checkout process
                elif checkout == "No":
                    # Delete all customer details
                    full_customer_details_list.pop(1)
                    print("Returning to Main Menu.")
                    # Return to main menu
                    running = False
                # Customer enters an invalid input
                else:
                    print("." * 120)
                    print("ERROR: Invalid Input. Please try again.")
        return checkout


def main():
    """Facilitate the main menu and program as a whole.

    :return: None
    """
    print("." * 120)
    # Print welcome
    print("Welcome to the Marsden Gourmet Sandwich Bar!")

    sandwich_list = [
        ["A", "Halloumi, Apricot Jam and Coleslaw", 15.95],
        ["B", "Crispy Pork Belly Banh Mi", 18.95],
        ["C", "Roasted Beetroot, Carrot, Spiced Nuts and Feta Cheese", 15.95],
        ["D", "Bratwurst Sausage, Scrambled Egg and Baby Spinach", 14.95],
        ["E", "Smoked Salmon, Olives and Gouda Cheese", 16.95],
        ["F", "Buttermilk Chicken, Pickled Cabbage and Crispy Shallots", 15.95]
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
        # Print main menu
        print("MAIN MENU")
        print_two_list(main_menu_list)
        print("." * 120)
        # Get customer's desired operation
        user_choice = get_string("Select Operation (Enter Corresponding Alphabet): ")
        print("."*120)

        # Display sandwich menu
        if user_choice == "A":
            print_sandwich_menu(sandwich_list)
        # Place an order
        elif user_choice == "B":
            order_sandwich(sandwich_list, complete_order_list)
        # Review order
        elif user_choice == "C":
            delivery = False
            review_orders(complete_order_list, delivery)
        # Edit order
        elif user_choice == "D":
            edit_order(complete_order_list, alphabet_list)
        # Cancel all orders
        elif user_choice == "E":
            cancel_total_order(complete_order_list)
        # Proceed to checkout
        elif user_choice == "F":
            checkout = proceed_checkout(complete_order_list, full_customer_details_list)
            if checkout == "Yes":
                running = False
        # Quit program
        elif user_choice == "X":
            print("Thank you for your time!")
            print("." * 120)
            running = False
        else:
            print("ERROR: Invalid input. Please try again.")
    return None


if __name__ == "__main__":
    main()
