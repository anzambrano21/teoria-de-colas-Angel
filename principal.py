import flet,random,simpy
from flet import Page, Column,Row, ElevatedButton ,Text
from nodos import nodo


class pruevas:
    def __init__(self,env,page:Page):
        self.env=env
        self.page=page
        self.col=Column(width=500,height=200,scroll=flet.ScrollMode.ALWAYS)
        self.contenido()
        

        self.num_Nodo=[]
    def contenido(self):
         self.n_TexNodo=flet.TextField(label="Numero de nodos")
         self.row=Column(controls=[
            self.n_TexNodo,
            flet.ElevatedButton(text="generar",on_click=self.generar)

         ])
         
         self.page.add(self.row)
    def generar(self,event):
        if (len(self.page.controls)>1):
            self.page.controls.pop(1)
            self.num_Nodo.clear()

        for i in range(int(self.n_TexNodo.value)):
            
            self.num_Nodo.append(flet.TextField(label=f"tiempo de llegada del nodo {i+1}"))
        self.num_Nodo.append(flet.ElevatedButton(text="operar",on_click=self.operarC))
        self.col.controls=self.num_Nodo
        self.page.add(self.col)
        self.page.update()
    def llegadaC(self,cliente,nodo):
        print(f"{cliente} llega al nodo {nodo.nombre} en t = {self.env.now}")
        yield self.env.timeout(nodo.tiempo_llegada)
        print(f"{cliente} se mueve al nodo B en t = {self.env.now}")
        yield self.env.timeout(nodo.tiempo_servicio)
        print(f"{cliente} es atendido en B en t = {self.env.now}")
    def operarC(self,event):
        TIEMPO_CORTE_MIN = 15
        TIEMPO_CORTE_MAX = 30
        nodos=[]
        
        for i in range(len(self.num_Nodo)):
             nodos.append(nodos(self.env,self.num_Nodo[i].value,random.uniform(TIEMPO_CORTE_MIN,TIEMPO_CORTE_MAX),nombre=f"{i}"))
        for nodo in nodos:
            self.env.process(nodo.llegada_cliente())

        self.env.run(until=100)
        longitud_promedio_cola = sum(nodo.cola.count for nodo in nodos) /len(self.num_Nodo)
        tiempo_espera_promedio = longitud_promedio_cola / 5  # 5 clientes en total

        print(f"Longitud promedio de la cola: {longitud_promedio_cola:.2f}")
        print(f"Tiempo de espera promedio: {tiempo_espera_promedio:.2f} minutos")
         
         
         
def main(page:Page):
    page.window_height=500
    page.window_width=500
    
    page.window_resizable=False
    env = simpy.Environment()
    # Parámetros

    page.title="Teoria de nodos"
    pruevas(env,page)
    page.update()
if __name__=="__main__":

        flet.app(main)