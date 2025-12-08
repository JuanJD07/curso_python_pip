from menu import mostrar_menu
from pedir_cafe import pedir_cafe
from historial_cafe import historial_cafe
from salir import salir
def main():
    while True:
        mostrar_menu()
        opcion = input('Selecciona una opción: ')

        if opcion =='1':
            pedir_cafe()

        elif opcion =='2':
            historial_cafe()

        elif opcion == '3':
            print('\nMuchas gracias por haber tomado nuestros servicios')
            salir()
            break

        else:
            print('Opción invalida, por favor seleccione una de las opciones sugeridas')

if __name__ == '__main__':
    main()