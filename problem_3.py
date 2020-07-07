from datetime import datetime
import pysftp
import mysql.connector

Db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="sftp"
)
mycursor = Db.cursor()

myHostname = "host_name"
myUsername = "username"
myPassword = "password"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print("Connection succesfully stablished ... ")

    # Switch to a remote directory
    sftp.cwd('/home/smsc/Documents/IMP')

    # Obtain structure of the remote directory '/var/www/vhosts'
    directory_structure = sftp.listdir_attr()

    # Print data
    a = []
    m = datetime.now()
    for attr in directory_structure:
        print(type(attr.filename))
        if attr.filename.endswith('.csv'):
            a.append(type(str(m) + attr.filename))
    print(a)

    # Define the file that you want to download from the remote directory
    dataFile = '/home/smsc/Documents/IMP/data.csv'


    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData


    file = convertToBinaryData(dataFile)
    # Define the local path where the file will be saved
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
    localFilePath = './TUTORIAL.txt'

    """
    My_Qurie = "INSERT INTO SFTP_table (file_data,Object_Name, Cell_ID,CallAttempts) VALUES(%s, %s, %s,%s)"
    val = [(file,,Object_Name,Cell_ID,CallAttempts)]
    mycursor.execute(My_Qurie, val)
    Db.commit()"""

    sftp.get(dataFile, localFilePath)
