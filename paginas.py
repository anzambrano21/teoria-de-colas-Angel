import flet,simpy
from flet import Page, Column
from nodos import Nodo
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
            self.page.controls.pop(2)
            #self.page.controls.pop(3)
            self.num_Nodo.clear()

        for i in range(int(self.n_TexNodo.value)):
            
            self.num_Nodo.append(flet.TextField(label=f"tiempo de llegada del nodo {i+1}"))
        self.col.controls=self.num_Nodo
        self.page.add(self.col)
        self.page.add(flet.ElevatedButton(text="operar",on_click=self.operarC))
        self.page.update()

    def operarC(self,event):

        nodos=[]
        Probalilida=[]
        
        for i in range(len(self.num_Nodo)):
             nodos.append(Nodo(self.env,int(self.num_Nodo[i].value),(15,30),nombre=f"{i}"))
        
        for nodo in nodos:
            self.env.process(nodo.llegada_cliente())
        

        self.env.run(until=100)

        for i in range(len(nodos)):
             Probalilida.append(nodos[i].Tlleg/nodos[i].Toper[1])
        res=Column(width=500,height=200,scroll=flet.ScrollMode.ALWAYS)
        resp=[]     
        for i in range(len(Probalilida)):
            resp.append(flet.Text(value="probabilidad de espera es {0}".format(Probalilida[i])))
        res.controls=resp
        self.page.add(res)
        self.page.update()
         
         