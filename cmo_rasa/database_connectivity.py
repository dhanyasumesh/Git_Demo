import mysql.connector
def DataUpdate(mobile_no,file_no): 
    mydb = mysql.connector.connect( 
        host="localhost", 
        user="root",  
        password="password", 
        database="rasa_cmo",
        auth_plugin='mysql_native_password'
    ) 
    mycursor = mydb.cursor() 
    # sql="INSERT INTO `file_status` (`mobile_number`, `file_no`) VALUES ('{0}','{1}')".format(mobile_no,file_no)
    sql="SELECT * FROM `file_status` WHERE `mobile_number`='{0}' AND `file_no`='{1}'".format(mobile_no,file_no) 
    mycursor.execute(sql) 
    # mydb.commit()
    results = mycursor.fetchall()


    for row in results:
        # id = row[0]
        # mobile_no = row[1]
        # file_no = row[2]
        # status = row[3]
        return[row]
      # Now print fetched result
        # utter_message("Your current status is {} ".format(status)) 
        # json_message = {mobile_no: “Hello”, field1: “imp_val_1”, field2: “imp_val_2”}
        # dispatcher.utter_message("Your current status is {} ".format(status)) 


    # if __name__=="__main__":

DataUpdate('1212121212','KLTH2121')

