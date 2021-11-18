import unittest


print(1%2)
# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in list(sentence):
		if i.lower() == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		most = 0
		for thing in self.items:
			if item.stock > most:
				most = self.item
		return most
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		highest = self.item[0]
		for item in self.items:
			if item.price > highest:
				most = self.item


# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual (count_a("Banana"), 3)
		self.assertEqual (count_a("BAnanA"), 3)
		self.assertEqual (count_a("bruh"), 0)
		self.assertEqual (count_a(""), 0)
		self.assertEqual (count_a("a"), 1)
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		warehouse = Warehouse()
		self.assertEqual(len(warehouse.items), 0)
		warehouse.add_item(self.item1)
		self.assertEqual(len(warehouse.items), 1)
		warehouse.add_item(self.item2)
		warehouse.add_item(self.item3)
		self.assertEqual(len(warehouse.items), 3)

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		warehouse1 = Warehouse()
		warehouse1.add_item(self.item1)
		self.assertEqual(warehouse1.get_max_stock(), self.item1)
		warehouse1.add_item(self.item2)
		warehouse1.add_item(self.item3)


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		pass
		

def main():
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()