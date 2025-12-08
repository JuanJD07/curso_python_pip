archivo_pedido = 'pedidos.txt'
def pedir_cafe():
    print('\nElige el café que prefieras:')
    print('1. Capuccino')
    print('2. Espresso')
    print('3. Café frío')
    print('4. Tinto')

    opcion = input('Opción: ')

    cafes = {
        '1' : 'Capuccino',
        '2' : 'Espresso',
        '3' : 'Café frío',
        '4' : 'Tinto'
    }

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print ('Has pedido un', cafe_elegido, '.Preparando café...')

        with open(archivo_pedido, 'a', encoding='utf-8') as archivo:
            archivo.write(cafe_elegido + '\n')

    else: 
        print('Opción no valida, por favor vuelva a intentar')
