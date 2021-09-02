import mysql.connector as mysql
import config
from config import HOST, USER, PASSWD

def insert_information(email, label,level):
    """
    This function insert provided data in database
    """

    db = mysql.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        auth_plugin='mysql_native_password',
        database="spam_of_the_dead")
    mycursor = db.cursor()
    mycursor.execute(
        'INSERT INTO emails (email,  label, level) values (%s, %s, %s)',
        (email, label, level))
    db.commit()
    print("Insert email information: OK !")