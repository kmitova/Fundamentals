class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        same_letter = [el for el in self.products if el[0] == first_letter]
        return same_letter

    def __repr__(self):
        self.products.sort()
        new_line = '\n'
        return f"Items in the {self.name} catalogue:{new_line}{new_line.join(self.products)}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
