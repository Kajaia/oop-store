class Store:
  def __init__(self, name, location, items):
    self.name = name
    self.location = location
    self.items = items

  def __repr__(self):
    return "The best store called {name} in {location}, with {items} items for sale!".format(name=self.name, location=self.location, items=len(self.items))

  def items_to_string(self):
    items = ""
    for item, price in self.items.items():
      items += item + ", "
    return items