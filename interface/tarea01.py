import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def curva_de_ejemplo():
    """
    Curva de Ejemplo que despliega una curva paramétrica en una ventana nueva

    Integrantes:
    - Omar Olivares Urrutia (@ofou)
    :return: plot curve
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z ** 2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='Curva Paramétrica de Ejemplo')
    ax.legend()

    fig.show()

    # Añadir el plot de matplotlib
    # fig = Figure(figsize=(5, 4), dpi=100)
    # t = np.arange(0, 3, .01)
    # fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
    #
    # canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    # canvas.draw()
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #
    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # canvas.mpl_connect("key_press_event", on_key_press)

    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.


def helice_conica():
    # añadir sus códigos aca
    """
        Curva de Ejemplo que despliega una Helice Cónica

        Integrantes:
        - Mario Labbé (@LsMario1998)
        - Mario González (@tatameister)
        - Cristóbal Cortés (@Cristobal140)
        - Thadly Guerra (@Thadly64)
        - Luis Inostroza (@luisinostrozaf)
        :return: Curva Helice Cónica
        """

    plt.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
    print (np.cos((np.pi*30)/180))

    e = 2.718281
    a = 3
    x = a * (e**(np.sin(45) * (1/np.tan(30)*theta))) * np.cos(theta)
    y = a * (e**(np.sin(45) * (1/np.tan(30)*theta)))* np.sin(theta)
    z = a * (e**(np.sin(45) * (1/np.tan(30)*theta))) * (1/np.tan(45))

    ax.plot(x, y, z, label='helice cónica')
    ax.legend()

    plt.show()
    pass
def helice_circular_1():
    """
    Curva que depliega una una helice circular en una ventana nueva

    Integrantes:
    - Felipe Lopez Vergara (@felipelopez00)
    - Bastian Bustamante Moraga (@BastianBustamante)
    - Rodrigo Torrez Queupan (@imperium31)
    - Juan Hernandez Gatica (@juanpablo1994)
    -Eric Rojas Palma (@valukar)
    :return: circular propeller
    """

    # añadir sus códigos aca
    n = 1000
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # caracteristicas de la helice circular
    t_max = 8 * np.pi
    t = np.linspace(0, t_max, n)
    z = t
    r = 5
    y = r * np.sin(t)
    x = r * np.cos(t)
    ax.plot(x, y, z, 'b', lw=2)

    # linea roja al centro de la helice circular
    ax.plot((0, 0), (0, 0), (-t_max * 0.2, t_max * 1.2), color='r', lw=2)

    plt.show()
    pass
def Corona_Sinusoidal():
    # añadir sus códigos aca
    pass
def curva_de_viviani():
    """
    Funcion que muestra una curva de viviani en una nueva ventana

    Integrantes:
    Levi Urbina
    Natalia Valenzuela
    Ricardo Vergara
    Estefany Alarcon

    return: curva_de_viviani
    """

    a = 1
    t = np.linspace(-4, 4 * np.pi, 100)
    x = a * (1 + np.cos(t))
    y = a * np.sin(t)
    z = 2 * a * np.sin(t / 2)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_title("Curva de viviani")
    ax.plot(x, y, z, label="Curva de Viviani", lw=5)
    plt.show()
    pass
def hipopoda_1():
    # añadir sus códigos aca
    '''
           Integrantes:
           - Boris Gutiérrez Cornejo (@BorisAndresLmb)
           - Juan González Jélvez (@JuanGonzalez33)
           - Pablo Barrera Whiteley (@Pablobw)
           - José Flores Cáceres (@JoseFlores9)
           - Cristobal Rojas Saavedra (@cristotix)

           Función hipopoda_1: Grafica la hipopoda
           Utiliza la forma paramétrica de la función
           x= a+(r-a)*cos(t)
           y=(r-a)*sen(t)
           z=2*((a*(r-a))**1/2))*sen(t)
           Parametros:
           a= distancia del centro de la esfera al eje del cilindro
           r=Radio de la esfera
           return: plot Curve (Hipopede)
           '''

    plt.rcParams['legend.fontsize'] = 12
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 99)
    a = 1
    r = 5
    x = a + (r - a) * np.cos(theta)
    y = (r - a) * np.sin(theta)
    z = 2 * (a * (r - a)) ** (1 / 2) * np.sin(theta / 2)
    ax.plot(x, y, z, label='Hipopede de Eudoxo')

    ax.legend()

    plt.show()
    pass
def conica_de_papus():
    """
        Curva que entrega una conica de papus en la interfaz grafica

        Integrantes:
        - José Fabián Ignacio González Encina (@GoldenFenix)
        - Cristian Eduardo Castillo (@criseduardjjd)
        - Diego Faundez Mendez(@diegofaundezm)
        - Claudio Alcaino Muñoz (@klauser99)
        - Francisco Castillo Moraga(@taifokk)
        :return: conica de papus
        """
    plt.rcParams['legend.fontsize'] = 12

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Prepare arrays x, y, z
    t = np.linspace(-9 * np.pi, 9 * np.pi, 2000)

    a1 = 30

    a = 15
    z = a1 * np.cos(a) * t
    r = z ** 2 + 1
    x = a1 * np.sin(a) * t * np.cos(t)
    y = a1 * np.sin(a) * t * np.sin(t)

    ax.plot(x, y, z, label='espiral conica de papus')
    ax.legend()

    plt.show()

    pass
def Curva_de_Arquitas():
    # añadir sus códigos aca
    """""
        Tipo de curva: Curva de Arquitas

      Esta es la animacion de la curva positiva pertenecientes a las curvas de Arquitas.

        Integrantes:
        Nicolas Fernandez (@mathice)
        Sebastian Mendez  (@SebaMendez)
        Cristobal Moreira (@cmoreirab)
        Gabriel Lara      (@Gabolara453)
        Dennis Queirolo   (@dennis-queirolo)

        """

    from matplotlib import pyplot as plt
    import numpy as np
    import mpl_toolkits.mplot3d.axes3d as p3
    from matplotlib import animation

    fig = plt.figure()
    ax = p3.Axes3D(fig)

    a = 20

    def gen(n):
        for theta in np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 100):
            yield np.array([a * np.cos(theta) ** 2, a * np.cos(theta) * np.sin(theta),
                            a * (((1 - np.cos(theta)) * np.cos(theta)) ** 1 / 2)])

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 1000
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

    # Setting the axes properties
    ax.set_xlim3d([-20.0, 20.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-20.0, 20.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-20.0, 10.0])
    ax.set_zlabel('Z')

    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000 / N, blit=False)

    # ani.save('matplot003.gif', writer='imagemagick')
    plt.show()

    """""
    Esta es la animacion de la curva negativa pertenecientes a las curvas de Arquitas.
    """

    from matplotlib import pyplot as plt
    import numpy as np
    import mpl_toolkits.mplot3d.axes3d as p3
    from matplotlib import animation

    fig = plt.figure()
    ab = p3.Axes3D(fig)

    a = 20

    def gen1(n):
        for theta in np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 100):
            yield np.array([a * np.cos(theta) ** 2, a * np.cos(theta) * np.sin(theta),
                            - a * (((1 - np.cos(theta)) * np.cos(theta)) ** 1 / 2)])

    def update1(num1, data1, line1):
        line1.set_data(data1[:2, :num1])
        line1.set_3d_properties(data1[2, :num1])

    N = 1000
    data1 = np.array(list(gen1(N))).T
    line1, = ab.plot(data1[0, 0:1], data1[1, 0:1], data1[2, 0:1])

    # Setting the axes properties
    ab.set_xlim3d([-20.0, 20.0])
    ab.set_xlabel('X')

    ab.set_ylim3d([-20.0, 20.0])
    ab.set_ylabel('Y')

    ab.set_zlim3d([-20.0, 10.0])
    ab.set_zlabel('Z')

    ani = animation.FuncAnimation(fig, update1, N, fargs=(data1, line1), interval=10000 / N, blit=False, repeat=False)

    # ani.save('matplot003.gif', writer='imagemagick')
    plt.show()

    """""
    Este es el intento de graficacion en 3D de la curva de Arquitas completa.
 """

    from matplotlib import pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import animation

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ab = fig.gca(projection='3d')

    a = 20

    theta = np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 100)
    t = 10
    x1 = a * np.cos(theta) ** 2
    y1 = a * np.cos(theta) * np.sin(theta)
    z1 = - a * ((1 - np.cos(theta)) * (np.cos(theta)) ** 1 / 2)
    z = a * (((1 - np.cos(theta)) * np.cos(theta)) ** 1 / 2)
    x = a * np.cos(theta) ** 2
    y = a * np.cos(theta) * np.sin(theta)
    N = 1000

    def gen(N):
        for theta in np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 100):
            x = a * np.cos(theta) ** 2
            y = a * np.cos(theta) * np.sin(theta)
            z = a * (((1 - np.cos(theta)) * np.cos(theta)) ** 1 / 2)
            yield np.array([x, y, z])

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    def gen1(N):
        for theta in np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 100):
            x1 = a * np.cos(theta) ** 2
            y1 = a * np.cos(theta) * np.sin(theta)
            z1 = -a * (((1 - np.cos(theta)) * np.cos(theta)) ** 1 / 2)
            yield np.array([x1, y1, z1])

    def update1(num1, data1, line1):
        line1.set_data1(data1[:2, :num1])
        line1.set_3d_properties(data1[2, :num1])

    data = np.array(list(gen(N))).T
    data1 = np.array(list(gen1(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])
    line1, = ab.plot(data1[0, 0:1], data1[-1, 0:1], data1[-2, 0:1])

    # Setting the axes properties
    ax.set_xlim3d([-20.0, 20.0])
    ax.set_xlabel('X')

    ab.set_xlim3d([20.0, -20.0])
    ab.set_xlabel('X')

    ax.set_ylim3d([-20.0, 20.0])
    ax.set_ylabel('Y')

    ab.set_ylim3d([20.0, -20.0])
    ab.set_ylabel('Y')

    ax.set_zlim3d([-20.0, 10.0])
    ax.set_zlabel('Z')

    ab.set_zlim3d([20.0, -10.0])
    ab.set_zlabel('Z')

    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000 / N, blit=False)

    ani1 = animation.FuncAnimation(fig, update1, N, fargs=(data1, line1), interval=10000 / N, blit=False)

    # ani.save('matplot003.gif', writer='imagemagick')
    plt.show()

    pass
def horoptera():
    # añadir sus códigos aca
    pass
def Curva_Bicilindrica():
    # añadir sus códigos aca
    pass

if __name__ == '__main__':
    # Creación de Ventanas
    root = tk.Tk()
    root.wm_title("Proyecto de Fisica 2019/01")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)

    # Cada grupo debe utilizar sus propia función
    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Ejemplo", command=curva_de_ejemplo)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hélice Cónica", command=helice_conica)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hélice Circular", command=helice_circular_1)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Corona Sinusoidal", command=Corona_Sinusoidal)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Viviani", command=curva_de_viviani)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hipopoda", command=hipopoda_1)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Arquitas", command=Curva_de_Arquitas)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva Bicilindrica", command=Curva_Bicilindrica)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Conica de Papus", command=conica_de_papus)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Horoptera", command=horoptera)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()
