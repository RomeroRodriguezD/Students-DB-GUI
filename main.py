import tkinter as tk
from tkinter import ttk, filedialog, font
from Alumne import Alumne
from SQL_Interaction import SQL_Interaction
import pandas as pd

# Sets up the GUI

class NESE_BBDD_GUI(tk.Tk):

    consideraciones = ["[NESE_A10]", "[NESE_B10]", "[NESE_B20]",
                       "[NESE_B30]", "[NESE_B40]", "[NESE_C10]",
                       "[NESE_D10]", "[NESE_D20]", "[NESE_D30]",
                       "[NESE_E10]", "[NESE_F10]", "[NESE_G10]",
                       "[NESE_H10]", "[NESE_I10]", "[NESE_J10]",
                       "[NESE_K10]", "[NESE_K20]",
                       "[NESE_M10]", "[NESE_Z10]", "[NESE_MG]", "[NESE_VG]"]

    materies = ["Llengua Catalana i Literatura", "Llengua Castellana i Literatura", "LLengua Estrangera",
                "Educacio Física", "Filosofía"]

    estados_matricula = ["Alta", "Baixa", "Aspirant"]

    def __init__(self, *args, **kwargs):
        self.window = tk.Tk()
        self.window.title("Alumnat NESE")
        self.window.pack_propagate(False)  # tells the root to not let the widgets inside it determine its size.
        self.window.resizable(0, 0)  # makes the root window fixed in size.
        self.window.geometry("800x450")
        self.font = font.Font(name='TkCaptionFont', exists=True)
        self.font.config(family='Arial', size=12) #Configura el tamany de lletra dels missatges d'error/informatius
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
        self.ventana_consultas = self.notebook.add(self.consulta_frame, text="Consultes")
        self.frame_agregar = ttk.Frame(self.notebook)
        self.ventana_agregar = self.notebook.add(self.frame_agregar, text="Afegir aspirant/alumne")
        self.adaptaciones_frame = ttk.Frame(self.notebook)
        self.ventana_adaptaciones = self.notebook.add(self.adaptaciones_frame, text="Afegir adaptacions")
        self.documentos_frame = ttk.Frame(self.notebook)
        self.documentos_ventana = self.notebook.add(self.documentos_frame, text="Afegir documentació")
        self.upload_frame = ttk.Frame(self.notebook)
        self.ventana_upload = self.notebook.add(self.upload_frame, text="Actualitzar base de dades")
        self.consideraciones_frame = ttk.Frame(self.notebook)
        self.ventana_consideraciones = self.notebook.add(self.consideraciones_frame, text="Llista Con.")


    def set_treeview(self):
        # Frame para el TreeView
        self.frame1 = tk.LabelFrame(self.consulta_frame, text="Dades SQL")
        self.frame1.place(height=200, width=800)

        ## Treeview
        self.tv1 = ttk.Treeview(self.frame1)
        self.tv1.place(relheight=1, relwidth=1)  # Ajusta el tamaño del widget al 100% del contenedor (frame1).
        self.treescrolly = tk.Scrollbar(self.frame1, orient="vertical", command=self.tv1.yview)  # command means update the yaxis view of the widget
        self.treescrollx = tk.Scrollbar(self.frame1, orient="horizontal",command=self.tv1.xview)  # command means update the xaxis view of the widget
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

        self.busqueda_frame = tk.LabelFrame(self.consulta_frame, text="Criteris de selecció")
        self.busqueda_frame.place(height=120, width=780, rely=0.47, relx=0.014)  # Dejar así fijado el ancho y las rel x e y.

        # Nom
        self.nom_label = tk.Label(self.busqueda_frame, text="Nom")
        self.nom_label.place(relx=0.01, rely=0)
        self.nom_entry = tk.Entry(self.busqueda_frame)
        self.nom_entry.place(relx=0.01, rely=0.25, width=100)

        # Cognom1
        self.cognom1_label = tk.Label(self.busqueda_frame, text="1r cognom")
        self.cognom1_label.place(relx=0.15, rely=0)
        self.cognom1_entry = tk.Entry(self.busqueda_frame)
        self.cognom1_entry.place(relx=0.15, rely=0.25, width=100)

        # Cognom2
        self.cognom2_label = tk.Label(self.busqueda_frame, text="2n cognom")
        self.cognom2_label.place(relx=0.29, rely=0)
        self.cognom2_entry = tk.Entry(self.busqueda_frame)
        self.cognom2_entry.place(relx=0.29, rely=0.25, width=100)

        #  Materia
        self.materia_label = tk.Label(self.busqueda_frame, text="Materia")
        self.materia_label.place(relx=0.43, rely=0)
        self.materia_combobox = ttk.Combobox(self.busqueda_frame)
        self.materia_combobox.place(relx=0.43, rely=0.25, width=100)
        self.materia_combobox['values'] = NESE_BBDD_GUI.materies

        # Tutor
        self.tutor_label = tk.Label(self.busqueda_frame, text="Tutor")
        self.tutor_label.place(relx=0.57, rely=0)
        self.tutor_entry = ttk.Combobox(self.busqueda_frame)
        self.tutor_entry.place(relx=0.57, rely=0.25, width=100)
        self.tutor_entry['values']= lista_tutores

        # consideraciones
        self.consideraciones_label1 = tk.Label(self.busqueda_frame, text="Consideración")
        self.consideraciones_label1.place(relx=0.71, rely=0)
        self.consideraciones_busqueda = ttk.Combobox(self.busqueda_frame)
        self.consideraciones_busqueda.place(relx=0.71, rely=0.25, width=100)
        self.consideraciones_busqueda['values'] = self.consideraciones

        # Estat
        self.estat_label1 = tk.Label(self.busqueda_frame, text="Estat matrícula")
        self.estat_label1.place(relx=0.85, rely=0)
        self.estat_combobox = ttk.Combobox(self.busqueda_frame)
        self.estat_combobox.place(relx=0.85, rely=0.25, width=100)
        self.estat_combobox['values'] = NESE_BBDD_GUI.estados_matricula

        # username
        self.username_label1 = tk.Label(self.busqueda_frame, text="Username")
        self.username_label1.place(relx=0.01, rely=0.5)
        self.username_entry1 = tk.Entry(self.busqueda_frame)
        self.username_entry1.place(relx=0.01, rely=0.7, width=100)

        # fecha alta

        self.fecha_label1 = tk.Label(self.busqueda_frame, text="Data de registre")
        self.fecha_label1.place(relx=0.15, rely=0.5)
        self.fecha_entry1 = tk.Entry(self.busqueda_frame)
        self.fecha_entry1.place(relx=0.15, rely=0.7, width=100)

        # cicle, en cas d'FP
        self.ciclefp_label1 = tk.Label(self.busqueda_frame, text="Estudis")
        self.ciclefp_label1.place(relx=0.29, rely=0.5)
        self.ciclefp_entry1 = tk.Entry(self.busqueda_frame)
        self.ciclefp_entry1.place(relx=0.29, rely=0.7, width=100)

        ######## Botón de Búsqueda (Función SELECT SQL) ######
        self.busqueda_button = tk.Button(self.busqueda_frame, text="Cercar", command=self.search_student) # setconfig externos?
        self.busqueda_button.place(relx=0.85, rely=0.55, width=100)

        ####### Botón para exportar el resultado #######
        self.exportar_button = tk.Button(self.consulta_frame, text="Exportar en format CSV", command=self.Exportar)  # Nota: Exportar con un índice autogenerado.
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
        self.agregar_frame = tk.LabelFrame(self.frame_agregar, text="Criteris d'introducció")
        self.agregar_frame.place(height=400, width=780, rely=0.05, relx=0.014)  # Dejar así fijado el ancho y las rel x e y.

        # Nom
        self.nom_label2 = tk.Label(self.agregar_frame, text="Nom")
        self.nom_label2.place(relx=0.01, rely=0)
        self.nom_entry2 = tk.Entry(self.agregar_frame)
        self.nom_entry2.place(relx=0.01, rely=0.05, width=100)

        # Cognom1
        self.cognom1_label2 = tk.Label(self.agregar_frame, text="1r cognom")
        self.cognom1_label2.place(relx=0.15, rely=0)
        self.cognom1_entry2 = tk.Entry(self.agregar_frame)
        self.cognom1_entry2.place(relx=0.15, rely=0.05, width=100)

        # Cognom2
        self.cognom2_label2 = tk.Label(self.agregar_frame, text="2n cognom")
        self.cognom2_label2.place(relx=0.29, rely=0)
        self.cognom2_entry2 = tk.Entry(self.agregar_frame)
        self.cognom2_entry2.place(relx=0.29, rely=0.05, width=100)

        # Materia
        self.materia_label2 = tk.Label(self.agregar_frame, text="Materia")
        self.materia_label2.place(relx=0.43, rely=0)
        self.materia_combobox2 = ttk.Combobox(self.agregar_frame)
        self.materia_combobox2.place(relx=0.43, rely=0.05, width=100)
        self.materia_combobox2['values'] = NESE_BBDD_GUI.materies

        # Tutor
        self.tutor_label2 = tk.Label(self.agregar_frame, text="Tutor")
        self.tutor_label2.place(relx=0.57, rely=0)
        self.tutor_entry2 = ttk.Combobox(self.agregar_frame)
        self.tutor_entry2.place(relx=0.57, rely=0.05, width=100)
        self.tutor_entry2['values']=lista_tutores

        # Adaptacions
        self.adaptacion_label = tk.Label(self.agregar_frame, text="Adaptacions")
        self.adaptacion_label.place(relx=0.01, rely=0.3)
        self.adaptacion_entry = tk.Text(self.agregar_frame)
        self.adaptacion_entry.place(height=200, width=300, relx=0.01, rely=0.35)

        # Label Consideracions y lista
        self.consideracions_label = tk.Label(self.agregar_frame, text="Consideracions")
        self.consideracions_label.place(relx=0.5, rely=0.3)
        self.consideracion_lista = ttk.Combobox(self.agregar_frame)
        self.consideracion_lista.place(height=20, width=300, relx=0.5, rely=0.35)
        self.consideracion_lista['values'] = NESE_BBDD_GUI.consideraciones

        # Estat
        self.estat_label2 = tk.Label(self.agregar_frame, text="Estat matrícula")
        self.estat_label2.place(relx=0.01, rely=0.15)
        self.estat_combobox2 = ttk.Combobox(self.agregar_frame)
        self.estat_combobox2.place(relx=0.01, rely=0.2, width=100)
        self.estat_combobox2['values'] = self.estados_matricula

        # Documents
        self.documents_label = tk.Label(self.agregar_frame, text="Documents aportats")
        self.documents_label.place(relx=0.5, rely=0.40)
        self.documents_text = tk.Text(self.agregar_frame)
        self.documents_text.place(relx=0.5, rely=0.45, height=161, width=200)

        # ¿username? ->
        self.username_label3 = tk.Label(self.agregar_frame, text="Username")
        self.username_label3.place(relx=0.15, rely=0.15)
        self.username_entry3 = tk.Entry(self.agregar_frame)
        self.username_entry3.place(relx=0.15, rely=0.2, width=100)

        # Fecha
        self.fecha_label2 = tk.Label(self.agregar_frame, text="Data de registre")
        self.fecha_label2.place(relx=0.29, rely=0.15)
        self.fecha_entry2 = tk.Entry(self.agregar_frame)
        self.fecha_entry2.place(relx=0.29, rely=0.2, width=100)

        # Cicle FP

        self.ciclefp_label2 = tk.Label(self.agregar_frame, text="Estudis")
        self.ciclefp_label2.place(relx=0.43, rely=0.15)
        self.ciclefp_entry2 = tk.Entry(self.agregar_frame)
        self.ciclefp_entry2.place(relx=0.43, rely=0.2, width=100)

        # Botón de añadir alumno
        self.afegir_button = tk.Button(self.agregar_frame, text="Afegir", command=self.Agregar)#, command=self.Agregar_Alumno)
        self.afegir_button.place(relx=0.8, rely=0.04)

    def set_adaptaciones(self):

        self.adaptacions_labelframe = tk.LabelFrame(self.adaptaciones_frame, text="Introdueix el username a modificar i afegeix les adaptacions")
        self.adaptacions_labelframe.place(height=400, width=780, rely=0.05, relx=0.014)  # Dejar así fijado el ancho y las rel x e y.
        self.adaptacion_modificaciones = tk.Text(self.adaptaciones_frame)
        self.adaptacion_modificaciones.place(relx=0.02, rely=0.10, height=350, width=400)

        # username
        self.username_label2 = tk.Label(self.adaptaciones_frame, text="Username")
        self.username_label2.place(relx=0.6, rely=0.10)
        self.username_entry2 = tk.Entry(self.adaptaciones_frame)
        self.username_entry2.place(relx=0.6, rely=0.15, width=100)

        # Botón de modificación
        self.agregar_adaptacion = tk.Button(self.adaptaciones_frame, text="Afegir adaptació", command=self.Adaptacion)#, command=self.Agregar_Adaptacion)
        self.agregar_adaptacion.place(relx=0.6, rely=0.22, width=150)

    def set_documentos(self):

        self.documentos_labelframe = tk.LabelFrame(self.documentos_frame, text="Introdueix el username a modificar i afegeix la documentació")
        self.documentos_labelframe.place(height=400, width=780, rely=0.05, relx=0.014)  # Dejar así fijado el ancho y las rel x e y.
        self.documentacion_modificaciones = tk.Text(self.documentos_frame)
        self.documentacion_modificaciones.place(relx=0.02, rely=0.10, height=350, width=400)

        # username
        self.username_label4 = tk.Label(self.documentos_frame, text="Username")
        self.username_label4.place(relx=0.6, rely=0.10)
        self.username_entry4 = tk.Entry(self.documentos_frame)
        self.username_entry4.place(relx=0.6, rely=0.15, width=100)

        # Botón de modificación
        self.agregar_documentos = tk.Button(self.documentos_frame, text="Afegir documentació", command=self.Documentacion)#, command=self.Agregar_Documentos)
        self.agregar_documentos.place(relx=0.6, rely=0.22, width=150)

    def set_upload(self):

        self.upload_labelframe = tk.LabelFrame(self.upload_frame)
        self.upload_labelframe.place(height=400, width=780, rely=0.05,relx=0.014)  # Dejar así fijado el ancho y las rel x e y.
        self.actualizar_button = tk.Button(self.upload_labelframe, text="Actualitzar base de dades Batx", command=self.Actualizar_BATX)#, command=self.Actualizar_BBDD_Batx)
        self.actualizar_button.place(relx=0.05, rely=0.25)
        self.actualizarFP_button = tk.Button(self.upload_labelframe, text="Actualitzar base de dades FP", command=self.Actualizar_FP)#, command=self.Actualizar_BBDD_FP)
        self.actualizarFP_button.place(relx=0.05, rely=0.35)
        self.actualizarFP_button = tk.Button(self.upload_labelframe, text="Actualitzar base de dades GES", command=self.Actualizar_GES)#, command=self.Actualizar_BBDD_GES)
        self.actualizarFP_button.place(relx=0.05, rely=0.45)
        self.fecha_actualizacion_label = tk.Label(self.upload_labelframe, text="Data de registre DD/MM/AAAA")
        self.fecha_actualizacion_label.place(relx=0.05, rely=0.1)
        self.fecha_actualizacion = tk.Entry(self.upload_labelframe)
        self.fecha_actualizacion.place(relx=0.05, rely=0.15, width=100)

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

        self.consideraciones_labelframe = tk.LabelFrame(self.consideraciones_frame, text="Llistat de consideracions")
        self.consideraciones_labelframe.place(height=400, width=780, rely=0.05,relx=0.014)  # Dejar así fijado el ancho y las rel x e y.
        self.consideraciones_lista = tk.Listbox(self.consideraciones_labelframe)
        self.consideraciones_lista.place(relx=0.02, rely=0.05, width=580, height=300)
        for i in consideraciones_fullname:
            self.consideraciones_lista.insert(tk.END,i)

    def search_student(self):

        self.new_interaction = db
        self.new_student = Alumne()
        self.new_student.nom = str(self.nom_entry.get())
        self.new_student.cognom1 = str(self.cognom1_entry.get())
        self.new_student.cognom2 = str(self.cognom2_entry.get())
        self.new_student.materia = str(self.materia_combobox.get())
        self.new_student.tutor = str(self.tutor_entry.get())
        self.new_student.consideraciones = str(self.consideraciones_busqueda.get())
        self.new_student.estat = str(self.estat_combobox.get())
        self.new_student.username = str(self.username_entry1.get())
        self.new_student.cicle_fp = str(self.ciclefp_entry1.get())
        self.new_student.data = str(self.fecha_entry1.get())

        #query = [{"nom":self.nom_input}, {"cognom1":self.cognom1_input},{"cognom2":self.cognom2_input}, {"materia":self.materia_input},
                 #{"tutor":self.tutor_input}, {"consideraciones":self.consideracion_input}, {"estat":self.estat}, {"username":self.username},
                 #{"cicle_fp":self.ciclefp}, {"data":self.data}
                 #]
        self.query_table = self.new_interaction.SQL_Query(self.new_student) # Devuelve una tabla de SQL accediendo con esta clase.
        self.Load_SQL_data(self.query_table) # Carga los datos en el treeview

    def Load_SQL_data(self, query_table):

        """Carga la base de datos en el Treeview"""

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

    def Exportar(self):

        self.new_interaction = db # Accede a SQL
        self.new_interaction.Exportar_Excel()  # Exporta y cierra

    def Cargar_CSV(self):

        try:
            self.archivo = filedialog.askopenfile(mode="r", filetypes=[("Full de valors separats per comes", "*.csv"), ("Tots els arxius", "*.*")])
            self.dataframe = pd.read_csv(self.archivo)
            self.dataframe.replace('\'',' ', regex=True, inplace=True)

            return self.dataframe

        except AttributeError:
            pass

    def Agregar(self):

        self.new_student = Alumne()
        self.new_student.nom = str(self.nom_entry2.get())
        self.new_student.cognom1 = str(self.cognom1_entry2.get())
        self.new_student.cognom2 = str(self.cognom2_entry2.get())
        self.new_student.materia = str(self.materia_combobox2.get())
        self.new_student.tutor = str(self.tutor_entry2.get())
        self.new_student.adaptaciones = str(self.adaptacion_entry.get(1.0, tk.END))
        self.new_student.consideraciones = str(self.consideracion_lista.get())
        self.new_student.estat = str(self.estat_combobox2.get())
        self.new_student.username = str(self.username_entry3.get())
        self.new_student.documentos = str(self.documents_text.get(1.0, tk.END))
        self.new_student.cicle_fp = str(self.ciclefp_entry2.get())  # TODO
        self.new_student.data = str(self.fecha_entry2.get())
        self.new_addition = db #Accede a la base de datos
        self.add_new_student = self.new_addition.Agregar_Alumno(self.new_student)

    def Adaptacion(self):

        self.new_student = Alumne()
        self.new_student.username = str(self.username_entry2.get())
        self.new_student.adaptaciones = str(self.adaptacion_modificaciones.get(1.0, tk.END))
        self.new_addition = db
        self.add_new_adaptaciones = self.new_addition.Agregar_Adaptacion(self.new_student)

    def Documentacion(self):

        self.new_student = Alumne()
        self.new_student.username = str(self.username_entry4.get())
        self.new_student.documentos = str(self.documentacion_modificaciones.get(1.0, tk.END))
        self.new_addition = db
        self.add_new_documentacion = self.new_addition.Agregar_Documentos(self.new_student)

    def Actualizar_BATX(self):

        self.archivo = self.Cargar_CSV()
        self.data = self.fecha_actualizacion.get()
        self.new_interaction = db
        self.new_update = self.new_interaction.Actualizar_BBDD_Batx(dataframe=self.archivo, data=self.data)

    def Actualizar_FP(self):

        self.archivo = self.Cargar_CSV()
        self.data = self.fecha_actualizacion.get()
        self.new_interaction = db
        self.new_update = self.new_interaction.Actualizar_BBDD_FP(dataframe=self.archivo, data=self.data)

    def Actualizar_GES(self):

        self.archivo = self.Cargar_CSV()
        self.data = self.fecha_actualizacion.get()
        self.new_interaction = db
        self.new_update = self.new_interaction.Actualizar_BBDD_GES(dataframe=self.archivo, data=self.data)


# Instancia un objeco que interactúe con SQL

global db
db = SQL_Interaction()

NESE_BBDD_GUI()