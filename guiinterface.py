from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import random
from bbddcredentials import Connection as connection




class Interface:

    considerations = ["[NESE_A10]", "[NESE_B10]", "[NESE_B20]",
                       "[NESE_B30]", "[NESE_B40]", "[NESE_C10]",
                       "[NESE_D10]", "[NESE_D20]", "[NESE_D30]",
                       "[NESE_E10]", "[NESE_F10]", "[NESE_G10]",
                       "[NESE_H10]", "[NESE_I10]", "[NESE_J10]",
                       "[NESE_K10]", "[NESE_K20]",
                       "[NESE_M10]", "[NESE_Z10]", "[NESE_MG]", "[NESE_VG]"]

    considerations = ["[NESE_A10] Discapacitat intel·lectual lleugera", "[NESE_B10] Discapacitat auditiva lleugera",
                       "[NESE_B20] Discapacitat autivida mitjana",
                       "[NESE_B30] Discapacitat auditiva severa", "[NESE_B40] Discapacitat auditiva profunda",
                       "[NESE_C10] Discapacitat visual",
                       "[NESE_D10] Discapacitat motriu: autònom", "[NESE_D20] Discapacitat motriu: semiautònom",
                       "[NESE_D30] Discapacitat motriu: depenent",
                       "[NESE_E10] Trastorn de espectre de autisme", "[NESE_F10] Trastorn greu de la conducta",
                       "[NESE_G10] Retard del desenvolupament sense etiologia clara",
                       "[NESE_H10] Alumnat nouvingut",
                       "[NESE_I10] Situacions socioeconòmiques i/o culturals desafavorides",
                       "[NESE_J10] Altes capacitats",
                       "[NESE_K10] Trastorns que condicionen aprenentatge: Dislèxia, TDAH, Discalculia, TEL",
                       "[NESE_K20] Retard greu d'aprenentatge",
                       "[NESE_M10] Trastorn mental greu", "[NESE_Z10] Pluridiscapacitat", "[NESE_MG] Malaltia greu",
                       "[NESE_VG] Violència de gènere"]


    materies = ["Llengua Catalana i Literatura", "Llengua Castellana i Literatura", "LLengua Estrangera", "Educacio Física", "Filosofía"]


    estados_matricula = ["Alta", "Baixa", "Aspirant"]

    def __init__(self, connection):

        self.window = Tk()
        self.window.title("Students Database")
        self.window.pack_propagate(False)  # tells the root to not let the widgets inside it determine its size.
        self.window.resizable(0, 0)  # makes the root window fixed in size.
        self.window.geometry("800x450")
        self.window.protocol("WM_DELETE_WINDOW", func=self.Close_BBDD)
        self.set_notebook()
        self.set_treeview()
        self.set_search()
        self.set_agregar()
        self.set_adaptaciones()
        self.set_documentos()
        self.set_consideraciones()
        self.set_upload()
        self.window.mainloop()

    def set_notebook(self):

        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill="both", expand="Yes")
        self.consulta_frame = ttk.Frame(self.notebook)
        self.ventana_consultas = self.notebook.add(self.consulta_frame, text="Search")
        self.frame_agregar = ttk.Frame(self.notebook)
        self.ventana_agregar = self.notebook.add(self.frame_agregar, text="Add student")
        self.adaptaciones_frame = ttk.Frame(self.notebook)
        self.ventana_adaptaciones = self.notebook.add(self.adaptaciones_frame, text="Add adaptations")
        self.documentos_frame = ttk.Frame(self.notebook)
        self.documentos_ventana = self.notebook.add(self.documentos_frame, text="Add documents")
        self.upload_frame = ttk.Frame(self.notebook)
        self.ventana_upload = self.notebook.add(self.upload_frame, text="Update database")
        self.consideraciones_frame = ttk.Frame(self.notebook)
        self.ventana_consideraciones = self.notebook.add(self.consideraciones_frame, text="Code list")


    def set_treeview(self):
        # Frame para el TreeView
        self.frame1 = LabelFrame(self.consulta_frame, text="SQL Data")
        self.frame1.place(height=200, width=800)

        ## Treeview
        self.tv1 = ttk.Treeview(self.frame1)
        self.tv1.place(relheight=1, relwidth=1)
        self.treescrolly = Scrollbar(self.frame1, orient="vertical", command=self.tv1.yview)  # command means update the yaxis view of the widget
        self.treescrollx = Scrollbar(self.frame1, orient="horizontal",command=self.tv1.xview)  # command means update the xaxis view of the widget
        self.tv1.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set)  # assign the scrollbars to the Treeview Widget
        self.treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
        self.treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

    def set_search(self):

        lista_tutores = ['Joan Marc Turon Dols', 'Helena Cegarra Ribas', 'Olga Torija de la Riva', 'Sandra Toboso',
                         'Silvia Salomó', 'Pere Chacon', 'Joan Puig',
                         'David Torres Velasco', 'Pere Bosch', 'Maria Carretero Ferrándiz', 'Santiago Cerezo Salcedo',
                         'Joan Carles Pérez', 'Carles Martí Hernández',
                         'Joan Ramon Serret Nadal', 'Alicia Vila', 'Olga Bresco', 'Pilar Gimenez', 'Berta Nicolau',
                         'Cristian Jordà', 'Cuntxi López', 'Ana Mora',
                         'Eva Carredas Salvado', 'Carme Martín']

        # Frame para todas las Entry y el botón de búsqueda

        self.busqueda_frame = LabelFrame(self.consulta_frame, text="Selection criteria")
        self.busqueda_frame.place(height=120, width=780, rely=0.47, relx=0.014)  # Dejar así fijado el ancho y las rel x e y.

        # Nom
        self.nom_label = Label(self.busqueda_frame, text="Name")
        self.nom_label.place(relx=0.01, rely=0)
        self.nom_entry = Entry(self.busqueda_frame)
        self.nom_entry.place(relx=0.01, rely=0.25, width=100)

        # Cognom1
        self.cognom1_label = Label(self.busqueda_frame, text="1s surname")
        self.cognom1_label.place(relx=0.15, rely=0)
        self.cognom1_entry = Entry(self.busqueda_frame)
        self.cognom1_entry.place(relx=0.15, rely=0.25, width=100)

        # Cognom2
        self.cognom2_label = Label(self.busqueda_frame, text="2d surname")
        self.cognom2_label.place(relx=0.29, rely=0)
        self.cognom2_entry = Entry(self.busqueda_frame)
        self.cognom2_entry.place(relx=0.29, rely=0.25, width=100)

        #  Materia
        self.materia_label = Label(self.busqueda_frame, text="Subject")
        self.materia_label.place(relx=0.43, rely=0)
        self.materia_combobox = ttk.Combobox(self.busqueda_frame)
        self.materia_combobox.place(relx=0.43, rely=0.25, width=100)
        self.materia_combobox['values'] = Interfaz.materies

        # Tutor
        self.tutor_label = Label(self.busqueda_frame, text="Tutor")
        self.tutor_label.place(relx=0.57, rely=0)
        self.tutor_entry = ttk.Combobox(self.busqueda_frame)
        self.tutor_entry.place(relx=0.57, rely=0.25, width=100)
        self.tutor_entry['values']= lista_tutores

        # consideraciones
        self.consideraciones_label1 = Label(self.busqueda_frame, text="Consideration")
        self.consideraciones_label1.place(relx=0.71, rely=0)
        self.consideraciones_busqueda = ttk.Combobox(self.busqueda_frame)
        self.consideraciones_busqueda.place(relx=0.71, rely=0.25, width=100)
        self.consideraciones_busqueda['values'] = self.consideraciones

        # Estat
        self.estat_label1 = Label(self.busqueda_frame, text="Current state")
        self.estat_label1.place(relx=0.85, rely=0)
        self.estat_combobox = ttk.Combobox(self.busqueda_frame)
        self.estat_combobox.place(relx=0.85, rely=0.25, width=100)
        self.estat_combobox['values'] = Interfaz.estados_matricula

        # username
        self.username_label1 = Label(self.busqueda_frame, text="Username")
        self.username_label1.place(relx=0.01, rely=0.5)
        self.username_entry1 = Entry(self.busqueda_frame)
        self.username_entry1.place(relx=0.01, rely=0.7, width=100)

        # fecha alta

        self.fecha_label1 = Label(self.busqueda_frame, text="Registration date")
        self.fecha_label1.place(relx=0.15, rely=0.5)
        self.fecha_entry1 = Entry(self.busqueda_frame)
        self.fecha_entry1.place(relx=0.15, rely=0.7, width=100)

        # cicle, en cas d'FP

        self.ciclefp_label1 = Label(self.busqueda_frame, text="Course")
        self.ciclefp_label1.place(relx=0.29, rely=0.5)
        self.ciclefp_entry1 = Entry(self.busqueda_frame)
        self.ciclefp_entry1.place(relx=0.29, rely=0.7, width=100)

        ######## Botón de Búsqueda (Función SELECT SQL) ######
        self.busqueda_button = Button(self.busqueda_frame, text="Search", command=self.SQL_Query) # setconfig externos?
        self.busqueda_button.place(relx=0.85, rely=0.55, width=100)

        ####### Botón para exportar el resultado #######
        self.exportar_button = Button(self.consulta_frame, text="Export", command=self.Exportar_Excel)  # Nota: Exportar con un índice autogenerado.
        self.exportar_button.place(relx=0.75, rely=0.78)


    def set_agregar(self):

        lista_tutores = ['Joan Marc Turon Dols', 'Helena Cegarra Ribas', 'Olga Torija de la Riva', 'Sandra Toboso',
                         'Silvia Salomó', 'Pere Chacon', 'Joan Puig',
                         'David Torres Velasco', 'Pere Bosch', 'Maria Carretero Ferrándiz', 'Santiago Cerezo Salcedo',
                         'Joan Carles Pérez', 'Carles Martí Hernández',
                         'Joan Ramon Serret Nadal', 'Alicia Vila', 'Olga Bresco', 'Pilar Gimenez', 'Berta Nicolau',
                         'Cristian Jordà', 'Cuntxi López', 'Ana Mora',
                         'Eva Carredas Salvado', 'Carme Martín']

        # Frame para todas las Entry y el botón de búsqueda
        self.agregar_frame = LabelFrame(self.frame_agregar, text="Criteria")
        self.agregar_frame.place(height=400, width=780, rely=0.05, relx=0.014)  # Dejar así fijado el ancho y las rel x e y.

        # Nom
        self.nom_label2 = Label(self.agregar_frame, text="Name")
        self.nom_label2.place(relx=0.01, rely=0)
        self.nom_entry2 = Entry(self.agregar_frame)
        self.nom_entry2.place(relx=0.01, rely=0.05, width=100)

        # Cognom1
        self.cognom1_label2 = Label(self.agregar_frame, text="1s surname")
        self.cognom1_label2.place(relx=0.15, rely=0)
        self.cognom1_entry2 = Entry(self.agregar_frame)
        self.cognom1_entry2.place(relx=0.15, rely=0.05, width=100)

        # Cognom2
        self.cognom2_label2 = Label(self.agregar_frame, text="2d surname")
        self.cognom2_label2.place(relx=0.29, rely=0)
        self.cognom2_entry2 = Entry(self.agregar_frame)
        self.cognom2_entry2.place(relx=0.29, rely=0.05, width=100)

        # Materia
        self.materia_label2 = Label(self.agregar_frame, text="Subject")
        self.materia_label2.place(relx=0.43, rely=0)
        self.materia_combobox2 = ttk.Combobox(self.agregar_frame)
        self.materia_combobox2.place(relx=0.43, rely=0.05, width=100)
        self.materia_combobox2['values'] = Interfaz.materies

        # Tutor
        self.tutor_label2 = Label(self.agregar_frame, text="Tutor")
        self.tutor_label2.place(relx=0.57, rely=0)
        self.tutor_entry2 = ttk.Combobox(self.agregar_frame)
        self.tutor_entry2.place(relx=0.57, rely=0.05, width=100)
        self.tutor_entry2['values']=lista_tutores

        # Adaptacions
        self.adaptacion_label = Label(self.agregar_frame, text="Adaptation")
        self.adaptacion_label.place(relx=0.01, rely=0.3)
        self.adaptacion_entry = Text(self.agregar_frame)
        self.adaptacion_entry.place(height=200, width=300, relx=0.01, rely=0.35)

        # Label Consideracions y lista
        self.consideracions_label = Label(self.agregar_frame, text="Consideration")
        self.consideracions_label.place(relx=0.5, rely=0.3)
        self.consideracion_lista = ttk.Combobox(self.agregar_frame)
        self.consideracion_lista.place(height=20, width=300, relx=0.5, rely=0.35)
        self.consideracion_lista['values'] = Interfaz.consideraciones

        # Estat
        self.estat_label2 = Label(self.agregar_frame, text="Current state")
        self.estat_label2.place(relx=0.01, rely=0.15)
        self.estat_combobox2 = ttk.Combobox(self.agregar_frame)
        self.estat_combobox2.place(relx=0.01, rely=0.2, width=100)
        self.estat_combobox2['values'] = self.estados_matricula

        # Documents
        self.documents_label = Label(self.agregar_frame, text="Documentation")
        self.documents_label.place(relx=0.5, rely=0.40)
        self.documents_text = Text(self.agregar_frame)
        self.documents_text.place(relx=0.5, rely=0.45, height=161, width=200)

        # ¿username? ->
        self.username_label3 = Label(self.agregar_frame, text="Username")
        self.username_label3.place(relx=0.15, rely=0.15)
        self.username_entry3 = Entry(self.agregar_frame)
        self.username_entry3.place(relx=0.15, rely=0.2, width=100)

        # Fecha
        self.fecha_label2 = Label(self.agregar_frame, text="Registration date")
        self.fecha_label2.place(relx=0.29, rely=0.15)
        self.fecha_entry2 = Entry(self.agregar_frame)
        self.fecha_entry2.place(relx=0.29, rely=0.2, width=100)

        # Cicle FP

        self.ciclefp_label2 = Label(self.agregar_frame, text="Course")
        self.ciclefp_label2.place(relx=0.43, rely=0.15)
        self.ciclefp_entry2 = Entry(self.agregar_frame)
        self.ciclefp_entry2.place(relx=0.43, rely=0.2, width=100)

        # Botón de añadir alumno
        self.afegir_button = Button(self.agregar_frame, text="Add student", command=self.Agregar_Alumno)
        self.afegir_button.place(relx=0.8, rely=0.04)

    def set_adaptaciones(self):

        self.adaptacions_labelframe = LabelFrame(self.adaptaciones_frame, text="Introduce username to update adaptations")
        self.adaptacions_labelframe.place(height=400, width=780, rely=0.05, relx=0.014)  # Dejar así fijado el ancho y las rel x e y.
        self.adaptacion_modificaciones = Text(self.adaptaciones_frame)
        self.adaptacion_modificaciones.place(relx=0.02, rely=0.10, height=350, width=400)

        # username
        self.username_label2 = Label(self.adaptaciones_frame, text="Username")
        self.username_label2.place(relx=0.6, rely=0.10)
        self.username_entry2 = Entry(self.adaptaciones_frame)
        self.username_entry2.place(relx=0.6, rely=0.15, width=100)

        # Botón de modificación
        self.agregar_adaptacion = Button(self.adaptaciones_frame, text="Add adaptation", command=self.Agregar_Adaptacion)
        self.agregar_adaptacion.place(relx=0.6, rely=0.22, width=150)

    def set_documentos(self):

        self.documentos_labelframe = LabelFrame(self.documentos_frame, text="Introduce username to update documents")
        self.documentos_labelframe.place(height=400, width=780, rely=0.05, relx=0.014)  # Dejar así fijado el ancho y las rel x e y.
        self.documentacion_modificaciones = Text(self.documentos_frame)
        self.documentacion_modificaciones.place(relx=0.02, rely=0.10, height=350, width=400)

        # username
        self.username_label4 = Label(self.documentos_frame, text="Username")
        self.username_label4.place(relx=0.6, rely=0.10)
        self.username_entry4 = Entry(self.documentos_frame)
        self.username_entry4.place(relx=0.6, rely=0.15, width=100)

        # Botón de modificación
        self.agregar_documentos = Button(self.documentos_frame, text="Afegir documentació", command=self.Agregar_Documentos)
        self.agregar_documentos.place(relx=0.6, rely=0.22, width=150)

    def set_upload(self):

        self.upload_labelframe = LabelFrame(self.upload_frame)
        self.upload_labelframe.place(height=400, width=780, rely=0.05,relx=0.014)  # Dejar así fijado el ancho y las rel x e y.
        self.cargar_button = Button(self.upload_labelframe, text="Open file", command=self.Cargar_CSV)
        self.cargar_button.place(relx=0.05, rely=0.05)
        self.ruta_label = Label(self.upload_labelframe, text="Loaded file: None")
        self.ruta_label.place(relx=0.20, rely=0.07)
        self.actualizar_button = Button(self.upload_labelframe, text="Update Batx Database", command=self.Actualizar_BBDD_Batx)
        self.actualizar_button.place(relx=0.05, rely=0.35)
        self.actualizarFP_button = Button(self.upload_labelframe, text="Update FP Database", command=self.Actualizar_BBDD_FP)
        self.actualizarFP_button.place(relx=0.05, rely=0.45)
        self.actualizarFP_button = Button(self.upload_labelframe, text="Update GES Database", command=self.Actualizar_BBDD_GES)
        self.actualizarFP_button.place(relx=0.05, rely=0.55)
        self.fecha_actualizacion_label = Label(self.upload_labelframe, text="Registration date DD/MM/AAAA")
        self.fecha_actualizacion_label.place(relx=0.05, rely=0.2)
        self.fecha_actualizacion = Entry(self.upload_labelframe)
        self.fecha_actualizacion.place(relx=0.05, rely=0.25, width=100)

    def set_consideraciones(self):

        consideraciones_fullname = ["[NESE_00]","[NESE_A10] Discapacitat intel·lectual lleugera",
                                    "[NESE_B10] Discapacitat auditiva lleugera",
                                    "[NESE_B20] Discapacitat autivida mitjana",
                                    "[NESE_B30] Discapacitat auditiva severa",
                                    "[NESE_B40] Discapacitat auditiva profunda",
                                    "[NESE_C10] Discapacitat visual",
                                    "[NESE_D10] Discapacitat motriu: autònom",
                                    "[NESE_D20] Discapacitat motriu: semiautònom",
                                    "[NESE_D30] Discapacitat motriu: depenent",
                                    "[NESE_E10] Trastorn de espectre de autisme",
                                    "[NESE_F10] Trastorn greu de la conducta",
                                    "[NESE_G10] Retard del desenvolupament sense etiologia clara",
                                    "[NESE_H10] Alumnat nouvingut",
                                    "[NESE_I10] Situacions socioeconòmiques i/o culturals desafavorides",
                                    "[NESE_J10] Altes capacitats",
                                    "[NESE_K10] Trastorns que condicionen aprenentatge: Dislèxia, TDAH, Discalculia, TEL",
                                    "[NESE_K20] Retard greu d'aprenentatge",
                                    "[NESE_M10] Trastorn mental greu", "[NESE_Z10] Pluridiscapacitat",
                                    "[NESE_MG] Malaltia greu",
                                    "[NESE_VG] Violència de gènere"]

        self.consideraciones_labelframe = LabelFrame(self.consideraciones_frame, text="Code list")
        self.consideraciones_labelframe.place(height=400, width=780, rely=0.05,relx=0.014)  # Dejar así fijado el ancho y las rel x e y.
        self.consideraciones_lista = Listbox(self.consideraciones_labelframe)
        self.consideraciones_lista.place(relx=0.02, rely=0.05, width=580, height=300)
        for i in consideraciones_fullname:
            self.consideraciones_lista.insert(END,i)

    def SQL_Query(self):

        global base_query
        base_query = f"SELECT * FROM ALUMNES WHERE 1 = 1"
        self.nom_input = str(self.nom_entry.get())
        self.cognom1_input = str(self.cognom1_entry.get())
        self.cognom2_input = str(self.cognom2_entry.get())
        self.materia_input = str(self.materia_combobox.get())
        self.tutor_input = str(self.tutor_entry.get())
        self.consideracion_input = str(self.consideraciones_busqueda.get())
        self.estat = str(self.estat_combobox.get())
        self.username = str(self.username_entry1.get())
        self.ciclefp = str(self.ciclefp_entry1.get())
        self.data = str(self.fecha_entry1.get())

        if self.nom_input != "":
            base_query += f" AND nom = '{self.nom_input}'"

        if self.cognom1_input != "":
            base_query += f" AND cognom1 = '{self.cognom1_input}'"

        if self.cognom2_input != "":
            base_query += f" AND cognom2 = '{self.cognom2_input}'"

        if self.materia_input != "":
            base_query += f" AND materia = '{self.materia_input}'"

        if self.tutor_input != "":
            base_query += f" AND tutor LIKE '%{self.tutor_input}%'"

        if self.consideracion_input != "":
            base_query += f" AND consideracions LIKE '%{self.consideracion_input}%'"

        if self.estat != "":
            base_query += f" AND estat = '{self.estat}'"

        if self.username != "":
            base_query += f" AND username = '{self.username}'"

        if self.ciclefp != "":
            base_query += f" AND cicle_fp = '{self.ciclefp}'"

        if self.data != "":
            base_query += f" AND data_registre = '{self.data}'"

        base_query += ";"
        print(base_query)
        # cursor.execute(base_query)
        global query_table
        query_table = pd.read_sql_query(base_query, connection.bbdd_nese)
        print(query_table)

        self.Load_SQL_data()

    def Exportar_Excel(self):

        global base_query
        query_table = pd.read_sql_query(base_query, connection.bbdd_nese)
        table2 = query_table.to_csv()
        #guardar_consulta = filedialog.asksaveasfile(mode="w", defaultextension=".xlsx")
        #query_table.to_excel(guardar_consulta.name)
        #messagebox.showinfo(title="miau", message=f"{guardar_consulta.name}")
        #query_table.to_excel(guardar_consulta.name)
        query_table.to_csv('./Cerca.csv')


    def Load_SQL_data(self):

        """Uploads SQL database on Treeview"""

        self.clear_data()
        self.tv1["column"] = list(query_table.columns)
        self.tv1["show"] = "headings"

        for column in self.tv1["columns"]:
            self.tv1.heading(column, text=column)  # cabecera de columna = nombre de columna

        df_rows = query_table.to_numpy().tolist()  # Vuelve el DataFrame una lista de listas.

        for row in df_rows:
            self.tv1.insert("", "end",values=row)  # Inserta cada lista en el treeview. Parámetros en https://docs.python.org/3/library/tkttk.html#tkttk.Treeview.insert

        return None

    def clear_data(self):  # Limpia el contenido del treeview para poner otra consulta
        self.tv1.delete(*self.tv1.get_children())
        return None

    def Agregar_Alumno(self):

        try:

            self.agregar = True
            self.nom = str(self.nom_entry2.get())
            self.cognom1 = str(self.cognom1_entry2.get())
            self.cognom2 = str(self.cognom2_entry2.get())
            self.materia = str(self.materia_combobox2.get())
            self.tutor = str(self.tutor_entry2.get())
            self.adaptacion = str(self.adaptacion_entry.get(1.0, END))
            self.consideracion = str(self.consideracion_lista.get())
            self.estat = str(self.estat_combobox2.get())
            self.username = str(self.username_entry3.get())
            self.documents = str(self.documents_text.get(1.0, END))
            self.ciclefp = str(self.ciclefp_entry2.get()) #TODO
            self.data_registre = str(self.fecha_entry2.get())

            self.base_query_add = f"INSERT into ALUMNES (codi, nom, cognom1, cognom2, tutor, materia, consideracions, adaptacions, estat, documents, username, cicle_fp, data_registre) values ("
            self.codigo_random = random.randint(1, 999999999)
            self.base_query_add += f"'{self.codigo_random}',"  # Este generará el valor aleatorio de la row, para hacerla única en SQL.

            if self.nom != "":
                self.base_query_add += f"'{self.nom}',"

            else:
                self.agregar = False
                messagebox.showerror(title="Name", message="Introduce name.")

            if self.cognom1 != "":
                self.base_query_add += f" '{self.cognom1}',"

            else:
                self.agregar = False
                messagebox.showerror(title="1s surname",
                                     message="Introduce surname.")

            if self.cognom2 != "":
                self.base_query_add += f" '{self.cognom2}',"

            else:
                self.agregar = False
                messagebox.showerror(title="2d surname",
                                     message="Introduce surname.")

            if self.materia != "":
                self.base_query_add += f" '{self.materia}',"

            else:
                self.agregar = False
                messagebox.showerror(title="Subject", message="Introduce subject.")

            if self.tutor != "":
                self.base_query_add += f" '{self.tutor}',"

            else:
                self.agregar = False
                messagebox.showerror(title="Tutor", message="Introduce tutor.")

            if self.consideracion != "":
                self.base_query_add += f" '{self.consideracion}',"
            else:
                self.agregar = False
                messagebox.showerror(title="Considerations", message="Choose a consideration.")

            if self.adaptacion != "":
                self.base_query_add += f" '{self.adaptacion}',"
            else:
                self.base_query_add += " 'No adaptation registered',"

            if self.estat != "":
                self.base_query_add += f" '{self.estat}',"
            else:
                self.agregar = False
                messagebox.showerror(title="Current state", message="Add a current state")

            if self.documents != "":
                self.base_query_add += f" '{self.documents}',"
            else:
                self.base_query_add += " 'Not added yet',"

            if self.username != "":
                self.base_query_add += f" '{self.username}',"
            else:
                self.base_query_add += " 'Not added yet',"

            if self.ciclefp != "":
                self.base_query_add += f" '{self.ciclefp}',"

            else:
                self.base_query_add += " 'Batx/GES',"

            if self.data_registre != "":
                self.base_query_add += f" '{self.data_registre}'"

            else:
                self.agregar = False
                messagebox.showerror(title="Data", message="No has introduit cap data.")

            self.base_query_add += ");"

            global cursor

            if self.agregar:
                print(self.base_query_add)
                connection.cursor.execute(self.base_query_add)
                connection.bbdd_nese.commit()
                messagebox.showinfo(title="Student added", message="Student added successfully.")
        except:
            messagebox.showerror(title="Error", message="Register error")

    def Agregar_Adaptacion(self):

        try:
            self.adaptacion = str(self.adaptacion_modificaciones.get(1.0, END))
            self.username = str(self.username_entry2.get())
            self.query = f"UPDATE ALUMNES set adaptacions = '{self.adaptacion}' where username = '{self.username}'"
            global cursor
            connection.cursor.execute(self.query)
            connection.bbdd_nese.commit()

        except:

            messagebox.showerror(title="error", text="Register error")

        self.adaptacion_modificaciones.delete(0, END)

    def Agregar_Documentos(self):

         try:
            self.documentos = str(self.documentacion_modificaciones.get(1.0, END))
            self.username = str(self.username_entry4.get())
            self.query = f"UPDATE ALUMNES set documents = '{self.documentos}' where username = '{self.username}'"
            global cursor
            connection.cursor.execute(self.query)
            connection.bbdd_nese.commit()

         except:
            messagebox.showerror(title="error", text="Register error")

         self.documentacion_modificaciones.delete(0, END)

    def Cargar_CSV(self):

        try:
            self.archivo = filedialog.askopenfile(mode="r", filetypes=[("Comma separated values", "*.csv"), ("All files", "*.*")])
            self.ruta_label.config(text=f"Loaded file: {self.archivo.name}")

        except AttributeError:
            pass

    def Actualizar_BBDD_Batx(self):

        try:

            self.dataframe = pd.read_csv(self.archivo)
            self.dataframe.replace('\'',' ', regex=True, inplace=True)

            # Esto para introducir nuevos datos totalmente de 0:
            for row in self.dataframe.itertuples():
                self.codi = random.randint(1, 999999999)
                self.nom = row.nom
                self.cognom1 = row.cognom1
                self.cognom2 = row.cognom2
                self.materia = row.materia
                self.tutor = row.tutor
                self.consideraciones = row.observacions_ioc
                self.estat = 'Alta'
                self.username = row.username
                self.data = str(self.fecha_actualizacion.get())
                self.ciclefp = 'Batx'
                self.sql_query = f"INSERT INTO ALUMNES (codi, nom, cognom1, cognom2, materia, tutor, consideracions, estat, username, cicle_fp, data_registre) values ('{self.codi}', '{self.nom}', '{self.cognom1}', '{self.cognom2}', '{self.materia}', '{self.tutor}', '{self.consideraciones}', '{self.estat}', '{self.username}', '{self.ciclefp}', '{self.data}');"

                if self.data != "":
                    connection.cursor.execute(self.sql_query)
                    connection.bbdd_nese.commit()  # Guardar modificaciones

        except:
            messagebox.showinfo(title="Error",message="Register error")

        baixes = f"UPDATE ALUMNES set estat = 'Baixa' where data_registre NOT LIKE '{self.data}' AND cicle_fp LIKE 'Batx' AND username NOT IN (SELECT username FROM (SELECT * FROM ALUMNES) as A2 WHERE data_registre = '{self.data}');"
        connection.cursor.execute(baixes)  # Actualitza altes/baixes
        self.fecha_actualizacion.delete(0, END)
        messagebox.showinfo(title="Data updated", message="New registers added.")

    def Actualizar_BBDD_FP(self):

        try:

            self.dataframe = pd.read_csv(self.archivo)
            self.dataframe.replace('\'', ' ', regex=True, inplace=True)
            # Esto para introducir nuevos datos totalmente de 0:
            for row in self.dataframe.itertuples():

                row_moduls = row.moduls_matriculats.split(',')
                for modul in row_moduls:
                    self.codi = random.randint(1, 999999999)
                    self.nom = row.nom
                    self.cognom1 = row.cognom1
                    self.cognom2 = row.cognom2
                    self.materia = modul
                    self.tutor = row.tutor
                    self.consideraciones = row.observacions_ioc
                    self.estat = 'Alta'
                    self.username = row.username
                    self.cicle_fp = row.sigles_cicle_LOE
                    self.data = str(self.fecha_actualizacion.get())
                    self.sql_query = f"INSERT INTO ALUMNES (codi, nom, cognom1, cognom2, materia, tutor, consideracions, estat, username, cicle_fp,  data_registre) values ('{self.codi}', '{self.nom}', '{self.cognom1}', '{self.cognom2}', '{self.materia}', '{self.tutor}', '{self.consideraciones}', '{self.estat}', '{self.username}', '{self.cicle_fp}', '{self.data}');"

                    if self.data != "":

                        connection.cursor.execute(self.sql_query)
                        connection.bbdd_nese.commit()  # Guardar modificaciones

        except:
            messagebox.showinfo(title="Error", message="Per seguretat, carregui l'arxiu csv de nou i torni a actualitzar dades.\n Revisa que hi hagi data.")

        baixes = f"UPDATE ALUMNES set estat = 'Baixa' where data_registre NOT LIKE '{self.data}' AND (cicle_fp NOT LIKE 'Batx' OR cicle_fp NOT LIKE 'GES') AND username NOT IN (SELECT username FROM (SELECT * FROM ALUMNES) as A2 WHERE data_registre = '{self.data}');"
        connection.cursor.execute(baixes) # Actualitza altes/baixes
        self.fecha_actualizacion.delete(0, END) # Vacía la fecha de actualización tras cargar datos
        messagebox.showinfo(title="Data updated", message="New registers added")

    def Actualizar_BBDD_GES(self):

        try:
            self.dataframe = pd.read_csv(self.archivo)
            self.dataframe.replace('\'',' ', regex=True, inplace=True)
            # Esto para introducir nuevos datos totalmente de 0:
            for row in self.dataframe.itertuples():
                self.codi = random.randint(1, 999999999)
                self.nom = row.nom
                self.cognom1 = row.cognom1
                self.cognom2 = row.cognom2
                self.materia = row.materia
                self.tutor = row.tutor
                self.consideraciones = row.observacions_ioc
                self.estat = 'Alta'
                self.username = row.username
                self.data = str(self.fecha_actualizacion.get())
                self.ciclefp = 'GES'
                self.sql_query = f"INSERT INTO ALUMNES (codi, nom, cognom1, cognom2, materia, tutor, consideracions, estat, username, cicle_fp, data_registre) values ('{self.codi}', '{self.nom}', '{self.cognom1}', '{self.cognom2}', '{self.materia}', '{self.tutor}', '{self.consideraciones}', '{self.estat}', '{self.username}', '{self.ciclefp}', '{self.data}');"

                if self.data != "":
                    connection.cursor.execute(self.sql_query)
                    connection.bbdd_nese.commit()  # Guardar modificaciones

        except:
            messagebox.showinfo(title="Error",message="Load your data file again.")

        baixes = f"UPDATE ALUMNES set estat = 'Baixa' where data_registre NOT LIKE '{self.data}' AND cicle_fp LIKE 'GES' AND username NOT IN (SELECT username FROM (SELECT * FROM ALUMNES) as A2 WHERE data_registre = '{self.data}');"
        connection.cursor.execute(baixes)  # Actualitza altes/baixes
        self.fecha_actualizacion.delete(0, END)
        messagebox.showinfo(title="Data updated", message="New registers added.")

    def Close_BBDD(self):
    
        connection.bbdd_nese.close()
        window.destroy()