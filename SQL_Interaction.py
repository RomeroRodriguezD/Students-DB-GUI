
from tkinter import  messagebox
import pandas as pd
import psycopg2 as sql
from bbddcredentials import credenciales

class SQL_Interaction:   #Clase destinada a todas las interacciones con el modelo

    def SQL_Query(self, student):

        base_query = f'SELECT * FROM "NESE_BBDD"."ALUMNES" WHERE 1 = 1' #Sintaxis de postgres requiere comillas

        if student.nom != "":
            base_query += f" AND nom = '{student.nom}'"

        if student.cognom1 != "":
            base_query += f" AND cognom1 = '{student.cognom1}'"

        if student.cognom2 != "":
            base_query += f" AND cognom2 = '{student.cognom2}'"

        if student.materia != "":
            base_query += f" AND materia = '{student.materia}'"

        if student.tutor != "":
            base_query += f" AND tutor LIKE '%{student.tutor}%'"

        if student.consideraciones != "":
            base_query += f" AND consideracions LIKE '%{student.consideraciones}%'"

        if student.estat != "":
            base_query += f" AND estat = '{student.estat}'"

        if student.username != "":
            base_query += f" AND username = '{student.username}'"

        if student.cicle_fp != "":
            if student.cicle_fp == "FP":
                base_query += " AND cicle_fp NOT LIKE 'Batx' AND cicle_fp NOT LIKE 'GES'" # Filtra alumnes de FP sols
            else:
                base_query += f" AND cicle_fp = '{student.cicle_fp}'"

        if student.data != "":
            base_query += f" AND data_registre = '{student.data}'"

        base_query += ";"
        global query_table
        self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
        query_table = pd.read_sql_query(base_query, self.new_connection)
        self.new_connection.close()
        return query_table # Devuelve el dataframe que será cargado en el treeview

    def Agregar_Alumno(self, student):

        try:

            self.agregar = True
            self.nom = student.nom
            self.cognom1 = student.cognom1
            self.cognom2 = student.cognom2
            self.materia = student.materia
            self.tutor = student.tutor
            self.adaptacion = student.adaptaciones
            self.consideracion = student.consideraciones
            self.estat = student.estat
            self.username = student.username
            self.documents = student.documentos
            self.cicle_fp = student.cicle_fp
            self.data_registre = student.data

            self.base_query_add = f'INSERT into "NESE_BBDD"."ALUMNES" (nom, cognom1, cognom2, tutor, materia, consideracions, adaptacions, estat, documents, username, cicle_fp, data_registre) values ('
            #self.codigo_random = random.randint(1, 999999999)
            #self.base_query_add += f"'{self.codigo_random}',"  # Este generará el valor aleatorio de la row, para hacerla única en SQL.

            if self.nom != "":
                self.base_query_add += f"'{self.nom}',"

            else:
                self.agregar = False
                messagebox.showerror(title="Nom", message="No has introduit cap nom. No s'afegirà l'alumne.")

            if self.cognom1 != "":
                self.base_query_add += f" '{self.cognom1}',"

            else:
                self.agregar = False
                messagebox.showerror(title="Primer cognom",
                                     message="No has introduit cap primer cognom. No s'afegirà l'alumne.")

            if self.cognom2 != "":
                self.base_query_add += f" '{self.cognom2}',"

            else:
                self.agregar = False
                messagebox.showerror(title="Segon cognom",
                                     message="No has introduit cap segon cognom. No s'afegirà l'alumne.")

            if self.materia != "":
                self.base_query_add += f" '{self.materia}',"

            else:
                self.agregar = False
                messagebox.showerror(title="Materia", message="No has introduit cap materia. No s'afegirà l'alumne.")

            if self.tutor != "":
                self.base_query_add += f" '{self.tutor}',"

            if self.consideracion != "":
                self.base_query_add += f" '{self.consideracion}',"
            else:
                self.agregar = False
                messagebox.showerror(title="Consideració",
                                     message="No has introduit cap primer consideració. No s'afegirà l'alumne.")

            if self.adaptacion != "":
                self.base_query_add += f" '{self.adaptacion}',"
            else:
                self.base_query_add += " 'Sense adaptacions registrades',"

            if self.estat != "":
                self.base_query_add += f" '{self.estat}',"
            else:
                self.agregar = False
                messagebox.showerror(title="Estat", message="No has introduit cap estat. No s'afegirà l'alumne.")

            if self.documents != "":
                self.base_query_add += f" '{self.documents}',"
            else:
                self.base_query_add += " 'Pendent d'assignació',"

            if self.username != "":
                self.base_query_add += f" '{self.username}',"
            else:
                self.base_query_add += " 'Pendent d'assignació',"

            if self.cicle_fp != "":
                self.base_query_add += f" '{self.cicle_fp}',"

            else:
                self.base_query_add += " 'Pendent d'assignació',"

            if self.data_registre != "":
                self.base_query_add += f" '{self.data_registre}'"

            else:
                self.agregar = False
                messagebox.showerror(title="Data", message="No has introduit cap data.")

            self.base_query_add += ");"


            if self.agregar:
                self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
                #self.new_connection.cursor.execute(self.base_query_add)
                self.cursor = self.new_connection.cursor()
                self.cursor.execute(self.base_query_add)
                self.new_connection.commit() # Guarda la transacción
                self.new_connection.close()
                messagebox.showinfo(title="Alumne afegit", message="Alumne afegit amb èxit.")
        except:
            messagebox.showerror(title="error", message="Error en el registre, probablement coincidencia de codis identificatius, prova de nou.")

    def Agregar_Adaptacion(self, student):

        if student.adaptaciones != "" and student.username != "":

            try:

                self.adaptacion = student.adaptaciones
                self.username = student.username
                self.query = 'UPDATE "NESE_BBDD"."ALUMNES" set adaptacions ='
                self.query += f"'{self.adaptacion}' where username = '{self.username}';"
                self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
                self.cursor = self.new_connection.cursor()
                self.cursor.execute(self.query)
                self.new_connection.commit()  # Guarda la transacción
                self.new_connection.close()
                messagebox.showinfo(title="Adaptacions", message="Adaptacions afegides amb èxit.")
            except:
                messagebox.showerror(title="error", message="Error en el registre, revisi el paràmetre username.")

        else:
            messagebox.showerror(title="Falten dades", message="Introdueix adaptacions i username")

    def Agregar_Documentos(self, student):

        if student.documentos != "" and student.username != "":

             try:
                self.documentos = student.documentos
                self.username = student.username
                self.query = 'UPDATE "NESE_BBDD"."ALUMNES" set documents ='
                self.query += f"'{self.documentos}' where username = '{self.username}'"
                self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
                self.cursor = self.new_connection.cursor()
                self.cursor.execute(self.query)
                self.new_connection.commit()  # Guarda la transacción
                self.new_connection.close()
                messagebox.showinfo(title="Documentació", message="Documentacions afegides amb èxit.")


             except:
                messagebox.showerror(title="error", message="Error en el registre, revisi el paràmetre username.")

        else:
            messagebox.showerror(title="Falten dades", message="Introdueix documentació i username")

    def Actualizar_BBDD_Batx(self, data, dataframe):

        update = True

        try:

            self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
            query5= 'CREATE TABLE "NESE_BBDD"."TEMP" AS SELECT * FROM "NESE_BBDD"."ALUMNES";'

            self.cursor = self.new_connection.cursor()
            self.cursor.execute(query5)
            self.new_connection.commit()
            self.new_connection.close()
            # Esto para introducir nuevos datos totalmente de 0:
            for row in dataframe.itertuples():

                self.nom = row.nom
                self.cognom1 = row.cognom1
                self.cognom2 = row.cognom2
                self.materia = row.materia
                self.tutor = row.tutor
                self.consideraciones = row.observacions_ioc
                self.estat = 'Alta'
                self.username = row.username
                self.data = data
                self.ciclefp = 'Batx'
                self.sql_query = f'INSERT INTO "NESE_BBDD"."ALUMNES" (nom, cognom1, cognom2, materia, tutor, consideracions, estat, username, cicle_fp, data_registre) values ('
                self.sql_query += f"'{self.nom}', '{self.cognom1}', '{self.cognom2}', '{self.materia}', '{self.tutor}', '{self.consideraciones}', '{self.estat}', '{self.username}', '{self.ciclefp}', '{self.data}');"

                if self.data != "":
                    self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
                    self.cursor = self.new_connection.cursor()
                    self.cursor.execute(self.sql_query)
                    self.new_connection.commit()  # Guarda la transacción
                    self.new_connection.close()

            self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
            self.cursor = self.new_connection.cursor()
            query3 = 'UPDATE "NESE_BBDD"."ALUMNES" as b set estat = '
            query3 += "'Baixa' FROM "
            query3 += '"NESE_BBDD"."TEMP" as t where (t.username = b.username and t.data_registre = b.data_registre) and (b.cicle_fp = '
            query3 += "'Batx') and t.username not in (SELECT username FROM (SELECT * FROM"
            query3 += ' "NESE_BBDD"."ALUMNES") as a2 where data_registre = '
            query3 += f" '{self.data}' ) ;"
            self.cursor.execute(query3)
            query4 = 'DROP TABLE "NESE_BBDD"."TEMP";'
            self.cursor.execute(query4)
            self.new_connection.commit()
            self.new_connection.close()
        except:
            update=False
            messagebox.showinfo(title="Error",message="Carregui l'arxiu de nou i/o afegeixi data de registre.")

        if update:
            messagebox.showinfo(title="Carrega de dades completada", message="Base de dades actualitzada amb els nous registres")

    def Actualizar_BBDD_FP(self, data, dataframe):

        #update = True

        #try:

            self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'],database=credenciales['database'],port=credenciales['port'])
            query5 = 'CREATE TABLE "NESE_BBDD"."TEMP" AS SELECT * FROM "NESE_BBDD"."ALUMNES";'
            self.cursor = self.new_connection.cursor()
            self.cursor.execute(query5)
            self.new_connection.commit()
            self.new_connection.close()

            for row in dataframe.itertuples():

                row_moduls = row.moduls_matriculats.split(',')
                for modul in row_moduls:

                    self.nom = row.nom
                    self.cognom1 = row.cognom1
                    self.cognom2 = row.cognom2
                    self.materia = modul
                    self.tutor = row.tutor
                    self.consideraciones = row.observacions_ioc
                    self.estat = 'Alta'
                    self.username = row.username
                    self.cicle_fp = row.sigles_cicle_LOE
                    self.data = data
                    self.sql_query = f'INSERT INTO "NESE_BBDD"."ALUMNES" (nom, cognom1, cognom2, materia, tutor, consideracions, estat, username, cicle_fp, data_registre) values ('
                    self.sql_query += f"'{self.nom}', '{self.cognom1}', '{self.cognom2}', '{self.materia}', '{self.tutor}', '{self.consideraciones}', '{self.estat}', '{self.username}', '{self.cicle_fp}', '{self.data}');"
                    if self.data != "":
                        self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
                        self.cursor = self.new_connection.cursor()
                        self.cursor.execute(self.sql_query)
                        self.new_connection.commit()  # Guarda la transacción
                        self.new_connection.close()

            self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
            self.cursor = self.new_connection.cursor()
            query3 = 'UPDATE "NESE_BBDD"."ALUMNES" as b set estat = '
            query3 += "'Baixa' FROM "
            query3 += '"NESE_BBDD"."TEMP" as t where (t.username = b.username and t.data_registre = b.data_registre) and (b.cicle_fp != '
            query3 += "'Batx' or b.cicle_fp != 'GES') and t.username not in (SELECT username FROM (SELECT * FROM"
            query3 += ' "NESE_BBDD"."ALUMNES") as a2 where data_registre = '
            query3 += f" '{self.data}' ) ;"
            self.cursor.execute(query3)
            query4 = 'DROP TABLE "NESE_BBDD"."TEMP";'
            self.cursor.execute(query4)
            self.new_connection.commit()
            self.new_connection.close()

        #except:
         #   update = False
          #  messagebox.showinfo(title="Error", message="Per seguretat, carregui l'arxiu csv de nou i torni a actualitzar dades.\n Revisa que hi hagi data.")

        #if update:
            messagebox.showinfo(title="Carrega de dades completada", message="Base de dades actualitzada amb els nous registres")

    def Actualizar_BBDD_GES(self, data, dataframe):

        update = True

        try:

            self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
            query5 = 'CREATE TABLE "NESE_BBDD"."TEMP" AS SELECT * FROM "NESE_BBDD"."ALUMNES";'
            self.cursor = self.new_connection.cursor()
            self.cursor.execute(query5)
            self.new_connection.commit()
            self.new_connection.close()

            for row in dataframe.itertuples():

                self.nom = row.nom
                self.cognom1 = row.cognom1
                self.cognom2 = row.cognom2
                self.materia = row.materia
                self.tutor = row.tutor
                self.consideraciones = row.observacions_ioc
                self.estat = 'Alta'
                self.username = row.username
                self.data = data
                self.ciclefp = 'GES'
                self.sql_query = f'INSERT INTO "NESE_BBDD"."ALUMNES" (nom, cognom1, cognom2, materia, tutor, consideracions, estat, username, cicle_fp, data_registre) values ('
                self.sql_query += f"'{self.nom}', '{self.cognom1}', '{self.cognom2}', '{self.materia}', '{self.tutor}', '{self.consideraciones}', '{self.estat}', '{self.username}', '{self.ciclefp}', '{self.data}');"
                if self.data != "":
                    self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
                    self.cursor = self.new_connection.cursor()
                    self.cursor.execute(self.sql_query)
                    self.new_connection.commit()  # Guarda la transacción
                    self.new_connection.close()

            self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
            self.cursor = self.new_connection.cursor()
            query3 = 'UPDATE "NESE_BBDD"."ALUMNES" as b set estat = '
            query3 += "'Baixa' FROM "
            query3 += '"NESE_BBDD"."TEMP" as t where (t.username = b.username and t.data_registre = b.data_registre) and (b.cicle_fp = '
            query3 += "'GES') and t.username not in (SELECT username FROM (SELECT * FROM"
            query3 += ' "NESE_BBDD"."ALUMNES") as a2 where data_registre = '
            query3 += f" '{self.data}' ) ;"
            self.cursor.execute(query3)
            query4 = 'DROP TABLE "NESE_BBDD"."TEMP";'
            self.cursor.execute(query4)
            self.new_connection.commit()
            self.new_connection.close()

        except:
            update = False
            messagebox.showinfo(title="Error",message="Carregui l'arxiu de nou i/o afegeixi data de registre.")

        if update:
            messagebox.showinfo(title="Carrega de dades completada", message="Base de dades actualitzada amb els nous registres")

    def Exportar_Excel(self):

        global base_query
        self.new_connection = self.new_connection = sql.connect(host=credenciales['host'],user=credenciales['user'], password=credenciales['passwd'], database = credenciales['database'], port=credenciales['port'])
        query_table = pd.read_sql_query(base_query, self.new_connection)
        self.new_connection.close()
        query_table.to_csv('./Cerca.csv')

