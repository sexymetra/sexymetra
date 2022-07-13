from telnetlib import VT3270REGIME
from turtle import st


class graph:
    def __init__(self, vertices=[], edges=[], graph_name='graph'):
        self.vertex = { tag:dict(name=vtx, post=[])
        for vtx,tag in vertices }
        self.edge = {edg:dict() for edg in edges}
        self.graph_name = graph_name

    def __str__(self):
        print( '>'*8 + self.graph_name + '-'*8 )
        print( self.vertex )
        print( self.edge )

        return '-'*8 +self.graph_name + '<'*8

    def post_vertex(self, cv_tag):
        return self.vertex.get(cv_tag,dict(post=[]))['post']
    
    def put_edge_on_vertex(self):
        for eg in self.edge:
            start, end = eg
            self.vertex[start]['post'] += [end]

    def get_vtag(self, vname):
        for vtg in self.vertex:
            if vname == self.vertex[vtg]['name']: return vtg
        else:
            print('no vertex with name {}'.formath(vname))
            return None