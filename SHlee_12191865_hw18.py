import design_graph as dsngrf

class Mygraph(dsngrf.graph):
    def __init__(self, vertices, edges, grfname):
        super().__init__(vertices, edges, grfname)
    
    def cycles(self, v):
        paths = []

        def dfs_paths(start, end, visited=[]):

            visited = visited + [start]
            
            if start == end:
                paths.append(visited)
            

            for node in self.post_vertex(start):
                if node not in visited:
                    dfs_paths(node, end, visited)
            
            return paths
        cycle_list= []
        for j in range(len(vs)-1):
            if v != j:
                dfs_paths(v , j)

        for w in paths:
            if v in self.post_vertex(w[-1]):
                w.append(v)
                cycle_list.append(w)
        for i ,j in enumerate(cycle_list):
            for x ,y in enumerate(j):  # j = [1,2,3,2]
                cycle_list[i][x] = self.vertex[y]['name']
                
        return cycle_list


if __name__=='__main__':               

    vs=[('v1',0),('v2',1),('v3',2),('v4',3),('v5',4),('v6',5)]
    es=[(0,1),(0,2),(1,3),(1,4),(2,1),(2,4),(3,5),(3,2),(4,5)]
    g1 = Mygraph( vs, es, 'graph_1')
    g1.put_edge_on_vertex()
    
    for vn in g1.vertex:
        print('cycles from {0}_vertex to itself'.format(vn))
        for path in g1.cycles(vn):
            print(path)