def recurse(graph, node, paths, path=[]):
    # base case  (terminal node)    DONE
    if not graph[node]:
        # the first time we do this, 4 gets added to the path such that it gets copied on all future paths.
        if node == len(graph) - 1:
            paths.append(path + [node])
            return
        else:
            return
    
    # not base case
    new_path = path + [node]
    for i in graph[node]:
        recurse(graph, i, paths, new_path)
    
            
def csFindAllPathsFromAToB(graph):
    paths = []
    
    recurse(graph, 0, paths, [])
    
    return paths

graph = [[4,3,1], 
         [3,2,4], 
         [3], 
         [4], 
         []]

print(csFindAllPathsFromAToB(graph))