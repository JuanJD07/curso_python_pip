archivo_pedido = 'pedidos.txt'

def salir():
    with open(archivo_pedido, 'w') as archivo:
        archivo.write('')