import design_graph as dsngrf

class mygraph(dsngrf.graph):
    def __init__ (self, vertices, edges, grfname):
        super().__init__( vertices, edges, grfname)

    def all_paths(self, v_s, v_d):

        def paths(v_s,v_d):
            if v_s == v_d:
              return [[]]

            path=[]
            for i in (self.post_vertex(v_s)):
                if not i in path:
                    for j in paths(i,v_d):
                        path.append([i] + j)
            return path
        result = []
        for k in paths(v_s,v_d):
            result.append([v_s]+k)
        return result
    
if __name__=='__main__':
    vs = [('v1',0),('v2',1),('v3',2),
    ('v4',3),('v5',4), ('v6',5)]
    
    es = [(0,1),(0,2),(1,3),(1,4),(2,1),
    (2,4),(3,5),(3,2),(4,5)]

    g1 = mygraph(vs,es,'graph_1')
    g1.put_edge_on_vertex()
    
    print(g1.all_paths(1,0))