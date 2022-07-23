#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            print("Path",path)
            node = path[-1]
            print("Node",node)
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                print("new_path",new_path)
                new_path.append(adjacent)
                print("new_path_append",new_path)
                queue.append(new_path)
                print("queue",queue)

customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

g = Graph(customDict)
print("Final Path",g.bfs("a", "f"))
