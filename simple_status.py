import mysql.connector, random,string
from datetime import datetime
cnx = mysql.connector.connect  (host='192.168.112.130',user='client1',password='clientpass', database='clustertest', auth_plugin='caching_sha2_password')

if cnx.is_connected():
        db_Info = cnx.get_server_info()
        print(db_Info)


#============================================

cursor = cnx.cursor(buffered=True)



mySql_Create_Table_Query = "SELECT VERSION();"
cursor.execute(mySql_Create_Table_Query)
record = cursor.fetchone()
print("\tQR:",mySql_Create_Table_Query,"\n\tRS: ", record)

print("*"*20);
mySql_Create_Table_Query = "SHOW tables;"
cursor.execute(mySql_Create_Table_Query)
record = cursor.fetchone()
print("\tQR:",mySql_Create_Table_Query,"\n\tRS: ", record)


print("*"*20);
mySql_Create_Table_Query = "SHOW COLUMNS FROM MyGuests;"
cursor.execute(mySql_Create_Table_Query)
record = cursor.fetchone()
print("\tQR:",mySql_Create_Table_Query,"\n\tRS: ", record)

print("*"*20);
mySql_Create_Table_Query = "select count(*)  as 'records Fish' from fishcontrol.fish;"
cursor.execute(mySql_Create_Table_Query)
record = cursor.fetchone()
print("\tQR:",mySql_Create_Table_Query,"\n\tRS: ", record)

print("*"*20);
mySql_Create_Table_Query = "select count(*)  as 'records MyGuests' from clustertest.MyGuests;"
cursor.execute(mySql_Create_Table_Query)
record = cursor.fetchone()
print("\tQR:",mySql_Create_Table_Query,"\n\tRS: ", record)

max = 300000

if input("write test:")=="y":
    for i in range(1,max):
        mySql_Create_Table_Query = "INSERT INTO clustertest.MyGuests ( firstname, lastname, email) VALUES ('nguyen','vo phuoc', 'email@') ;"
        cursor.execute(mySql_Create_Table_Query)

        mySql_Create_Table_Query = "INSERT INTO fishcontrol.fish ( name, length_mm, weight_gm) VALUES ('"+ ''.join(random.choice(string.ascii_lowercase) for i in range(10))+ "','33', '111') ;"
        cursor.execute(mySql_Create_Table_Query)

        if (i % 500) == 0 : cnx.commit()
        if (i/max*100 % 0.5) ==0 : print(i/max*100 )



#
#






#================
cnx.close()
