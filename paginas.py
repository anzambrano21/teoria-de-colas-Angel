import flet
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
         self.n_TexNodo=flet.TextField(label="Numero de nodos",on_change=self.soloNumero)
         self.row=Column(controls=[
            self.n_TexNodo,
            flet.ElevatedButton(text="generar",on_click=self.generar)

         ])
        
         
         self.page.add(self.row)
    def soloNumero(self,e):
        
        
        try:
            n=int(self.n_TexNodo.value)
        except:
            
            self.n_TexNodo.value=""
        
        self.page.update()
        
    def generar(self,event):
        if (len(self.page.controls)>1):
            self.page.controls.pop(1)
            self.page.controls.pop(2)
            self.num_Nodo.clear()
        try:
            n=int(self.n_TexNodo.value)
        except:
            
            self.n_TexNodo.value="0"
        if (int(self.n_TexNodo.value)>0):
            for i in range(int(self.n_TexNodo.value)): self.num_Nodo.append(flet.TextField(label=f"tiempo de llegada del nodo {i+1}",on_change=self.soloNumero))
            self.col.controls=self.num_Nodo
            self.page.add(self.col)
            self.page.add(flet.ElevatedButton(text="operar",on_click=self.operarC))
            self.page.update()
        

    def operarC(self,event):

        nodos=[]
        Probalilida=[]
        ban=True
        CerosNodos = any(nodo.value.isdigit() and int(nodo.value) == 0 for nodo in self.num_Nodo)
        for i in range(len(self.num_Nodo)):
            try:
                n=int(self.num_Nodo[i].value)
            except:
                ban=False
        if(not CerosNodos and ban):
            
            for i in range(len(self.num_Nodo)): nodos.append(Nodo(self.env,int(self.num_Nodo[i].value),(15,30),nombre=f"{i}"))
            for nodo in nodos: self.env.process(nodo.llegada_cliente())

            self.env.run(until=100)

            for i in range(len(nodos)): Probalilida.append(nodos[i].Tlleg/nodos[i].Toper[1])
            res=Column(width=500,height=200,scroll=flet.ScrollMode.ALWAYS)
            resp=[]     
            for i in range(len(Probalilida)):resp.append(flet.Text(value="probabilidad de espera es {0}".format(Probalilida[i])))
            res.controls=resp
            self.page.add(res)
            self.page.update()
         
         