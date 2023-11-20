class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product):
        if product.availability > 0:
            if product in self.items:
                self.items[product] += 1
            else:
                self.items[product] = 1
            product.availability -= 1
        else:
            print(f"{product.name} is not available.")

    def update_quantity(self, product, quantity):
        if product in self.items:
            if product.availability + self.items[product] >= quantity:
                product.availability += self.items[product] - quantity
                self.items[product] = quantity
            else:
                print(f"Only {product.availability + self.items[product]} items of {product.name} are available.")
        else:
            print(f"{product.name} is not in the cart.")

    def remove_product(self, product):
        if product in self.items:
            product.availability += self.items[product]
            del self.items[product]

    def view_total_bill(self):
        total = sum(product.price * quantity for product, quantity in self.items.items())
        return total

def main():
    # Get user input
    products_input = input("Enter products (e.g., [{name: 'Laptop', price: 1000, available: true}] ")
    add_to_cart_input = input("Enter product to add to cart (e.g., 'Laptop'): ")
    update_quantity_input = input("Enter product and quantity to update (e.g., 'Laptop, 2'): ")
    remove_from_cart_input = input("Enter product to remove from cart (e.g., 'Headphones'): ")

    # Parse user input
    products = eval(products_input)
    product_to_add = add_to_cart_input.strip("'")
    product_to_update, quantity_to_update = update_quantity_input.split(', ')
    product_to_remove = remove_from_cart_input.strip("'")
    quantity_to_update = int(quantity_to_update.strip())

    # Create products and add them to the cart[^6^][6]
    cart = Cart()
    for product in products:
        p = Product(**product)
        if p.name == product_to_add:
            cart.add_product(p)
        if p.name == product_to_update:
            cart.update_quantity(p, quantity_to_update)
        if p.name == product_to_remove:
            cart.remove_product(p)

    # View total bill
    print("Total Bill: Your total bill is $", cart.view_total_bill())

if __name__ == "__main__":
    main()
