import mysql.connector
Db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="sftp"
)
con = Db.cursor()
con.execute("CREATE TABLE SFTP_table (id INT AUTO_INCREMENT PRIMARY KEY, Result_time DATETIME , file_data BLOB NOT "
            "NULL, Granularity_Period "
            "VARCHAR(255), Object_Name VARCHAR(255), Cell_ID VARCHAR(100), CallAttempts INT(234))")

