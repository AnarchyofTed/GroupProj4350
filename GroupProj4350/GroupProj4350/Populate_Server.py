
from server import *
def MakeDataBase(serverName,databaseName):
    #serverName= input('Enter the server name: ')
    MainServer=server(serverName, databaseName)
    MainServer.command("""CREATE TABLE customers(
                            customer_id UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL PRIMARY KEY,
                            customer_name varchar(50) NOT NULL,
                            customer_phone varchar(11) NOT NULL UNIQUE,
                            customer_storePreference varchar(50) NOT NULL,
                            customer_username varchar(50) NOT NULL,
                            customer_password varchar(50) NOT NULL
                            );""")
    MainServer.command("""CREATE TABLE employees(
                                employee_id UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL PRIMARY KEY,
                                employee_name varchar(50) NOT NULL,
                                employee_username varchar(50) NOT NULL,
                                employee_password varchar(50) NOT NULL,
                                employee_storePreference varchar(50) NOT NULL,
                                employee_accessLevel int NOT NULL,
                                employee_sales DECIMAL(10,2) NOT NULL,
                                employee_phone varchar(11) NOT NULL UNIQUE);""")
    MainServer.command("""CREATE TABLE store(
                                store_id UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL PRIMARY KEY,
                                store_sales DECIMAL(10,2) NOT NULL,
                                store_name varchar(50) NOT NULL UNIQUE);""")
    MainServer.command("""CREATE TABLE orders(
                                order_id UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL PRIMARY KEY,
                                customer_id UNIQUEIDENTIFIER FOREIGN KEY REFERENCES customers(customer_id),
                                employee_id UNIQUEIDENTIFIER FOREIGN KEY REFERENCES employees(employee_id),
                                store_id UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES store(store_id),
                                order_date DATE NOT NULL,order_price DECIMAL(10,2) NOT NULL);""")
    MainServer.command("""CREATE TABLE shipments(
                                shipment_id UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL PRIMARY KEY,
                                order_id UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES orders(order_id),
                                shipment_date DATE NOT NULL);""")
    MainServer.command("""CREATE TABLE item(
                                item_id UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL PRIMARY KEY,
                                item_price DECIMAL(10,2) NOT NULL,item_description varchar(50) NOT NULL,
                                quantity_inStock int NOT NULL);""")
    MainServer.command("""CREATE TABLE full_set(
                                set_id UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL PRIMARY KEY,
                                set_description varchar(50) NOT NULL UNIQUE);""")
    MainServer.command("""CREATE TABLE set_item(
                                set_itemId UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL PRIMARY KEY,
                                item_id UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES item(item_id),
                                set_itemQuantity int NOT NULL,
                                set_id UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES full_set(set_id));""")
    MainServer.command("""INSERT INTO customers(customer_name, customer_phone, customer_storePreference, customer_username, customer_password)VALUES(
                                'Blake Cox', '2134567968', 'LegoTron', 'MrBlake123', '123456'),
                                ('Jacob Butler',  '1230987658', 'LegoTron', 'MrJacob456', '123456'),
                                ('Drew Araujo',  '1235436554', 'Mrs.LegoTron', 'MrDrew789', '123456');""")
    MainServer.command("""INSERT INTO employees(employee_name, employee_username, employee_password, employee_storePreference, employee_accessLevel, employee_sales, employee_phone)VALUES
                                ('Joseph Smith', 'Mr.Smith', 'password', 'Mrs.LegoTron', 1, 10000, '2143245543'),	
                                ('Harry Potter', 'Mr.Potter', 'password1', 'Mrs.LegoTron', 2, 9000, '2145555543'),	
                                ('Billy Idol', 'Mr.Idol', 'password2', 'LegoTron', 1, 15000, '2154345543'),	
                                ('Pocahontas Lady', 'Mr.Lady', 'password3', 'LegoTron', 2, 11000, '7657655543');""")
    MainServer.command("INSERT INTO store(store_sales, store_name)VALUES(200345, 'Mrs.LegoTron'),(591765, 'LegoTron');")
    MainServer.command("""INSERT INTO orders(customer_id, employee_id, order_date, order_price, store_id)VALUES
                                ((SELECT customer_id FROM customers WHERE customer_phone='2134567968'), (SELECT employee_id FROM employees WHERE employee_phone='2143245543'),'2020-04-29', 108.92, (SELECT store_id FROM store WHERE store_name='Mrs.LegoTron')),	
                                ((SELECT customer_id FROM customers WHERE customer_phone='2134567968'), (SELECT employee_id FROM employees WHERE employee_phone='2143245543'),'2020-04-12', 400.92, (SELECT store_id FROM store WHERE store_name='Mrs.LegoTron')),((SELECT customer_id FROM customers WHERE customer_phone='1235436554'), (SELECT employee_id FROM employees WHERE employee_phone='7657655543'), '2020-05-21', 678.90, (SELECT store_id FROM store WHERE store_name='LegoTron')),		((SELECT customer_id FROM customers WHERE customer_phone='1235436554'), (SELECT employee_id FROM employees WHERE employee_phone='7657655543'), 		'2020-01-21', 70.90, (SELECT store_id FROM store WHERE store_name='LegoTron')),		((SELECT customer_id FROM customers WHERE customer_phone='1235436554'), NULL,		'2020-03-25', 432.90, (SELECT store_id FROM store WHERE store_name='Mrs.LegoTron')),		((SELECT customer_id FROM customers WHERE customer_phone='1230987658'), (SELECT employee_id FROM employees WHERE employee_phone='2145555543'), 		'2020-06-28', 54.90, (SELECT store_id FROM store WHERE store_name='Mrs.LegoTron')),		((SELECT customer_id FROM customers WHERE customer_phone='1230987658'), (SELECT employee_id FROM employees WHERE employee_phone='2154345543'), 		'2020-03-21', 890.90, (SELECT store_id FROM store WHERE store_name='LegoTron')),		((SELECT customer_id FROM customers WHERE customer_phone='1230987658'), NULL, 		'2020-04-21', 1023.99, (SELECT store_id FROM store WHERE store_name='LegoTron')),	(NULL, (SELECT employee_id FROM employees WHERE employee_phone='2154345543'), 	'2020-02-12', 36.70, (SELECT store_id FROM store WHERE store_name='LegoTron'));""")
    MainServer.command("INSERT INTO shipments(order_id, shipment_date)VALUES((SELECT order_id FROM orders WHERE order_price = 1023.99), '2020-04-22'),((SELECT order_id FROM orders WHERE order_price = 70.90), '2020-01-22'),	((SELECT order_id FROM orders WHERE order_price = 678.90), '2020-05-22');")
    MainServer.command("INSERT INTO item(item_price, item_description, quantity_inStock)VALUES(.28, 'Brick 1x8 Blue', 127),(.28, 'Brick 1x8 Red', 94),(.28, 'Brick 1x8 Yellow', 342),(.28, 'Brick 1x8 Orange', 110),(.28, 'Brick 1x8 Black', 76),(.89, 'Plate 4x4 Round Orange', 132),(.89, 'Plate 4x4 Round Red', 121),(.89, 'Plate 4x4 Round Black', 212),(.89, 'Plate 4x4 Round Yellow', 87),(.89, 'Plate 4x4 Round Blue', 92),(.14, 'Plate 2x3 Yellow', 23),(.14, 'Plate 2x3 Black', 23),(.14, 'Plate 2x3 Orange', 23),(.14, 'Plate 2x3 Purple', 23),(.07, 'Nose Cone Small', 40),(.06, 'Round Brick 1x1 Green', 104),(.06, 'Round Brick 1x1 Red', 94),(.06, 'Round Brick 1x1 Yellow', 144),(.06, 'Round Brick 1x1 Maroon', 104),(.24, '.5 Circle Plate 2x6 Blue', 90), (.24, '.5 Circle Plate 2x6 Red', 99), (.24, '.5 Circle Plate 2x6 Yellow', 120), (.24, '.5 Circle Plate 2x6 Black', 81), (.24, '.5 Circle Plate 2x6 Orange', 37), (.32, 'Brick 2x8 Red', 86),(.32, 'Brick 2x8 Blue', 109),(.32, 'Brick 2x8 Green', 78),(.32, 'Brick 2x8 Orange', 120),(.32, 'Brick 2x8 Black', 139),(.53, 'Brick 4x16 Red', 86),(.53, 'Brick 4x16 Blue', 86),(.53, 'Brick 4x16 Black', 86),(.53, 'Brick 4x16 Yellow', 86),(.53, 'Brick 4x16 Orange', 86),(.53, 'Brick 4x16 Green', 86),(2.3, 'Person 1', 42),(2.3, 'Person 2', 48),(2.3, 'Person 3', 37),(2.3, 'Person 4', 9),(7.9, 'Person 5', 1),(2.3, 'Person 6', 67),(2.3, 'Person 7', 96),(.24, 'Brick 2x2 Red', 201),(.24, 'Brick 2x2 Yellow', 223),(.24, 'Brick 2x2 Blue', 231),(.24, 'Brick 2x2 Black', 278),(.24, 'Brick 2x2 Green', 301),(1.2, 'Plate 12x24 Red', 65),(1.2, 'Plate 12x24 Blue', 45),(1.2, 'Plate 12x24 Black', 76),(1.2, 'Plate 12x24 Orange', 15),(1.2, 'Plate 12x24 Yellow', 34),(.14, 'Flat Tile 1x6 Red', 45),(.14, 'Flat Tile 1x6 Blue', 56),(.14, 'Flat Tile 1x6 Black', 9),(.14, 'Flat Tile 1x6 Green', 89),(.14, 'Flat Tile 1x6 Yellow', 36),(.14, 'Flat Tile 1x6 Purple', 145),(.14, 'Flat Tile 1x6 White', 46),(.44, 'Wall Element 1x6x5 Red', 56),(.44, 'Wall Element 1x6x5 Yellow', 56),(.44, 'Wall Element 1x6x5 Blue', 56),(.44, 'Wall Element 1x6x5 White', 56),(.44, 'Wall Element 1x6x5 Black', 56);")
    MainServer.command("INSERT INTO full_set(set_description)VALUES('Set 1'),('Set 2'),('Set 3');")
    MainServer.command("INSERT INTO set_item(item_Id, set_itemQuantity, set_id)VALUES((SELECT item_id FROM item WHERE item_description = 'Plate 12x24 Red'), 2, (SELECT set_id FROM full_set WHERE set_description = 'Set 1')), ((SELECT item_id FROM item WHERE item_description = 'Plate 12x24 Orange'), 2, (SELECT set_id FROM full_set WHERE set_description = 'Set 1')), ((SELECT item_id FROM item WHERE item_description = 'Wall Element 1x6x5 Blue'), 2, (SELECT set_id FROM full_set WHERE set_description = 'Set 1')), ((SELECT item_id FROM item WHERE item_description = 'Brick 2x8 Orange'), 9, (SELECT set_id FROM full_set WHERE set_description = 'Set 1')), ((SELECT item_id FROM item WHERE item_description = 'Brick 1x8 Blue'), 15, (SELECT set_id FROM full_set WHERE set_description = 'Set 1')), ((SELECT item_id FROM item WHERE item_description = 'Brick 1x8 Orange'), 20, (SELECT set_id FROM full_set WHERE set_description = 'Set 2')),((SELECT item_id FROM item WHERE item_description = 'Brick 1x8 Red'), 10, (SELECT set_id FROM full_set WHERE set_description = 'Set 2')), ((SELECT item_id FROM item WHERE item_description = 'Person 1'), 1, (SELECT set_id FROM full_set WHERE set_description = 'Set 2')), ((SELECT item_id FROM item WHERE item_description = 'Person 3'), 1, (SELECT set_id FROM full_set WHERE set_description = 'Set 2')), ((SELECT item_id FROM item WHERE item_description = 'Plate 12x24 Yellow'), 4, (SELECT set_id FROM full_set WHERE set_description = 'Set 2')), ((SELECT item_id FROM item WHERE item_description = 'Plate 12x24 Orange'), 3, (SELECT set_id FROM full_set WHERE set_description = 'Set 2')), ((SELECT item_id FROM item WHERE item_description = 'Plate 12x24 Black'), 3, (SELECT set_id FROM full_set WHERE set_description = 'Set 3')),((SELECT item_id FROM item WHERE item_description = 'Person 6'), 1, (SELECT set_id FROM full_set WHERE set_description = 'Set 3')),((SELECT item_id FROM item WHERE item_description = 'Plate 4x4 Round Black'), 3, (SELECT set_id FROM full_set WHERE set_description = 'Set 3')),((SELECT item_id FROM item WHERE item_description = 'Wall Element 1x6x5 Black'), 4, (SELECT set_id FROM full_set WHERE set_description = 'Set 3')),((SELECT item_id FROM item WHERE item_description = 'Wall Element 1x6x5 Blue'), 3, (SELECT set_id FROM full_set WHERE set_description = 'Set 3')),((SELECT item_id FROM item WHERE item_description = 'Nose Cone Small'), 10, (SELECT set_id FROM full_set WHERE set_description = 'Set 3'));")
    MainServer.command("COMMIT TRANSACTION")
    MainServer.endConnection()
    print("Finished Making tables")


