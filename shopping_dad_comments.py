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
        # TODO from dad need to remove the space and put the name in quotes item["name"]
        # price_separate should be item["price"]
        # the addition should be
        # total_price += item['price']
        # might want to format each item["price"] that you print. This isn't such a big deal as you enter the value
        print(f'{item["name"]}: ${price_separate}')
        total_price += price
    print(f'total price $: {total_price:.2f}')


print('\n Shopping Cart Application!')

# TODO from dad. make this all into a function, and then call the function after each choice
# this will get the looping you want. You then need to call this after it is defined in order to start
# it. This only needs to be called once in each option besides 5, just as the very last
# option outside any other if/else logic. By changing this it also doesn't require setting the list
# of choices and enter your choice as constants since they are only typed out once.


def handle_input():
    print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
    choice = input('enter your choice: ')
    if choice == '5':
        print('goodbye :)')
        # TODO need to call quit using (), so
        # quit()
        quit
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
            # TODO from dad. You need to check each condition separately, and use and/or. In this case
            # the number can't be both less than 0 and greater than the length of the cart
            # so you would use or
            # if item_index <= 0 or item_index > len(cart):
            # for item_index you will want to delete 1 because indexes are 0 based
            # removed_item = cart.pop(item_index - 1)
            if 0 <= item_index < len(cart):
                removed_item = cart.pop(item_index)
                print(f'removed item: {removed_item}')
            else:
                print('invalid item number')
            # TODO from dad. I moved the choice outside the if/else statement
            # that way if they make an invalid selection it prompts them for action again.
        handle_input()
    elif choice == '4':
        print(f'your total is ${total_price:.2f}')
        handle_input()


handle_input()
