class Shopper:
  def __init__(self, name, age, payment_type, store, items):
    self.name = name
    self.age = age
    self.payment_type = payment_type
    self.store = store
    self.items = items

  def __repr__(self):
    return "Byer {name}, who is {age} years old, purchased {items_length} items by {payment} in {store} store, for a total of: {total}₾".format(name=self.name, age=self.age, payment=self.payment_type, store=self.store, items_length=self.items_length(), total=str(self.calculate_total()))

  def items_length(self):
    return len(self.purchased_items())

  def calculate_total(self):
    purchased_items = self.purchased_items()
    store_items = self.items[1]
    total = 0
    for item, price in store_items.items():
      for purchase in purchased_items:
        if item == purchase:
          total += price
    return total

  def purchased_items(self):
    return [item.strip() for item in self.items[0].split(',')]