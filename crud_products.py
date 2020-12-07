class Products:
    products = []

    def set_product(self):
        name = input('Enter product name: ')
        category = input('Enter product category: ')
        price = input('Enter product price : ')
        self.products.append({
            'name': name,
            'category': category,
            'price': price 
        })

    def show_products(self):
        for product in self.products:
            name, category, price = product.values()
            print('NAME: ' + name + ' CATEGORY: ' + category + ' PRICE: ' + str(price))

