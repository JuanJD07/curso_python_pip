import matplotlib.pyplot as plt  # Importamos la librería matplotlib para crear gráficos


def generate_pie_chart():
    labels = ["A", "B", "C"]  # Etiquetas que se mostrarán en cada porción del gráfico
    values = [
        400,
        200,
        35,
    ]  # Valores numéricos que determinan el tamaño de cada porción

    fig, ax = (
        plt.subplot()
    )  # Creamos una figura y un eje donde se dibujará el gráfico circular
    ax.pie(
        values, labels=labels
    )  # Generamos el gráfico de pastel usando los valores y etiquetas

    plt.savefig(
        "pie.png"
    )  # Guardamos el gráfico generado en un archivo llamado 'pie.png'
    plt.close()  # Cerramos la figura para liberar memoria y evitar conflictos con futuros gráficos0
