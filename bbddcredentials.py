import mysql.connector as sql

class Connection:

    bbdd_nese = sql.connect(

            host="localhost",
            user="david",
            passwd="password",
            database="Students_BBDD"

        )

    cursor = bbdd_nese.cursor()