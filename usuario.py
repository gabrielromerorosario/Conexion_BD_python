import sqlite3

class Conexion_DB ():

     
    def Crear_DB(nombre_DB):

        cone = sqlite3.connect(nombre_DB)
        cone.close()
        

    def Crear_Table_USER(nombre_DB,nombre_TB,valor_nom):
        nombre_TB
        conect = sqlite3.connect(nombre_DB)
        puntero =conect.cursor()
        puntero.execute("CREATE TABLE "+nombre_TB+"(ID INTEGER PRIMARY KEY AUTOINCREMENT ,"+valor_nom+" VARCHAR(40),Direcion VARCHAR(100))")
        puntero.close()
        conect.close()
        

    def Crear_Table_Direciones(nombre_DB,nombre_TB,):
        nombre_TB
        conect = sqlite3.connect(nombre_DB)
        puntero =conect.cursor()
        puntero.execute("CREATE TABLE "+nombre_TB+"(ID INTEGER PRIMARY KEY AUTOINCREMENT,Id_Direciones INTEGER ,Direciones VARCHAR(150), CONSTRAINT fk_Usuario FOREIGN KEY(Id_Direciones) REFERENCES Usuario(ID))")
        puntero.close()
        conect.close()

    def Insertar_INTO_USER(nombre_DB,tabla,valor1,valor2):
        tabla, valor1, valor2
        datos=[valor1,valor2]
        conect = sqlite3.connect(nombre_DB)
        puntero =conect.cursor()
        print(f"El usuario {valor1} fue creado y vive em {valor2}")
        puntero.execute(f"INSERT INTO {tabla}(Nombre,Direcion) VALUES(?,?)",datos)
        conect.commit()
        puntero.close()
        conect.close()

    def Insertar_INTO_Dire(nombre_DB,tabla,valor1,valor2):
        tabla
        datos=[valor1,valor2]
        conect = sqlite3.connect(nombre_DB)
        puntero =conect.cursor()
        puntero.execute(f"INSERT INTO {tabla}(Id_Direciones,Direciones) VALUES(?,?)",datos)
        conect.commit()
        puntero.close()
        conect.close()

    
    def Select(nombre_DB,valor,tabla,tabla2,valor2):
        
        conect = sqlite3.connect(nombre_DB)
        puntero =conect.cursor()
        puntero.execute(f" SELECT {valor} FROM {tabla} AS u LEFT JOIN {tabla2}  AS d where u.ID = {valor2}  ")
        datos = puntero.fetchall()
        puntero.close()
        conect.close()
        return datos
       #resultado =Conexion_DB.Select("Cliente",Traer,"Usuario","Direciones")
        

    def Select_INNER(nombre_DB,Lista,tabla1,tabla2):
        tabla1
        conect = sqlite3.connect(nombre_DB)
        puntero =conect.cursor()
        puntero.execute(f" SELECT {Lista} FROM {tabla1} AS u INNER JOIN {tabla2} AS d ON u.ID = d.Id_Direciones")
        datos = puntero.fetchone()
        conect.close()
        return datos
        

print("************************************************************************")
print("***************************Bienvenido***********************************")
print("Menu de Opciones")
print( " 1) Crear Cliente 2)Agregar nueva direcion 3)Buscar Cliente")


    


repuesta = int(input("Elige la opcion deseada : "))

if repuesta == 1:
    try:
        nombre = input("Ingrese el nombre del Cliente : ").lower()
        Direcion = input("Ingresela direcion del Cliente : ").lower()
        Conexion_DB.Insertar_INTO_USER("Cliente","Usuario",nombre,Direcion)
        print("El Usuario fue Creado")
    except ValueError:
         print("Oops!  No se puedo Crear.  Try again...")
    
    
    
elif repuesta == 2:
    ID_direcion = input("Ingrese el ID Del Usuario a quien agregara nueva Direcion : ").lower()
    Direcion = input("Ingrese la nueva Direcion : ").lower()
    
    try:
        Conexion_DB.Insertar_INTO_Dire("Cliente","Direciones",ID_direcion,Direcion)
        print("Direcion Agregada")
    except ValueError:
         print("Oops!  No se puedo Crear.  Try again...")

elif repuesta == 3:
    ID = int(input("Ingrese el Nombre de usuario que desea consultar : "))
    Traer ="Nombre,Direcion,Direciones"

    try:
        
        resultado =Conexion_DB.Select("Cliente",Traer,"Usuario","Direciones",ID)
        
        print(resultado[:1])


            


    except ValueError:
         print("Oops!  No se puedo Crear.  Try again...")

else:
    print("Ingrese un numero correcto")

print("************************************************************************")
print("***************************Hasta Pronto*********************************")
         
   