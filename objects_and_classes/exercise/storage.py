class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if self.capacity > len(self.storage):
            self.storage.append(product)

    def get_products(self):
        return self.storage

storage = Storage(3)
storage.add_product("a")
storage.add_product("b")
storage.add_product("c")
storage.add_product("d")
storage.add_product("e")
print(storage.get_products())
