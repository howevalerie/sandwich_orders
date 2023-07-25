"""This file contains a program for ordering sandwiches."""

# Declare List for All Sandwich Orders
complete_order_list = []

# Declare List of the Alphabets in Order
alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                 "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                 "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Declare List for Storing Customer Details
full_customer_details_list = [
    ["Pickup or Delivery:", "Name:", "Address:", "Phone Number:"]
]

order_letters_list = []


def get_string(message):
    """Get string input.

    :param message: string
    :return: string
    """
    running = True
    while running is True:
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
    while running is True:
        # Get input
        my_integer = input(message)
        # Ensure input is an integer
        if my_integer.isdigit() is True:
            return int(my_integer)
        else:
            print("ERROR: Invalid Input. Please try again.")
            print("." * 120)


def get_quantity(message):
    """Get a quantity that it is greater than 0 and lower than 5.

    :param message: string
    :return: integer
    """
    quantity = 0
    running = True
    while running is True:
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
                print("ERROR: Quantity exceeds the maximum of 5. "
                      "Please try again.")
                print("." * 120)
    return quantity


def get_index(relevant_list, item):
    """Find index of item in a list.

    :param relevant_list: list
    :param item: string
    :return: integer
    """
    i = 0
    # Loop through nested lists
    for row in relevant_list:
        # Check if item is in each nested list
        if item in row:
            # If item is in nested list, return the index of the item
            return i
        i += 1


def check_if_in_list(relevant_list, item):
    """Use item provided and return True or False
    depending on whether it is in the list.

    :param relevant_list: list
    :param item: string
    :return: boolean
    """
    for row in relevant_list:
        # Check if item is in each nested list
        if item in row:
            return True


def get_valid_input(valid_inputs_list, message):
    """Get the customer to enter the input until the input is in the 1D list.

    :param valid_inputs_list: list
    :param message: string
    :return: boolean
    """
    running = True
    while running is True:
        # Get the relevant item
        item = get_string(message)
        # Check if the item is valid
        if item in valid_inputs_list:
            return item
        # Customer enters an invalid input
        else:
            print("Invalid Input. Please try again.")
            print("." * 120)


def get_order_total(orders_list, delivery):
    """Calculate the total charge for all the orders.

    :param orders_list: list
    :param delivery: boolean
    :return: integer
    """
    order_total = 0
    # Loop through total order and add costs according to quantity
    for i in range(0, len(orders_list)):
        order_total += orders_list[i][3]
    # Add $3 delivery fee if customer chooses delivery
    if delivery is True:
        order_total += 3
    return order_total


def print_two_column_list(relevant_list):
    """Print list with two columns.

    :param relevant_list: list
    :return: None
    """
    # Loop through list
    for i in range(0, len(relevant_list)):
        # Print items from list
        output = "{}: {:70}"\
            .format(relevant_list[i][0],
                    relevant_list[i][1])
        print(output)
    return None


def print_customer_details(customer_details_list):
    """Print customer details.

    :param customer_details_list: list
    :return: None
    """
    # Loop through the customer details list
    for i in range(0, len(customer_details_list[1])):
        # Print customer details from the list
        output = "{:40} {:<80}"\
            .format(customer_details_list[0][i],
                    customer_details_list[1][i])
        print(output)
    return None


def get_valid_postcode(message):
    """Ensure that the customer's postcode entry is 4 digits long.

    :param message: string
    :return: integer
    """
    running = True
    while running is True:
        postcode_entry = get_integer(message)
        valid_postcode = postcode_entry
        # Count the number of digits in the postcode entry
        digits = 0
        while postcode_entry > 0:
            digits += 1
            postcode_entry = postcode_entry//10
        # Postcode entry has four digits
        if digits == 4:
            return valid_postcode
        # Postcode entry does not have four digits
        else:
            print("ERROR: Invalid Input: 4 digits were expected. "
                  "Please try again.")
            print("." * 120)


def get_valid_phone_number():
    """Get number of digits in the customer's phone number entry.

    :return: integer
    """

    going = True
    while going is True:
        # Get phone number entry
        phone_number_entry = get_integer("Phone Number: (+64) ")
        phone_number = phone_number_entry
        # Count the number of digits in the phone number entry
        digits = 0
        while phone_number_entry > 0:
            digits += 1
            phone_number_entry = phone_number_entry // 10
        if digits == 8:
            valid_phone_number = "+64 " + str(phone_number)
            return valid_phone_number
        else:
            print("ERROR: Invalid Input: "
                  "8 digits were expected. Please try again.")


def print_receipt(orders_list, customer_details_list, method):
    """Print receipt.

    :param orders_list: list
    :param customer_details_list: list
    :param method: boolean
    :return: None
    """
    print("STEP 1: CONFIRM ORDER AND DETAILS")
    print()
    # Print customer details
    print("YOUR DETAILS")
    print_customer_details(customer_details_list)
    print()
    # Print full review of orders
    review_orders(orders_list, method)
    return None


def print_sandwich_menu(sw_list):
    """Print total sandwich menu and prices.

    :param sw_list: list
    :return: None
    """
    # Print sandwich menu
    print("SANDWICH MENU")
    for i in range(0, len(sw_list)):
        output = "{}: {:60}: ${:<10}"\
            .format(sw_list[i][0], sw_list[i][1], sw_list[i][2])
        print(output)
    return None


def order_sandwich(sw_list, orders_list):
    """Get sandwich orders.

    :param sw_list: list
    :param orders_list: list
    :return: None
    """
    # Print sandwich menu
    print_sandwich_menu(sw_list)
    # Display option to return to main menu
    print("{}: {:60}".format("X", "Return to Main Menu"))
    print("." * 120)
    print("MAKE AN ORDER")
    # Get the corresponding letter for customer's choice of sandwich
    msg_sandwich_choice = "{:60}"\
        .format("Select Sandwich Type: ")
    # Get a valid input for the corresponding letter
    sw_choice_letter = get_valid_input(
        ["A", "B", "C", "D", "E", "F", "X"],
        msg_sandwich_choice)

    # Customer wishes to return to the main menu
    if sw_choice_letter == "X":
        return None
    # Customer wishes to make an order

    # Get index for desired sandwich
    sw_type_index = get_index(alphabet_list, sw_choice_letter)
    # Get the name of the desired sandwich
    sw_type = sw_list[sw_type_index][1]
    # Check if an order for this sandwich type already exists
    already_ordered = check_if_in_list(orders_list, sw_type)
    # Customer has already made an order for this sandwich type
    if already_ordered is True:
        # Notify customer of duplication
        print("ERROR: You have already made an "
              "order for {} sandwiches. ".format(sw_type))
        print("." * 120)
        # Display options: edit quantity or cancel duplicate order
        print("OPTIONS")
        duplicate_options = [
            ["A", "Edit Quantity of " + sw_type + " Sandwiches"],
            ["B", "Cancel Duplicate Order & Return to Main Menu"]
        ]
        print_two_column_list(duplicate_options)
        print("")
        # Get customer choice
        msg_option_choice = "Select Option: "
        chosen_option = get_valid_input(["A", "B"], msg_option_choice)
        if chosen_option == "A":
            print("." * 120)
            # Direct customer to edit order quantity
            edit_order(complete_order_list)
            return None
        elif chosen_option == "B":
            return None
    # Customer has NOT already made an order for this sandwich type
    else:
        # Get individual price for the sandwich type
        sw_price = sw_list[sw_type_index][2]
        # Get the desired quantity for the sandwich type
        sw_quantity = get_quantity(
            "{:60}".format("Enter Quantity (Maximum of 5): "))
        # Calculate total cost of sandwiches at quantities
        sw_total_price = sw_quantity*sw_price
        # Store the order details in a list
        order_list = [
            sw_type,
            sw_quantity,
            sw_price,
            sw_total_price
        ]
        # Add order details list to the complete order list
        complete_order_list.append(order_list)
        print("." * 120)
        # Display the processed order
        print("PROCESSED ORDER")
        order_output = "{} x {} Sandwiches"\
            .format(sw_quantity, sw_type)
        print(order_output)
    return None


def review_orders(orders_list, delivery):
    """Allow the customer to review their orders.

    :param orders_list: list
    :param delivery: boolean
    :return: None
    """
    # The customer cannot review orders if their cart is empty
    if len(orders_list) == 0:
        print("ERROR: Unable to review orders as cart is empty")
        return None
    # The customer's cart is not empty
    else:
        print("ORDER REVIEW")
        # Calculate total cost
        order_total = get_order_total(complete_order_list, delivery)
        # Print order review
        for i in range(0, len(orders_list)):
            output = "{} x {:60}: {:<1} x ${:4} = ${:4.2f}"\
                .format(orders_list[i][1],
                        orders_list[i][0],
                        orders_list[i][1],
                        orders_list[i][2],
                        orders_list[i][3])
            print(output)
        # Print total charge
        total_charge = "{:<64}: ${:4.2f}".format("Total Charge", order_total)
        print("-" * 90)
        print(total_charge)
        return None


def edit_order(orders_list):
    """Allow the customer to edit their orders.

    :param orders_list: list
    :return: None
    """
    # The customer cannot edit if their cart is empty
    if len(orders_list) == 0:
        print("ERROR: Unable to edit orders as cart is empty")
        return None
    # The customer's cart is not empty
    else:
        for i in range(0, len(orders_list)):
            letter = alphabet_list[i]
            order_letters_list.append(letter)

        print("EDIT ORDER")
        # Display customer options for editing orders
        edit_options = [
            ["A", "Remove a Sandwich Type"],
            ["B", "Edit Quantity of Sandwich"],
            ["X", "Cancel and Return to Main Menu"]
        ]
        print_two_column_list(edit_options)
        print("." * 120)

        # Get customer choice for editing orders
        msg_user_choice = "Select Operation: "
        user_choice = get_valid_input(["A", "B", "X"], msg_user_choice)
        # Customer Selects: Cancel and Return to Main Menu
        if user_choice == "X":
            order_letters_list.clear()
            return None

        # Display a review of customer orders
        print("." * 120)
        print("ORDER REVIEW")
        for i in range(0, len(orders_list)):
            output = "{}: {} x {:60}"\
                .format(order_letters_list[i],
                        orders_list[i][1],
                        orders_list[i][0])
            print(output)
        print("." * 120)

        # Get customer to select which order to edit
        msg_sw_letter = "Select Order to Edit: "
        sw_letter = get_valid_input(order_letters_list, msg_sw_letter)

        # Get index of letter (same as index of sandwich)
        sw_index = get_index(alphabet_list, sw_letter)
        sw_type = orders_list[sw_index][0]
        sw_quantity = orders_list[sw_index][1]

        # Customer wishes to completely remove an order
        if user_choice == "A":
            # Remove order
            complete_order_list.pop(sw_index)
            # Provide customer confirmation of removal
            print("ACTION: Removed {} x {} Sandwiches"
                  .format(sw_quantity, sw_type))
        # Customer wishes to edit the quantity of the order
        elif user_choice == "B":
            new_quantity_loop = True
            while new_quantity_loop is True:
                # Get new quantity
                new_quantity = get_quantity(
                    "Enter New Quantity for {} Sandwiches: "
                    . format(sw_type))
                orders_list[sw_index][1] = new_quantity
                # The new quantity is the same as old quantity
                if new_quantity == sw_quantity:
                    print("." * 120)
                    # Inform customer
                    print("NOTE: There are already {} {} sandwiches."
                          .format(new_quantity, sw_type))
                    msg_confirmation = "Do you want to proceed with it " \
                                       "(Yes/No)? "
                    no_quantity_change_continue = get_valid_input(
                        ["Yes", "No"], msg_confirmation)
                    # Customer wishes NOT to change order quantity
                    if no_quantity_change_continue == "Yes":
                        print("ACTION: "
                              "Quantity of {} Sandwiches will remain at {}"
                              .format(sw_type, sw_quantity))
                        new_quantity_loop = False
                    # Customer wishes to enter a different quantity
                    elif no_quantity_change_continue == "No":
                        print("Alright. Please Enter New Quantity Again. ")
                        print("."*120)
                # The new quantity is the different to the old quantity
                else:
                    # Display the processed change in quantity
                    print("ACTION: Quantity of {} Sandwiches: "
                          "Updated from {} to {}"
                          .format(sw_type, sw_quantity, new_quantity))
                    new_quantity_loop = False
    return None


def cancel_total_order(orders_list):
    """Allow the customer to cancel all their orders.

    :param orders_list: list
    :return: None
    """
    # Cannot cancel total order until customer places at least one order
    if len(orders_list) == 0:
        print("ERROR: "
              "Unable to cancel all orders as cart is empty")
        return None
    # The customer's cart is not empty
    else:
        # Get the customer's confirmation to cancel order
        cancel_confirm_msg = "Confirmation: Do you want to " \
                             "the cancel all orders (Yes/No)? "
        cancel_confirm = get_valid_input(
            ["Yes", "No"], cancel_confirm_msg)
        # Customer wishes to cancel order
        if cancel_confirm == "Yes":
            # Clear list containing all orders
            complete_order_list.clear()
            # Confirm that all orders have been cancelled
            print("ACTION: All orders have been cancelled")
        # Customer does not wish to cancel the order
        elif cancel_confirm == "No":
            # Confirm that no orders have been cancelled
            print("ACTION: No orders have been cancelled. "
                  "Returning to Main Menu.")


def get_customer_details(customer_details_list):
    """Get customer details according to the pickup or delivery preference.

    :param customer_details_list: list
    :return: None
    """
    # If the customer has already entered their details...
    if len(customer_details_list) == 2:
        # Display collected details and ask if they wish to update them.
        print("UPDATE DETAILS?")
        print("We've already received the following details: ")
        print("")
        print_customer_details(customer_details_list)
        print("")
        update_details_msg = "Do you wish to update your details (Yes/No)? "
        update_details = get_valid_input(
            ["Yes", "No"], update_details_msg)
        # If customer wishes to update their details
        if update_details == "Yes":
            # Delete all details already collected and allow them to re-enter
            customer_details_list.pop(1)
            print("." * 120)
        # If the customer does not wish to update their details
        elif update_details == "No":
            # Inform the customer that no changes have been made to the details
            print("No changes have been made to your details.")
            # Return to Main Menu
            return None

    running = True
    while running is True:
        # Display options for Order Details
        print("STEP 1: ENTER ORDER DETAILS")
        print("")
        pickup_delivery = [
            ["A", "Pickup (No Additional Fee)"],
            ["B", "Delivery (Incurs an Additional $3 Delivery Fee)"],
            ["X", "Cancel and Return to Main Menu"]
        ]
        print_two_column_list(pickup_delivery)
        print("." * 120)

        # Get customer choice (pickup or delivery)
        method = get_valid_input(
            ["A", "B", "X"],
            "Select Preferred Method: ")

        # Customer wishes to return to the main menu
        if method == "X":
            return None

        # Get Customer Details
        print("." * 120)
        print("STEP 2: ENTER YOUR DETAILS")
        print("")
        # Get customer name
        name = get_string("Name: ")

        # Customer selects pickup
        if method == "A":
            customer_details = ["Pickup", name]
            # Add list with customer details into full customer details list
            customer_details_list.append(customer_details)
        # Customer selects delivery
        elif method == "B":
            phone_number = get_valid_phone_number()
            number = str(get_integer("House Number: "))
            street = get_string("Street: ")
            suburb = get_string("Suburb: ")
            postcode = str(get_valid_postcode("Postcode: "))
            # Concatenate address details to create full address
            address = number + " " + street + ", " + suburb + ", " + postcode
            # Store customer name, address and phone number in a list
            customer_details = ["Delivery", name, address, phone_number]
            # Add list with customer details into full customer details list
            customer_details_list.append(customer_details)
        print("." * 120)

        # Get confirmation from customer regarding details
        print("STEP 3: CHECK YOUR DETAILS")
        print("")
        # Display collected customer details
        print_customer_details(customer_details_list)
        print("")
        # Ask customer if the collected details are accurate
        confirm = get_valid_input(
            ["Yes", "No"],
            "CONFIRM: Are the following details accurate (Yes/No)? ")
        # Customer confirms that the collected details are accurate
        if confirm == "Yes":
            # Confirm that details have been saved
            print("Thank you. Your details have been saved.")
            # Return to Main Menu
            return None
        # Customer CANNOT confirm that collected details are accurate
        elif confirm == "No":
            # Delete all details already collected and allow them to re-enter
            customer_details_list.pop(1)
            print("Please Try Again")
            print("." * 120)


def proceed_checkout(orders_list, customer_details_list):
    """Get the customer through the checkout process.

    :param orders_list: list
    :param customer_details_list: list
    :return checkout: string
    """
    # Cannot proceed to checkout until customer places at least one order
    if len(complete_order_list) == 0:
        # Inform the customer
        print("ERROR: Unable to proceed to checkout as cart is empty")
        # Return to Main Menu
        return None
    # Cannot proceed to checkout until customer enters their details
    if len(customer_details_list) == 1:
        # Inform the customer
        print("ERROR: "
              "Unable to proceed to checkout as details have not been entered")
        # Return to Main Menu
        return None
    else:
        # Determine if the customer chose delivery or pickup
        method = customer_details_list[0][0]
        # Print full receipt
        print_receipt(orders_list, customer_details_list, method)
        print()
        print("." * 120)

        # Get confirmation for completing the checkout process
        running = True
        while running is True:
            msg_confirm_checkout = "Confirm and Proceed to Checkout (Yes/No)? "
            checkout = get_valid_input(["Yes", "No"], msg_confirm_checkout)
            print("." * 120)
            # Customer wishes to complete checkout process
            if checkout == "Yes":
                # Confirm that order has been processed
                print("STEP 2: CHECKOUT")
                print("Your Order Has Been Processed. Thank You for Supporting"
                      " the Marsden Gourmet Sandwich Bar!")
                print("." * 120)
                running = False
            # Customer does not wish to complete checkout process
            elif checkout == "No":
                # Delete all customer details
                full_customer_details_list.pop(1)
                print("Returning to Main Menu")
                running = False
    return checkout


def main():
    """Facilitate the main menu and program as a whole.

    :return: None
    """
    print("." * 120)
    # Print welcome
    print("Welcome to the Marsden Gourmet Sandwich Bar!")

    # Sandwich Options and Prices
    sandwich_list = [
        ["A", "Halloumi, Apricot Jam and Coleslaw", 15.95],
        ["B", "Crispy Pork Belly Banh Mi", 18.95],
        ["C", "Roasted Beetroot, Carrot, Spiced Nuts and Feta Cheese", 15.95],
        ["D", "Bratwurst Sausage, Scrambled Egg and Baby Spinach", 14.95],
        ["E", "Smoked Salmon, Olives and Gouda Cheese", 16.95],
        ["F", "Buttermilk Chicken, Pickled Cabbage and Crispy Shallots", 15.95]
    ]

    # Menu Option Lists
    main_menu_list = [
        ["A", "Display Sandwich Menu"],
        ["B", "Place an Order"],
        ["C", "Review Order"],
        ["D", "Edit Order"],
        ["E", "Cancel All Orders"],
        ["F", "Enter Details"],
        ["G", "Proceed to Checkout"],
        ["X", "Quit"]
    ]

    running = True
    while running is True:
        print("." * 120)
        # Print Main Menu
        print("MAIN MENU")
        print_two_column_list(main_menu_list)
        print("." * 120)
        # Get customer's desired operation
        user_choice = get_valid_input(
            ["A", "B", "C", "D", "E", "F", "G", "X"],
            "Select Option: ")
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
            edit_order(complete_order_list)
        # Cancel all orders
        elif user_choice == "E":
            cancel_total_order(complete_order_list)
        # Enter customer details
        elif user_choice == "F":
            get_customer_details(full_customer_details_list)
        # Proceed to checkout
        elif user_choice == "G":
            checkout = proceed_checkout(
                complete_order_list, full_customer_details_list)
            if checkout == "Yes":
                running = False
        # Quit program
        elif user_choice == "X":
            print("Thank you for your time!")
            print("." * 120)
            running = False
    return None


if __name__ == "__main__":
    main()
