CREATE TABLE IF NOT EXISTS dim_customer (
    customer_key INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    customer_name TEXT,
    city TEXT
);

CREATE TABLE IF NOT EXISTS dim_customer (
    customer_key INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    customer_name TEXT,
    city TEXT
);


CREATE TABLE IF NOT EXISTS dim_product (
    product_key INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    product_name TEXT,
    category TEXT
);


CREATE TABLE IF NOT EXISTS dim_date (
    date_key INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date TEXT
);


CREATE TABLE IF NOT EXISTS fact_sales (
    order_id INTEGER,
    customer_key INTEGER,
    product_key INTEGER,
    date_key INTEGER,
    amount REAL
);
