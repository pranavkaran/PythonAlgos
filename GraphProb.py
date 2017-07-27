from collections import defaultdict
class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, n):
		visited = [False]*(len(self.graph))
		queue = []
		queue.append(n)
		visited[n] = True
		while queue :
			n = queue.pop(0)
			print n
			for i in self.graph[n]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print "Following is Breadth First Traversal (starting from vertex 2)"
g.BFS(2)

