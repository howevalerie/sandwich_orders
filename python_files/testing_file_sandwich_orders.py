sandwich_list = [
    ["A", "Halloumi, Apricot Jam and Coleslaw", 15.95],
    ["B", "Crispy Pork Belly Banh Mi", 18.95],
    ["C", "Roasted Beetroot, Carrot, Spiced Nuts and Feta Cheese", 15.95],
    ["D", "Bratwurst Sausage, Scrambled Egg and Baby Spinach", 14.95],
    ["E", "Smoked Salmon, Olives and Gouda Cheese", 16.95],
    ["F", "Buttermilk Chicken, Pickled Cabbage and Crispy Shallots", 15.95],
    ["X", "Return to Main Menu", "---"]
]

y = 0.0
i = 0
for i in range(0, len(sandwich_list)-1):
    n = sandwich_list[i][2]
    y += n
print(y)
