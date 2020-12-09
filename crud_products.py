class Product:

    _id: int
    _name: str
    _description: str
    _weight: float
    _height: float
    _width: float
    _length: float
    _price: float
    _category: list

    def __init__(
            self, name: str, description: str, price: float, weight: float, 
            height: float, width: float, length: float, category: str
            ) -> None:
        self.set_id()
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)
        self.set_weight(weight)
        self.set_height(height)
        self.set_width(width)
        self.set_length(length)
        self.set_category(category)

    def set_id(self) -> None:
        if len(product_list) == 0:
            self._id = 1
        else:
            self._id = product_list[-1].get_id() + 1

    def set_name(self, name: str) -> None:
        self._name = name

    def set_description(self, description: str) -> None:
            self._description = description


    def set_price(self, price: float) -> None:
        if float(price) > 0:
            self._price = price
        else:
            print('Invalid value')

    def set_weight(self, weight: float) -> None:
        if float(weight) > 0:
            self._weight = weight
        else:
            print('Invalid value')
 
    def set_height(self, height: float) -> None:
        if float(height) > 0:
            self._height = height
        else:
            print('Invalid value')
 
    def set_width(self, width: float) -> None:
        if float(width) > 0:
            self._width = width
        else:
            print('Invalid value')
 
    def set_length(self, length: float) -> None:
        if float(length) > 0:
            self._length = length
        else:
            print('Invalid value')

    def set_category(self, category: list) -> None:
        self._category = category

 
    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_price(self) -> float:
        return self._price

    def get_weight(self) -> float:
        return self._weight

    def get_height(self) -> float:
        return self._height

    def get_width(self) -> float:
        return self._width

    def get_length(self) -> float:
        return self._length

    def get_category(self) -> list:
        return self._category


class Category:

    _name: str

    def __init__(self, name: str) -> None:
        self.set_name(name)

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name


product_list = []
category_list = []

predefined = ['decoration', 'toys', 'crafts', 'furniture', ]
for item in predefined:
    category_list.append(Category(item))

while(True):
    option = int(input(
            '\n1 - REGISTER A NEW PRODUCT' +
            '\n2 - SHOW ALL PRODUCTS' + 
            '\n3 - UPDATE PRODUCT' + 
            '\n4 - DELETE PRODUCT' + 
            '\n0 - EXIT\n'
        ))

    if option == 1:
        product_category = []
        while(True):
            counter = 0
            print('First choose the category in which the product is')
            print('These are the pre-registered categories: ')
            for item in category_list:
                counter = counter + 1
                print(f'{counter} - {item.get_name()}')
            option = input('Enter the desired category number or 0 to create a new one or "S" to exit: ')
            if option.upper() == 'S':
                break
            cat_num = int(option) - 1
            if cat_num == 0:
                new_category = input('Enter category name: ')
                category_list.append(new_category)
                product_category.append(new_category)
            else:
                category = category_list[cat_num].get_name()
                product_category.append(category)
                print(product_category)


        name = input('Enter product name: ')
        description = input('Enter product description: ')
        price = input('Enter product price: ')
        weight = input('Enter product weight: ')
        height = input('Enter product height: ')
        width = input('Enter product width: ')
        length = input('Enter product length: ')

        if len(description) >= 20:
            product_list.append(Product(name, description, price, weight, height, width, length, product_category))
        else:
            print('Try again, for the description there must be at least 20 characters')

    elif option == 2:

        for product in product_list:
            print(
                f'ID: {product.get_id()} ' +
                f'| NAME: {product.get_name()} ' +
                f'| DESCRIPTION: {product.get_description()} ' +
                f'| PRICE: {float(product.get_price()):.2f} ' +
                f'| WEIGHT: {float(product.get_weight()):.2f} ' +
                f'| HEIGHT: {float(product.get_height()):.2f} ' +
                f'| WIDTH: {float(product.get_width()):.2f} ' +
                f'| LENGTH: {float(product.get_length()):.2f} ' +
                f'| CATEGORY: {product.get_category()}'
                )

    elif option == 3:

        update_id = int(input('Enter product ID you want to update: '))

        for product in product_list:
            if product.get_id() == update_id:

                ind = product_list.index(product)
                
                name = input('Enter product new name: ')
                description = input('Enter product new description: ')
                price = input('Enter product new price: ')
                weight = input('Enter product new weight: ')
                height = input('Enter product new height: ')
                width = input('Enter product new width: ')
                length = input('Enter product new length: ')
                category = input('Enter product new category: ')

                if len(description) >= 20:
                    product_list[ind].set_name(name)
                    product_list[ind].set_price(price)
                    product_list[ind].set_price(weight)
                    product_list[ind].set_price(height)
                    product_list[ind].set_price(width)
                    product_list[ind].set_price(length)
                    product_list[ind].set_category(category)
                    break
                else:
                    print('Try again, for the description there must be at least 20 characters')

    elif option == 4:
        delete_id = int(input('Enter product ID you want to delete: '))

        for product in product_list:
            if product.get_id() == delete_id:

                ind = product_list.index(product)                
                product_list.pop(ind)
                break

    elif option == 0:
        print('See ya!')
        break

    else:
        print('Please, choose from 1 to 4 or type 0 to exit')
        continue
