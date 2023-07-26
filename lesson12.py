from sqlite3 import connect


conn = connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (32) NOT NULL UNIQUE
    );
''')
conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (128) NOT NULL,
        descr VARCHAR (4096),
        price DECIMAL (8, 2) NOT NULL CHECK ( price > 0 ),
        is_published BOOLEAN DEFAULT (true),
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
    );
''')
conn.commit()

cur.execute('CREATE INDEX IF NOT EXISTS category_id_index ON product (category_id);')
cur.execute('CREATE INDEX IF NOT EXISTS is_published_index ON product (is_published);')
conn.commit()


# cur.execute('''
#     INSERT INTO category (name) VALUES (?);
# ''', ('Coffee', ))
# conn.commit()

# cur.execute('''
#     SELECT * FROM category WHERE id >= 1;
# ''')
# print(cur.fetchall())


# cur.execute('''
#     UPDATE category SET name = ? WHERE id = 1;
# ''', ('Кофе', ))
# conn.commit()


# cur.execute("DELETE FROM category WHERE name LIKE '%акция%';")
# conn.commit()

# products = (
#     ('Cappuccino', 5.5, 1),
#     ('Latte', 6.5, 1),
# )
# cur.executemany('INSERT INTO product (name, price, category_id) VALUES (?, ?, ?);', products)
# conn.commit()


# cur.execute('INSERT INTO category (name) VALUES (?);', ('Tea', ))
# conn.commit()


# cur.execute('''
#     SELECT category.name, product.name, product.price
#     FROM category
#     JOIN product ON category.id = product.category_id
#     WHERE product.is_published = true;
# ''')
# print(cur.fetchall())


from psycopg2 import connect
from psycopg2.extras import NamedTupleCursor


with connect('postgresql://bh69:qwerty@0.0.0.0:5432/bh69') as conn:
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        # cur.execute("insert into category(name) values(%s);", ('Coffee', ))
        # conn.commit()
        cur.execute('select * from category;')
        print(cur.fetchall())
