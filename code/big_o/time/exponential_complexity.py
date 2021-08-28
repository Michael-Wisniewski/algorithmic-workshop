def find_menu(toppings):
    menu = ['']

    for topping in toppings:
        new_variants = []

        for variant in menu:
            new_variants.append(variant)

        for index in range(len(new_variants)):
            new_variants[index] += topping
            
        menu += new_variants

    return menu
