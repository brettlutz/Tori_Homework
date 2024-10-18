options = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]
items = []


def print_options():
    for index, item in enumerate(options):
        print(f"{index + 1}. {item}")


def print_items():
    for index, item in enumerate(items):
        print(f"{index + 1}: {item['name']} - ${item['price']}")


def select_option():
    print("\nAvailable actions:")
    print_options()
    user_choice = int(input("Please select an option from the list above: "))
    return user_choice


shopping = True
while shopping:
    choice = select_option()
    if choice < 0 or choice > 5:
        print("You have made an invalid selection.")
    elif choice == 1:
        add_item = True
        while add_item:
            name_input = input("\nWhat would you like to add to your cart? ")
            price_input = input("How much does it cost? ")
            items.append({"name": name_input, "price": price_input})
            add_another = input("Would you like to add another item? YES/NO ")
            if (add_another.lower() == "no"):
                add_item = False
    elif choice == 2:
        print_items()
    elif choice == 3:
        if len(items) == 0:
            print("\nYour cart is already empty, please make another selection")
        else:
            print_items()
            delete_selection = int(
                input("\nWhich item would you like to remove? "))
            if delete_selection > len(items):
                print("You have made an invalid selection.")
            else:
                del items[delete_selection - 1]
    elif choice == 4:
        total = 0
        for item in items:
            total += float(item['price'])
        print(f"\nYour cart total is: ${total}")
    else:
        shopping = False
        print("\nThank you for using the shopping cart")
