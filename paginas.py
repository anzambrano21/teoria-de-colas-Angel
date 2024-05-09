import flet
from flet import Page, Column,Row
from nodos import Nodo
import random
class pruevas:
    def __init__(self,env,page:Page):
        self.env=env
        self.page=page
        self.col=Column(width=500,height=200,scroll=flet.ScrollMode.ALWAYS)
        self.contenido()
        

        self.num_Nodo=[]
    def contenido(self):
         self.n_TexNodo=flet.TextField(label="Numero de nodos",on_change=self.soloNumero)
         self.row=Column(controls=[
            self.n_TexNodo,
            Row(controls=[flet.ElevatedButton(text="generar",on_click=self.generar),
                         flet.ElevatedButton(text="random",on_click=self.random)])
            
            

         ])
        
         
         self.page.add(self.row)

    def soloNumero(self,e):
        try:
            n=int(self.n_TexNodo.value)
        except:
            self.n_TexNodo.value=""
        self.page.update()
        
    def generar(self,event):
        if (len(self.page.controls)>2):
            self.page.controls.pop(1)
            self.page.controls.pop(2)
            self.num_Nodo.clear()
        try:
            n=int(self.n_TexNodo.value)
        except:
            
            self.n_TexNodo.value="0"
        if (int(self.n_TexNodo.value)>0):
            for i in range(int(self.n_TexNodo.value)): self.num_Nodo.append(flet.TextField(label=f"tiempo de llegada del nodo {i+1}"))
            self.col.controls=self.num_Nodo
            self.page.add(self.col)
            self.page.add(flet.ElevatedButton(text="operar",on_click=self.operarC))
            self.page.update()
    def random(self,event):
        for i in range(len(self.num_Nodo)): self.num_Nodo[i].value= random.randint(1,40)
        self.page.update()

    def operarC(self,event):
        

        nodos=[]
        Probalilida=[]
        ban=True
        CerosNodos = any(float(nodo.value) <= 0  for nodo in self.num_Nodo)
        for i in range(len(self.num_Nodo)):
            try:
                n=float(self.num_Nodo[i].value)
            except:
                ban=False
        if(not CerosNodos and ban):
            
            for i in range(len(self.num_Nodo)): nodos.append(Nodo(self.env,float(self.num_Nodo[i].value),(15,30),nombre=f"{i}"))
            for nodo in nodos: self.env.process(nodo.llegada_cliente())

            self.env.run(until=100)

            for i in range(len(nodos)): Probalilida.append(1-(nodos[i].Tlleg/nodos[i].Toper[1]))
            res=Column(width=500,height=75,scroll=flet.ScrollMode.ALWAYS)
            resp=[]     
            print(Probalilida)
            for i in range(len(Probalilida)):resp.append(flet.Text(value="probabilidad de atender es {0}".format(Probalilida[i])))
            res.controls=resp
            self.page.add(res)
            self.page.update()
         
         