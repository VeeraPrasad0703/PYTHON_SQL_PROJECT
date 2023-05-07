import mysql.connector;
my_db=mysql.connector.connect(host='localhost',user='root',password='252771@Veera');
cur=my_db.cursor();
cur.execute('create database INVENTORY_MANAGEMENT_CONTROL');
