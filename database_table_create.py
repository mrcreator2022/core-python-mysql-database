import pymysql as mq

conn = mq.connect(host="localhost",user="root",database="schools")

# try:
#     mysql =conn.cursor()
#     tc="create table student(st_id INT primary key auto_increment,st_name varchar(50),st_class varchar(10),st_email varchar(100))"
#     mysql.execute(tc)
#     print("Table created successfully")
# except:
#     print("Already table created")

# try:
#     mysql =conn.cursor()
#     tc="create table states(state_id INT primary key auto_increment,state_name varchar(50),country_id int(11))"
#     mysql.execute(tc)
#     print("Table created successfully")
# except:
#     print("Already table created")    


# try:
#     mysql =conn.cursor()
#     tc="create table orders(order_id INT primary key auto_increment,order_date datetime,user_id INT,order_amount varchar(255))"
#     mysql.execute(tc)
#     print("Table created successfully")
# except:
#     print("Already table created")

# try:
#     mysql =conn.cursor()
#     tc="create table categories(cat_id INT primary key auto_increment,cat_name varchar(50),parent_id INT)"
#     mysql.execute(tc)
#     print("Table created successfully")
# except:
#     print("Already table created")    

try:
    mysql =conn.cursor()
    tc="create table employees(emp_id INT primary key auto_increment,emp_name varchar(50),dname varchar(50))"
    mysql.execute(tc)
    print("Table created successfully")
except:
    print("Already table created")   