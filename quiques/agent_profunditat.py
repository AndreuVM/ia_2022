""" Fitxer que conté l'agent barca en profunditat.

S'ha d'implementar el mètode:
    actua()
"""
from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca


class BarcaProfunditat(Barca):
    def __init__(self):
        super(BarcaProfunditat, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def actua(
            self, percep: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat_inicial = Estat(percep.to_dict())

        pass


    def cerca(self, estat_inicial: Estat):
        self.__oberts = [estat_inicial]
        self.__tancats = []
        while self.__oberts:
            estat_actual = self.__oberts.pop()
            if estat_actual.es_meta():
                break
            else:
                list = estat_actual.genera_fill()
                self.__tancats.append(estat_actual)
                for i in list:
                    self.__oberts.append(i)
        if estat_inicial.es_meta(): #devuelve el padre y la accion del hijo
            estat_pare = Estat(estat_inicial.pare.to_dict())
            while estat_pare is not None:
                self.__accions.append(estat_pare.acc_poss)
                estat_pare = Estat(estat_inicial.pare.to_dict())
            self.__accions.reverse()    
        pass
                

