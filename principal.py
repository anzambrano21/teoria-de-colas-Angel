import flet
from flet import Page, Column,Row, IconButton ,Text

class pruevas:
    def __init__(self,page:Page):
        self.page=page
        num_Nodo=0
def main(page:Page):
    page.title="Teoria de nodos"
    pruevas(page)
if __name__=="__main__":

        flet.app(main)