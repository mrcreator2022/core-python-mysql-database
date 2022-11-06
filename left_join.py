import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15} {:<20} {:<20}".format("State Id","State Name","Country Name"))

#queury all
try:
    #sql="Select * from students"
    sql = "Select states.state_id,states.state_name,countries.country_name from states left join countries on states.country_id=countries.country_id"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        #print(s)
        print("{:<15} {:<20} {:<20}".format(s[0],s[1],str(s[2])))
except:
    print("Error")
