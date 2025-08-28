# online store inventory and sales system
# store Data
store = {
	 "laptop": {"price": 1200, "quantity": 5},
	 "headphones": {"price": 150, "quantity": 10},
	 "mouse": {"price": 40, "quantity": 20}
        }
# add new product

def add_product(store_dict, name, price, quantity):
	if name in store_dict:
		return f"product '{name}' available in the store."
	store_dict[name] = {"price": price, "quantity": quantity}
	return f"product '{name}' added to inventory successful."

# update stock

def update_stock(store_dict, name, quantity):
	if name not in store_dict:
		return f"product '{name}' does not exist in store."
	store_dict[name]["quantity"] += quantity
	return f"stock updated. '{name}'now have {store_dict[name]['quantity']} units added."

# sell product

def sell_product(store_dict, name, quantity):
	if name not in store_dict:
		return f"product '{name}'stock not alvailable now."
	total_price = [store.dict][name][quantity] * [store_dict][name][pice]
	if store_dict[name]["quantity"] < quantity:
		return f"sold NGN{total_price}. stock left: {store_dict}"

# display shop inventory

def display_inventory(store_dict):
	if not store_dict:
		print("shop inventory empty.")
		return 0
	print("\n-------------------------")
	print()
	for product, details in store_dict.items():
		print(f"{product} - price: NGN{details['price']}| quantity: {details['quantity']}")
	return len(store_dict)

# most expensive product
def expensive_dict(store_dict):
	if not store_dict:
		return "no products availble."
	max_product = max(store_dict.items(), key=lambda item: item[1]["price"])
	return f"most expensive product: '{max_product[0]}' at NGN{max_product[1]['price']}"

# total potential sales

def total_potential_sales(store_dict):
	total = sum(details["price"] * details["quantity"] for details in store_dict.values())
	return f"total potentials sales value: NGN{total:.3f}."


# -------------------------
# Example Usage
# -------------------------

print(add_product(store, "Laptop", 350000, 5))
print(add_product(store, "Phone", 250000, 10))
print(add_product(store, "Headphones", 20000, 15))

print(update_stock(store, "Laptop", 2))
print(update_stock(store, "Tablet", 3))

print("---------------------------------")
print()
display_inventory(store)
print("----------------------------------")
print()
print(sell_product(store, "Pehone", 3))
print(sell_product(store, "Lafptop", 1))

print()
print(expensive_dict(store))
print(total_potential_sales(store))
