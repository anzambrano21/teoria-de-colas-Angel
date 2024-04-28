import random
import simpy
#creamos una clase de nodos con un tiempo de llegada y de atender
class Nodo:
    def __init__(self,evn,Tlleg,Toper,nombre):
        self.even=evn
        self.Tlleg=Tlleg
        self.Toper=Toper
        self.nombre=nombre
        self.cola= simpy.Resource(evn, capacity=1)
    def llegada_cliente(self):
        while True:
            yield self.even.timeout(random.expovariate(1 / self.Tlleg))
            with self.cola.request() as req:
                yield req
                yield self.even.timeout(random.uniform(*self.Toper))  # Tiempo de servicio
                print(f"Cliente atendido en {self.nombre}.")
