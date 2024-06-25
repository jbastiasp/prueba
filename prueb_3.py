genero=("Ficción", "No Ficción", "Ciencia")
lista_libros=[]
lista_De_las_ventas=[]
opcion=[]

def registro():
    TituloLibro=input("Ingresar nombre del libro ").lower()
    Autor=input("ingresa autor del libro").lower()
    Genero= input("ingresar el tipo de genero").lower()
    Precio= input("ingresar precio del libro").lower()
    
    lista_libros.append({
         "titulo":TituloLibro,
         "Autor":Autor,
         "Genero":Genero,
         "Precio":Precio
    })
    return 

def Listar_todos_los_libros():
        for i in lista_libros:
            print()


def registrar_venta():
     print(lista_libros)
     Titulo=input("Ingresar nombre del libro")
     while not Titulo in lista_libros:
          print("invalido")
          Titulo=input("Ingresar nombre del libro")
          Autor=input("ingresa autor del libro")
          Genero= input("ingresar el tipo de genero")
          Precio= input("ingresar precio del libro")
     for Titulo in lista_libros:
               print("libro disponible")
     cantidad=int(input("ingresa la cantidad de libros que quieras"))
     precio=int(input("ingresa la cantidad de libros que quieras"))
     PFinal=cantidad*precio

     lista_De_las_ventas.append({
          "titulo":Titulo,
          "Autor":Autor,
          "Genero":Genero,
          "Precio":Precio
     })
     print(lista_De_las_ventas)
           
def imprimir_reporte_de_ventas():
     op=input("ingresar genero de libro")
     if op=="":  
           for i in lista_De_las_ventas:
                 print(i)     

while True:
    print("1. registrar libro")
    print("2. listar todos los libros")
    print("3. registrar venta")
    print("4.imprimir reporte de ventas")
    print("5.generar txt")
    print("6.salir del programa")
    

    opcion=int(input("ingresa tu opcion"))

    if opcion ==1:
      print("registrar libro")
      registro()
    elif opcion==2:
      print("2. listar todos los libros")
      Listar_todos_los_libros()
    elif opcion==3:
      print("3. registrar venta") 
      registrar_venta()
    elif opcion==4:
      print("4.imprimir reporte de ventas")
      imprimir_reporte_de_ventas()
    elif opcion==5:
      print("5.generar txt") 
      
    elif opcion==6:
      print("6.salir del programa")