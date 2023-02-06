from json import loads

products_file_path = "./products.txt"


def get_all_products():
    with open(products_file_path) as products_file:
        return [loads(line.strip()) for line in products_file]
