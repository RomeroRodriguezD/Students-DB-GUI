import mysql.connector as sql

credenciales = {"host":"localhost",
            "user":"David",
            "passwd":"barberay2",
            "database":"NESE_BBDD"}

class Connection:

    bbdd_nese = sql.connect(  #Credenciales a variable externa e importada

            host="localhost",
            user="David",
            passwd="barberay2",
            database="NESE_BBDD"

        )

    cursor = bbdd_nese.cursor()

    credenciales = {"host":"localhost",
            "user":"David",
            "passwd":"barberay2",
            "database":"NESE_BBDD"}