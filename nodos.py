import random
#creamos una clase de nodos con un tiempo de llegada y de atender
class nodo:
    def __init__(self,evn,Tlleg,Toper,nombre):
        self.even=evn
        self.Tlleg=Tlleg
        self.Toper=Toper
        self.nombre=nombre
    def llegada_cliente(self):
        while True:
            yield self.env.timeout(random.expovariate(1 / self.tasa_llegada))
            with self.cola.request() as req:
                yield req
                yield self.env.timeout(random.uniform(15, 30))  # Tiempo de servicio
