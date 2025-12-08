archivo_pedido = 'pedidos.txt'
def historial_cafe():
    try:
        with open(archivo_pedido, 'r', encoding='utf-8') as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(i, '. ', pedido.strip())
            
            else:
                print('Aún no hay ningun pedido')
    
    except FileNotFoundError:
        print('\nTodavia no existe un historial de pedidos')