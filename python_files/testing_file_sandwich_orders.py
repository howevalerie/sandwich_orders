def get_input_in_2d_list(relevant_list, message):
    """Get the customer to enter the input until the input is in the 2D list.

    :param relevant_list: list
    :param message: string
    :return: boolean
    """
    running = True
    while running is True:
        # Get the relevant item
        item = get_string(message)
        in_list = False
        # Loop through nested lists
        for row in relevant_list:
            # Check if item is in each nested list
            if item in row:
                in_list = True
        if in_list is True:
            return item
        # Customer enters an invalid input
        else:
            print("Invalid Input. Please try again.")
            print("." * 120)