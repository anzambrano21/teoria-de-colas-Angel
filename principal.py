import flet
from flet import Page, Column,Row, ElevatedButton ,Text

class pruevas:
    def __init__(self,page:Page):
        self.page=page
        
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
            
            self.num_Nodo.append(flet.TextField(label="Nodo N "+str(i)+""))
        col=Column(self.num_Nodo)
        self.page.add(col)
        self.page.update()
         
         
def main(page:Page):
    page.window_height=400
    page.window_width=500
    
    page.window_resizable=False
    
    page.title="Teoria de nodos"
    pruevas(page)
    page.update()
if __name__=="__main__":

        flet.app(main)