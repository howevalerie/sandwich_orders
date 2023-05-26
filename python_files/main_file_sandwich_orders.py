def get_string(message):
    my_string = str(input(message)).capitalize()
    return my_string

def get_integer(message):
    my_integer = int(input(message))
    return my_integer

def print_menu(L):
    for i in range (0, len(L)):
        output = "{}: {:70}: {:<9}".format(L[i][0], L[i][1], L[i][2])
        print(output)
    print("."*120)

def main():

    sandwich_list = [
        ["A", "Halloumi, Apricot Jam and Coleslaw", 15.95],
        ["B", "Crispy Pork Belly Banh Mi", 18.95],
        ["C", "Roasted Beetroot, Carrot, Spiced Nuts and Feta Cheese", 15.95],
        ["D", "Bratwurst Sausage, Scrambled Egg and Baby Spinach", 14.95],
        ["E", "Smoked Salmon, Olives and Gouda Cheese", 16.95],
        ["F", "Buttermilk Chicken, Pickled Cabbage and Crispy Shallots", 15.95]
    ]

    menu_options = """
    A: Print Menu
    X: Quit
    """

    running = True

    while running == True:
        print(menu_options)

        user_choice = get_string("Enter the corresponding letter for your desired operation: ")

        print("."*120)

        if user_choice == "A":
            print_menu(sandwich_list)
        elif user_choice == "X":
            print("Thank you for your time!")
            running = False
        else:
            print("Invalid input. Please try again.")
            print("." * 120)

if __name__ == "__main__":
    main()