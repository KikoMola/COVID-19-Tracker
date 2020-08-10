from tkinter import *

root = Tk()
root.geometry("400x150")
root.title("Obtener datos de COVID-19")


def muestraDatos():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid
    covid = Covid()

    casos = []
    confirmados = []
    activos = []
    muertos = []
    recuperados = []

    try:
        root.update()
        paises = data.get()
        nombres_paises = paises.strip()
        nombres_paises = nombres_paises.replace(" ", ",")
        nombres_paises = nombres_paises.split(",")

        for x in nombres_paises:
            casos.append(covid.get_status_by_country_name(x))
            root.update()

        for y in casos:
            confirmados.append(y["confirmed"])
            activos.append(y["active"])
            muertos.append(y["deaths"])
            recuperados.append(y["recovered"])

        confirmados_p = mpatches.Patch(color='green', label='Confirmados')
        recuperados_p = mpatches.Patch(color='red', label='Recuperados')
        activos_p = mpatches.Patch(color='blue', label='Activos')
        muertes_p = mpatches.Patch(color='black', label='Muertes')

        plt.legend(handles=[confirmados_p, recuperados_p, activos_p, muertes_p])

        for x in range(len(nombres_paises)):
            plt.bar(nombres_paises[x], confirmados[x], color='green')
            if recuperados[x] > activos[x]:
                plt.bar(nombres_paises[x], recuperados[x], color='red')
                plt.bar(nombres_paises[x], activos[x], color='blue')
            else:
                plt.bar(nombres_paises[x], activos[x], color='blue')
                plt.bar(nombres_paises[x], recuperados[x], color='red')
            plt.bar(nombres_paises[x], muertos[x], color='black')
        plt.title('Casos de COVID-19 actuales')
        plt.xlabel('País')
        plt.ylabel('Casos(en millones)')
        plt.show()

    except Exception as e:
        data.set("Introduce bien los datos")


Label(root, text="Introduce los nombres de los países\nde los que quieras obtener los\ndatos de COVID-19",
      font="Roboto 15 bold").pack()
Label(root, text="Introduce nombres de países:").pack()
data = StringVar()
entry = Entry(root, textvariable=data, width=50).pack()
Button(root, text="Enviar", command=muestraDatos).pack()
root.mainloop()


