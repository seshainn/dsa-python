class Graph:
  def __init__(self):
    self.adj_list = {}

  def print_graph(self):
    for key, value in self.adj_list.items():
        print(key,':', value)

  def add_vertex(self, vertex):
    if vertex not in self.adj_list.keys():
        self.adj_list[vertex] = []
        return True
    return False

  def add_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True
    return False

  def remove_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): 
        try:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
        except ValueError:
            pass
        return True
    return False

  def remove_vertex(self, vertex):
    if vertex in self.adj_list.keys():
        for value in self.adj_list[vertex]:
            self.adj_list[value].remove(vertex)
        del self.adj_list[vertex]
        return True
    return False
  
  def dfs_traversal(self, start_vertex, visited=None):
     if visited is None:
        visited=set()
     if start_vertex not in self.adj_list:
        return
     visited.add(start_vertex)
     print(start_vertex, end=" ")     
     for vertex in self.adj_list[start_vertex]:
        if vertex not in visited:
          self.dfs_traversal(vertex, visited)
  
g = Graph()
g.add_vertex(7)
g.add_vertex(9)
g.add_vertex(4)
g.add_vertex(2)
g.add_edge(7,9)
g.add_edge(9,4)
g.add_edge(9,2)
g.add_edge(4,2)
g.print_graph()
g.dfs_traversal(7)
  