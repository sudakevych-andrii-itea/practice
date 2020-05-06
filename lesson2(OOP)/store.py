class Store:
    total_sold_count_item = 0

    def __init__(self, name, sold_items_count):
        self.name = name,
        self.sold_items_count = sold_items_count
        Store.total_sold_count_item += self.sold_items_count

    def increase_sold_items_count(self, sold_count):
        self.sold_items_count += sold_count
        Store.total_sold_count_item += sold_count

    def get_sold_items_count(self):
        return self.sold_items_count

    @staticmethod
    def get_total_sold_items_count():
        return Store.total_sold_count_item


if __name__ == '__main__':
    store1 = Store('store1', 0)
    store1.increase_sold_items_count(100)
    print(store1.get_sold_items_count())
    store2 = Store('store2', 200)
    print(store2.get_sold_items_count())
    print(Store.get_total_sold_items_count())
