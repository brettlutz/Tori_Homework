price_separate = []
total_price = 0
cart = []
name = []
price = 0


def display_cart(cart):
    if not cart:
        print('your cart is empty!')
    else:
        print('Shopping cart:')
    for item in cart:
        # might want to format each item["price"] that you print. This isn't such a big deal as you enter the value
        print(f'{item["name"]}: ${item["price"]}')
        total_price += item["price"]
    print(f'total price $: {total_price:.2f}')


print('\n Shopping Cart Application!')


def handle_input():
    print(' 1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
    choice = input('enter your choice: ')
    if choice == '5':
        print('goodbye :)')
        quit()
    elif choice == '1':
        item_name = input('What would you like to add to your cart?: ')
        item_price = float(input('Enter Item Price: $'))
        item = {'name': item_name, 'price': item_price}
        cart.append(item)
        print("added to cart")
        handle_input()
    elif choice == '2':
        display_cart(cart)
        handle_input()
    elif choice == '3':
        if not cart:
            print('Your cart is already empty')
        else:
            display_cart(cart)
            item_index = int(
                input("Enter the item number you want to remove: "))
            if item_index <= 0 or item_index > len(cart):
                removed_item = cart.pop(item_index - 1)
                print(f'removed item: {removed_item}')
            else:
                print('invalid item number')
        handle_input()
    elif choice == '4':
        print(f'your total is ${total_price:.2f}')
        handle_input()


handle_input()
