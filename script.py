from store import Store
from shopper import Shopper

products = {
    "Apple": 2.99,
    "Banana": 3.45,
    "Bread": 1.2,
    "Cheese": 5.65,
    "Eggs": 2.75,
    "Milk": 1.99,
    "Tomatoes": 0.75,
    "Chicken Breast": 7.99,
    "Coffee": 4.5,
    "Orange Juice": 2.25,
    "Yogurt": 3.15,
    "Pasta": 1.5,
    "Salmon": 10.25,
    "Avocado": 2.99,
    "Spinach": 1.25,
    "Olive Oil": 6.49,
    "Cereal": 3.75,
    "Potatoes": 0.99,
    "Ground Beef": 5.89,
    "Ice Cream": 4.25
}

store_name = input('Which store did you visit? ')
store_location = input('Where is it located, enter city name? ')
store = Store(
  store_name,
  store_location,
  products
)
print(store)

shopper_name = input("What is your name? ")
shopper_age = input("What about your age, if not a secret? ")
shopper_payment = input("Did you pay by 'Cash' or 'Card'? ")
shopper_items = input("What did you buy from this list of items: " + store.items_to_string() + " write with commas: ")
shopper = Shopper(
  shopper_name,
  shopper_age,
  shopper_payment,
  store.name,
  [shopper_items, products]
)
print(shopper)