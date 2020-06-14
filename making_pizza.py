#requested_toopings = ['mayo']
#if requested_toopings:
  #  for requested_tooping in requested_toopings:
       # print("Adding "+requested_tooping.title()+" into your pizza.")
#else:
 #   print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requsted_topping in requested_toppings:
    if requsted_topping in available_toppings:
        print("Adding "+requsted_topping.title()+" to your pizza!")
    else:
        print("We are sorry! "+requsted_topping.title()+" is out of stock!")


print("Here is your pizza!")