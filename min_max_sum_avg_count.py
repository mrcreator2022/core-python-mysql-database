import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15}".format("Order Amount"))

#queury all
try:
    #sql="Select * from students"
    #sql = "Select min(order_amount) from orders"
    #sql = "Select max(order_amount) from orders"
    #sql = "Select sum(order_amount) from orders"
    #sql = "Select avg(order_amount) from orders"
    sql = "Select count(*) from orders"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        #print(s)
        print("{:<15}".format(s[0]))
except:
    print("Error")
