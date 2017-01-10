
from cgraph.graphs import graph


class Node:       
    def __str__(self):
        return self.name if self.name is not None else self.__class__.__name__    
        
    def __repr__(self):
        return self.__str__()

    def forward(self, inputs):
        raise NotImplementedError()

    def ngradient(self, cache):
        raise NotImplementedError()

    @staticmethod
    def nary_function(klass, *args):   
        c = klass()
        for n in args:
            graph.add_edge(n, c)
        return c