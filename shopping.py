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
        print(f'{item["name"]}: ${item["price"]}')
        total_price += item["price"]
    print(f'total price $: {total_price:.2f}')


CHOICES = ' 1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit'
ENTER = "enter your choices: "


print('\n Shopping Cart Application!')


print(CHOICES)

choice = input(ENTER)
if choice == '5':
    print('goodbye :)')
    quit()
elif choice == '1':
    item_name = input('What would you like to add to your cart?: ')
    item_price = float(input('Enter Item Price: $'))
    item = {'name': item_name, 'price': item_price}
    cart.append(item)
    print("added to cart")
    print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
    choice = input(ENTER)
elif choice == '2':
    display_cart(cart)
    print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
    choice = input(ENTER)
elif choice == '3':
    if not cart:
        print('Your cart is already empty')
        print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
        choice = input(ENTER)
    else:
        display_cart(cart)
        item_index = int(input("Enter the item number you want to remove: "))
        if item_index <= 0 and item_index < len(cart):
            removed_item = cart.pop(item_index - 1)
            print(f'removed item: {removed_item}')
        else:
            print('invalid item number')
        print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
        choice = input(ENTER)
elif choice == '4':
    print(f'your total is ${total_price:.2f}')
    print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
    choice = input(ENTER)

    # test for commit message
