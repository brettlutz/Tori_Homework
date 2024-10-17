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
    print(f'{item [name]}: ${price_separate}')
    total_price += price
  print (f'total price $: {total_price:.2f}')
  

print('\n Shopping Cart Application!')
print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')

choice = input('enter your choice: ')
if choice == '1':
  item_name = input('What would you like to add to your cart?: ')
  item_price = float(input('Enter Item Price: $'))
  item = {'name': item_name, 'price': item_price}
  cart.append(item)
  print("added to cart")
  print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
  choice = input('enter your choice: ')
elif choice == '2': 
  display_cart(cart)
  print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
  choice = input('enter your choice: ')
elif choice == '3':
  if not cart:
    print('Your cart is already empty')
    print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
    choice = input('enter your choice: ')
  else:
    display_cart(cart)
    item_index = int(input("Enter the item number you want to remove: "))
    if 0 <= item_index < len(cart):
      removed_item = cart.pop(item_index)
      print(f'removed item: {removed_item}')
      print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
      choice = input('enter your choice: ')
    else:
      print('invalid item number')                  
elif choice == '4':
  print (f'your total is ${total_price:.2f}')
  print('1. add to cart \n 2. display cart \n 3. remove item \n 4. compute total \n 5. quit')
  choice = input('enter your choice: ')
elif choice == '5':
  print('goodbye :)')
  quit
  


