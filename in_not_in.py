import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15} {:<15}".format("Order Id","Order Amount"))

#queury all
try:
    #sql = "Select order_id,order_amount from orders where order_id in(1,3)"
    sql = "Select order_id,order_amount from orders where order_id not in(1,3)"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        #print(s)
        print("{:<15} {:<15}".format(s[0],s[1]))
except:
    print("Error")
