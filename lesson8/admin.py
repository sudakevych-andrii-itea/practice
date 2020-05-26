from sqlite_context_manager import SQLite


class Admin:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name

    def _create_category_table(self):
        with SQLite(self.db_name) as cur:
            cur.execute("CREATE TABLE if not exists category("
                        "category_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "category_name VARCHAR NOT NULL)")

    def add_category(self, name):
        self._create_category_table()
        with SQLite(self.db_name) as cur:
            cur.execute("INSERT INTO category (category_name) VALUES (?)", (name,))

    def _create_product_table(self):
        with SQLite(self.db_name) as cur:
            cur.execute("CREATE TABLE if not exists product("
                        "product_id INTEGER PRIMARY KEY AUTOINCREMENT, "                        
                        "product_name VARCHAR NOT NULL, "                        
                        "price DECIMAL NOT NULL, "
                        "in_sale TINYINT NOT NULL, "
                        "in_stock TINYINT NOT NULL, "
                        "description TEXT, "
                        "product_url VARCHAR, "
                        "category_id INTEGER,"
                        "FOREIGN KEY(category_id) REFERENCES category(category_id))")

    def add_product(self, product_name, price, in_sale, in_stock, category_id, description='', product_url=''):
        self._create_product_table()
        if not product_url:
            product_url = product_name.replace(' ', '-').lower()
        args = (product_name, price, in_sale, in_stock, description, product_url, category_id)
        with SQLite(self.db_name) as cur:
            cur.execute("INSERT INTO product "
                        "(product_name, price, in_sale, in_stock, description, product_url, category_id)"
                        "VALUES (?,?,?,?,?,?,?)", args)
