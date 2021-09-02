"""
Script to create MySQL db Indeed
"""
import mysql.connector as mysql
import config

def create_database():
    """
    Create Indeed db
    """
    print("Creating Database...")

    HOST = config.HOST
    USER = config.USER
    PASSWD = config.PASSWD

    db = mysql.connect(
        host = HOST,
        user = USER,
        passwd = PASSWD)

    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE spam_of_the_dead")

    print("...Database creation OK !")

def create_table():
    HOST = config.HOST
    USER = config.USER
    PASSWD = config.PASSWD

    db = mysql.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        auth_plugin='mysql_native_password',
        database="spam_of_the_dead")

    mycursor = db.cursor()

    mycursor.execute('CREATE TABLE emails'
                     '(email_id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, '
                     'email VARCHAR(10000), '
                     'label INT(2),'
                     'level INT(2)); ')

    print("Table created")
