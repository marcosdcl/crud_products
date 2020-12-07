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

product = Products()

while True:
    menu = int(input('\n1 - SHOW PRODUCTS\n2 - REGISTER A NEW PRODUCT\n0 - EXIT\n'))
    if menu == 1:
        product.show_products()
    elif menu == 2:
        product.set_product()
    elif menu == 0:
        break
    else:
        print('Please, type only 1 or 2')
        continue
