complete_order_list = []

def get_string(message):
    my_string = str(input(message)).capitalize()
    return my_string

def get_integer(message):
    my_integer = int(input(message))
    return my_integer

def get_sandwich_type(L, item):
    i = 0
    for x in L:
        if item in x:
            return L[i][1]
        i +=1

def print_main_menu(L):
    print("MAIN MENU")
    for i in range(0, len(L)):
        output = "{}: {:70}".format(L[i][0], L[i][1])
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
        sandwich_choice_letter = get_string("Enter the corresponding letter for your desired sandwich type: ")

        if any(sandwich_choice_letter in nested_list for nested_list in L):
            if sandwich_choice_letter == "X":
                running = False
            else:
                order_type = get_sandwich_type(L, sandwich_choice_letter)
                order_quantity = get_integer("How many {} Sandwiches would you like? ".format(order_type))
                order_list = [order_type, order_quantity]
                complete_order_list.append(order_list)
                print("." * 100)
                order_output = "{} {} Sandwiches have been added to your order. ".format(order_quantity, order_type)
                print(order_output)
                running = False
        else:
            print("Invalid Input. Please try again.")
            print("." * 100)


def review_and_checkout(L):
    print("ORDER REVIEW")
    for i in range(0, len(L)):
        output = "{:60}: {:<5}".format(L[i][0], L[i][1])
        print(output)
    return None

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
        ["X", "Return to Main Menu", "---"]
    ]

    main_menu_list = [
        ["A", "Display Sandwich Menu"],
        ["B", "Place an Order"],
        ["C", "Review Order and Proceed to Checkout"],
        ["X", "Quit"]
    ]

    running = True
    while running == True:
        print("." * 100)
        print_main_menu(main_menu_list)
        print("." * 100)
        user_choice = get_string("Enter the corresponding letter for your desired operation: ")
        print("."*100)

        if user_choice == "A":
            print_sandwich_menu(sandwich_list)
        elif user_choice == "B":
            order_sandwich(sandwich_list)
        elif user_choice == "C":
            review_and_checkout(complete_order_list)
        elif user_choice == "X":
            print("Thank you for your time!")
            running = False
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()