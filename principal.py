import flet,simpy
from flet import Page
from paginas import pruevas
#definicion de funcion prinicipal        
def main(page:Page):
    #definimos la estructura de la ventana
    page.window_height=1000
    page.window_width=1000
    #caselar el cambio de tamaño
    page.window_resizable=False
    env = simpy.Environment()
    # Parámetros

    page.title="Teoria de nodos"
    pruevas(env,page)
    page.update()
if __name__=="__main__":

        flet.app(main)