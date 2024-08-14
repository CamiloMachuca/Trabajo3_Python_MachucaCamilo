import json
from datetime import date

listaPedidos=[]
with open("./Pedidos.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaPedidos=json.load(files)

listaMenu=[]
with open("./Menu.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaMenu=json.load(files)

def guardarPedido(miDato):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("Pedidos.json","w") as outfile:
        json.dump(miDato,outfile)
def guardarpedidos(cliente,estado,items):

    pedido= {
        "cliente": cliente,
        "items": items,
        "estado": estado
    }

    listaPedidos.append(pedido)
    guardarPedido(listaPedidos)

buliano=True
while buliano==True:

    print("##########################")
    print("#### Menu principal ####")# se realizo el menu principal con sus respectivas opciones
    print("##########################")
    print("(1) Realizar un pedido")
    print("(2) Realizar consulta")
    print("(3) Salir del programa")
    opcion=int(input("Ingrese la opcion deseada: "))
    if opcion==1:
        bucle=True
        while bucle==True:

            print()
            print("####### Menu de opciones ######")# menu para la realización de pedidos
            print("(1) Realizar un pedido")
            print("(2) Revisar el menu ")
            print("(3) salir del programa")
            print()
            opci=int(input("ingrese la opcion deseada: "))
            if opci==1:
                print("Ingrse los siguientes datos para realizar el pedido: ")
                cliente=input("Ingrese el nombre del cliente: ")
                buclee=True
                while buclee==True:# se crea un bucle while para guardar los items que el usuario requiera

                    nombre=input("Ingrese el nombre: ")
                    items=[]
                    for i in listaMenu:
                        if nombre==i["nombre"]:
                            categoria=i["categoria"]
                            precio=i["precio"]
                            items.append({ "categoria":categoria,"nombre": nombre,"precio": precio})
                            break

                    estado=input("Ingrese el estado: ")
                    respuesta=int(input("Deseas agregar otro producto escribe 1=si o 2=no: "))
                    if respuesta==1:
                        buclee=True
                    elif respuesta==2:
                        buclee=False
                guardarpedidos(cliente,estado,items)
            elif opci==2:
                print("Este es el menu de productos disponible: ")# se muestran los productos que hay en el menu
                for i in listaMenu:
                    print("categoria: ", i["categoria"])
                    print("nombre: ", i["nombre"])
                    print("precio: ", i["precio"])
                    print()
            
            elif opci==3:
                bucle=False

    elif opcion==2:
        bulianito=True
        while bulianito==True:

            print("##########################")
            print("#### Menu de consulta ####")
            print("##########################")
            print("(1) Mostrar todos los pedidos")
            print("(2) mostrar un pedido particular")
            print("(3) salir al menu principal")
            opcio=int(input("Ingresa la opcion deseada: "))
            if opcio==1:
                print("Los pedidos realizados son: ")# se muestran todos los pedidos que hay hasta la fecha 
                for i in listaPedidos:
                    print()
                    print("cliente:", i["cliente"])
                    print("estado:", i ["estado"])
                    print("items")
                    for i in i["items"]:
                        
                        print(f"nombre: {i["nombre"]}")
                        print(f"categoria: {i["categoria"]}")
                        print(f"precio: {i["precio"]}")
                        print()
                        break

            elif opcio==2:
                cliente=input("Ingrese el nombre del cliente al cual deseas revisar el pedido: ")# se muestra el pedido de un cliente en especifico 
                for i in listaPedidos:
                    if cliente==i["cliente"]:
                        print("cliente:", i["cliente"])
                        print("estado:", i ["estado"])
                        print("items")
                        for i in i["items"]:
                            print(f"nombre: {i["nombre"]}")
                            print(f"categoria: {i["categoria"]}")
                            print(f"precio: {i["precio"]}")
                            print()
                            break
                            
                    

            else:
                bulianito=False


    else:
        buliano=False

# Programa desarrollado por camilo machuca vega Grupo: T2