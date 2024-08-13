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
def guardarpedidos(cliente, categoria,nombre,precio,estado,items):

    pedido= {
        "cliente": cliente,
        "items": [],
        

        "estado": estado
    }
    for categoria,nombre,precio in items:
        pedido["items"].append({
            "categoria": categoria,
            "nombre":nombre,
            "prcio": precio
        })
        listaPedidos.append(pedido)
        guardarPedido("Pedidos.json",listaPedidos)

buliano=True
while buliano==True:

    print("##########################")
    print("#### Menu de opciones ####")
    print("##########################")
    print("(1) Realizar un pedido")
    print("(2) Realizar consulta")
    print("(3) Salir del programa")
    opcion=int(input("Ingrese la opcion deseada: "))
    if opcion==1:
        bucle=True
        while bucle==True:
            print()
            print("(1) Realizar un pedido")
            print("(2) Revisar el menu ")
            print("(3) salir del programa")
            print()
            opci=int(input("ingrese la opcion deseada: "))
            if opci==1:
                buclee=True
                while buclee==True:
                    print("Ingrse los siguientes datos para realizar el pedido: ")
                    cliente=input("Ingrese el nombre del cliente: ")
                    nombre=input("Ingrese el nombre: ")
                    items=[]
                    for i in listaMenu:
                        if nombre==i["nombre"]:
                            categoria=i["categoria"]
                    for i in listaMenu:
                        if nombre==i["nombre"]:
                            precio=i["precio"]
                    estado=input("Ingrese el estado: ")
                    items.append(( categoria, nombre, precio))
                    respuesta=int(input("Deseas agregar otro producto escribe 1=si o 2=no: "))
                    if respuesta==1:
                        buclee=True
                    elif respuesta==2:
                        buclee=False
                    guardarpedidos(cliente, categoria,nombre,precio,estado,items)
            elif opci==2:
                print("Este es el menu de productos disponible: ")
                for i in listaMenu:
                    print

        

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
                print("Los pedidos realizados son: ")
                for i in listaPedidos:
                    print("cliente:", i["cliente"])
                    print("items:", i["items"])
                    print("estado:", i ["estado"])

            elif opcio==2:
                cliente=input("Ingrese el nombre del cliente al cual deseas revisar el pedido: ")
                for i in listaPedidos:
                    if cliente==i["cliente"]:
                        print("cliente:", i["cliente"])
                        print("items:", i["items"])
                        print("estado:", i ["estado"])

            else:
                bulianito=False





else:
    buliano=False