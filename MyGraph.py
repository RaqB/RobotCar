class MyGraph:
    def __init__(self, data):
        """
        Params:
                data <dict> - Los nodos y sus adyacentes
        """
        self.__data = data
        self.__actives = [True] * 36
        self.__getindex = lambda n: n % 10 + (6 * (n // 10))

    def __getitem__(self, node):
        """
        Retorna los nodos adyacentes al nodo entregado como argumento.
        Params:
                node <int> - Id del nodo
        """
        try:
            return self.__data[node]
        except Exception as e:
            raise e

    def __setitem__(self, node, value):
        """
        Activa o desactiva un nodo, para que pueda o no ser visitado
        Params:
                node <int> - Id del nodo
                value <bool> - True | False
        """
        try:
            index = self.__getindex(node)
            self.__actives[index] = value
        except Exception as e:
            raise e

    def isenabled(self, node):
        """
        Retorna True si el nodo entregado como argumento
        esta activado, de lo contrario False.
        Params:
                node <int> - Id del nodo
        """
        try:
            index = self.__getindex(node)
            return self.__actives[index]
        except Exception as e:
            raise e

    def reset(self, value=True):
        """
        Asigna a todos los nodos en valor pasado como argumento
        Params:
                value <bool> - True | False
        """
        try:
            for i in range(36):
                self.__actives[i] = value
        except Exception as e:
            raise e

    def direction(self, a, b=None):
        """
        Retorna la primera direccion entre el nodo a y el nodo b,
        si b es None, retorna la primera direccion entre el nodo a
        y si primer adyacente
        Params:
                a <int> - Id de un nodo cualquiera
                b <int> - Id de un nodo cualquiera
        """
        for i, n in enumerate(self.__data[a]):
            if n == b:
                return i
            if not b and n != -1:
                return i
